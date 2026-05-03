#!/usr/bin/env python3
"""Kill Team 40K Expert Agent — Interactive CLI rules advisor."""

import os
import sys
import base64
import json
import re
import html as html_mod
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

import anthropic

SCRIPT_DIR = Path(__file__).parent
MODEL = "claude-opus-4-7"
MAX_TOKENS = 8192
ALLOWED_DOMAINS = {"wahapedia.ru", "www.wahapedia.ru", "ktdash.app", "www.ktdash.app"}

# ── Knowledge base ────────────────────────────────────────────────────────────

def load_knowledge_base() -> str:
    files = [
        "kill_team_core_rules_guide.md",
        "targeting_quick_reference.md",
    ]
    parts = []
    for fname in files:
        path = SCRIPT_DIR / fname
        if path.exists():
            parts.append(f"## {fname}\n\n{path.read_text()}")
    return "\n\n---\n\n".join(parts)


def build_system(knowledge_base: str) -> list:
    return [
        {
            "type": "text",
            "text": (
                "You are a Warhammer 40,000 Kill Team 3rd Edition expert — a master of the rulebook, "
                "all faction kill teams, operatives, ploys, equipment, missions, and the competitive meta.\n\n"
                "Your job: answer player questions about rules, resolve disputes, explain how mechanics "
                "interact, and help players get better at the game. Be precise about rule wording, cite "
                "the relevant rule when useful, and give clear examples.\n\n"
                "You have two tools available:\n"
                "• fetch_web_page — fetch text from wahapedia.ru/kill-team3 or ktdash.app\n"
                "• fetch_image — fetch and view an image from those same sites\n\n"
                "Use these tools when a question covers a faction, operative, or rule not in your local "
                "knowledge base, or when you want to verify up-to-date stats/errata."
            ),
        },
        {
            "type": "text",
            "text": f"# LOCAL KNOWLEDGE BASE\n\n{knowledge_base}",
            "cache_control": {"type": "ephemeral"},
        },
    ]


# ── Tool definitions ──────────────────────────────────────────────────────────

TOOLS = [
    {
        "name": "fetch_web_page",
        "description": (
            "Fetch the text content of a page on wahapedia.ru or ktdash.app. "
            "Use for faction rules, operative datasheets, missions, FAQs, errata, "
            "or any Kill Team content not in the local knowledge base."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "URL on wahapedia.ru or ktdash.app."}
            },
            "required": ["url"],
        },
    },
    {
        "name": "fetch_image",
        "description": (
            "Fetch and visually inspect an image on wahapedia.ru or ktdash.app. "
            "Use for datacard images, stat tables, mission diagrams, or any visual content."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "Image URL on wahapedia.ru or ktdash.app."}
            },
            "required": ["url"],
        },
    },
]


# ── Tool implementations ──────────────────────────────────────────────────────

def _allowed(url: str) -> bool:
    try:
        return urlparse(url).netloc in ALLOWED_DOMAINS
    except Exception:
        return False


def _fetch_bytes(url: str, timeout: int = 15) -> tuple[bytes, str]:
    """Return (content_bytes, content_type). Raises on error."""
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 Kill-Team-Expert-Bot/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read(), resp.headers.get_content_type() or ""


def _html_to_text(html: str) -> str:
    try:
        import html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = True
        h.body_width = 0
        return h.handle(html)
    except ImportError:
        pass
    html = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<(br|p|div|h[1-6]|li|tr)[^>]*>", "\n", html, flags=re.IGNORECASE)
    html = re.sub(r"<[^>]+>", "", html)
    html = html_mod.unescape(html)
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html.strip()


def tool_fetch_web_page(url: str) -> list:
    if not _allowed(url):
        return [{"type": "text", "text": f"Blocked: only wahapedia.ru and ktdash.app are allowed. Got: {url}"}]
    try:
        content, ctype = _fetch_bytes(url)
        charset = "utf-8"
        if "charset=" in ctype:
            charset = ctype.split("charset=")[-1].split(";")[0].strip()
        text = _html_to_text(content.decode(charset, errors="replace"))
        if len(text) > 40000:
            text = text[:40000] + "\n\n[... content truncated at 40 000 chars ...]"
        return [{"type": "text", "text": text}]
    except Exception as exc:
        return [{"type": "text", "text": f"Error fetching {url}: {exc}"}]


def tool_fetch_image(url: str) -> list:
    if not _allowed(url):
        return [{"type": "text", "text": f"Blocked: only wahapedia.ru and ktdash.app are allowed. Got: {url}"}]
    try:
        content, ctype = _fetch_bytes(url)
        if not ctype.startswith("image/"):
            return [{"type": "text", "text": f"URL returned non-image content-type: {ctype}"}]
        return [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": ctype.split(";")[0].strip(),
                    "data": base64.standard_b64encode(content).decode(),
                },
            }
        ]
    except Exception as exc:
        return [{"type": "text", "text": f"Error fetching image {url}: {exc}"}]


def dispatch_tool(name: str, inputs: dict) -> list:
    if name == "fetch_web_page":
        return tool_fetch_web_page(inputs.get("url", ""))
    if name == "fetch_image":
        return tool_fetch_image(inputs.get("url", ""))
    return [{"type": "text", "text": f"Unknown tool: {name}"}]


# ── Agent turn ────────────────────────────────────────────────────────────────

CYAN  = "\033[1;36m"
GREEN = "\033[1;32m"
AMBER = "\033[33m"
RESET = "\033[0m"
BOLD  = "\033[1m"


def run_turn(client: anthropic.Anthropic, messages: list, system: list) -> None:
    """Run one user turn through the agentic loop (tool calls included)."""
    printed_header = False

    while True:
        with client.messages.stream(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=system,
            tools=TOOLS,
            thinking={"type": "adaptive"},
            messages=messages,
        ) as stream:
            # Stream text blocks to terminal
            for text in stream.text_stream:
                if not printed_header:
                    print(f"\n{CYAN}Kill Team Expert:{RESET} ", end="", flush=True)
                    printed_header = True
                print(text, end="", flush=True)

            response = stream.get_final_message()

        # Append assistant turn (including any thinking/tool_use blocks)
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason != "tool_use":
            if printed_header:
                print()  # final newline after streamed text
            elif not printed_header:
                # Claude returned nothing (shouldn't normally happen)
                print(f"\n{CYAN}Kill Team Expert:{RESET} [no response]")
            break

        # Execute tools
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                arg_preview = json.dumps(block.input)[:120]
                print(f"\n{AMBER}  → [{block.name}] {arg_preview}{RESET}", flush=True)
                result_content = dispatch_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result_content,
                })

        messages.append({"role": "user", "content": tool_results})
        # Reset header flag so continuation text gets the label
        printed_header = False


# ── Main CLI ──────────────────────────────────────────────────────────────────

BANNER = f"""{AMBER}
╔══════════════════════════════════════════════════════════════════╗
║    ██╗  ██╗██╗██╗     ██╗         ████████╗███████╗ █████╗ ███╗ ║
║    ██║ ██╔╝██║██║     ██║            ██╔══╝██╔════╝██╔══██╗████╗║
║    █████╔╝ ██║██║     ██║            ██║   █████╗  ███████║██╔██╗║
║    ██╔═██╗ ██║██║     ██║            ██║   ██╔══╝  ██╔══██║██║╚██╗║
║    ██║  ██╗██║███████╗███████╗       ██║   ███████╗██║  ██║██║ ╚═╝║
║                                                                  ║
║         40K  KILL TEAM  EXPERT  —  Rules & Tactics Advisor       ║
║     Type your question below. 'exit' or Ctrl-C to quit.          ║
╚══════════════════════════════════════════════════════════════════╝{RESET}"""


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic()

    print(BANNER)
    print("Loading knowledge base...", end="", flush=True)
    kb = load_knowledge_base()
    system = build_system(kb)
    print(f" {len(kb):,} chars loaded.\n")

    messages: list = []

    while True:
        try:
            user_input = input(f"{GREEN}You:{RESET} ").strip()
        except (EOFError, KeyboardInterrupt):
            print(f"\n\n{BOLD}Good luck in your games, commander!{RESET}")
            break

        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "q"):
            print(f"\n{BOLD}Good luck in your games, commander!{RESET}")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            run_turn(client, messages, system)
        except anthropic.AuthenticationError:
            print("\nError: Invalid API key. Check ANTHROPIC_API_KEY.", file=sys.stderr)
            break
        except anthropic.RateLimitError:
            print(f"\n{AMBER}Rate limited — please wait a moment and try again.{RESET}")
            messages.pop()  # remove unsent user message so it can be retried
        except anthropic.APIConnectionError:
            print("\nNetwork error. Check your internet connection.", file=sys.stderr)
            messages.pop()
        except Exception as exc:
            print(f"\nUnexpected error: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
