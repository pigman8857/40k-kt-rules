# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

A Kill Team 3rd Edition rules reference project. Three markdown files contain human-readable rules guides; `make_pdfs.py` renders them into styled A4 PDFs with a grimdark parchment aesthetic. Rules content is sourced from Wahapedia (Core Book, February 2026).

## Regenerating the PDFs

```bash
python3 make_pdfs.py
```

This overwrites both PDFs in place. No build system or test runner — this is the only command needed.

**Dependencies:** `reportlab` (Python) and DejaVu fonts at `/usr/share/fonts/truetype/dejavu/`. DejaVu is required (not optional) because the targeting reference uses Unicode box-drawing characters (┌│└╔║╚) that standard PDF fonts cannot render.

## Architecture of make_pdfs.py

The script has four layers:

**1. Custom Flowables** — ReportLab `Flowable` subclasses that draw directly to the PDF canvas rather than using built-in elements:
- `GoldRule` — gold horizontal rule with diamond ends (used for `---` separators and under H1)
- `SectionBanner` — full-width dark red bar with gold left accent (used for H2 headings)
- `CodeBlock` — dark background block using `DVMono`; draws text line-by-line with per-token colour highlighting for `✅/YES` (green) and `❌/NO/CANNOT` (red)
- `BlockQuote` — parchment box with gold left bar (used for `>` blockquotes)

**2. `parse_md(text)`** — Line-by-line state machine that converts markdown to a ReportLab `story` list. Tracks state for: code blocks, tables (accumulates header + rows before flushing), bullet groups, and numbered lists. Each state flushes when a different element type is encountered.

**3. `guess_col_widths(header)`** — Heuristic that maps table header content to column width ratios from `COL_CONFIGS`. **Critical constraint:** all checks use exact header matches (`h[0] == 'stat'`) with explicit column-count guards (`n == 2`), not substring checks. This was a fixed bug — `'stat' in 'state'` is True, which caused the Wounds & Injury table (3-col) to receive a 2-element width list, blowing the table past the page margin.

**4. `build_pdf(md_path, pdf_path, doc_title)`** — Wires everything together: reads markdown → `parse_md` → `SimpleDocTemplate.build` with a page callback (`make_page_template`) that draws the dark red header bar and footer on every page.

## Adding a New Document

1. Write the content as a `.md` file following the existing markdown conventions.
2. Add a `build_pdf(...)` call at the bottom of `make_pdfs.py`.
3. If the new file contains tables whose headers don't match any existing `COL_CONFIGS` key, add an entry to `COL_CONFIGS` and a corresponding exact-match guard in `guess_col_widths`. Always use `h[0] == 'exact string'` with `n == column_count` — never bare substring checks.

## Kill Team Expert Agent

`kill_team_agent.py` is an interactive CLI chatbot powered by `claude-opus-4-7`.

```bash
python3 kill_team_agent.py
```

**Requires:** `ANTHROPIC_API_KEY` environment variable.

The agent:
- Loads the two markdown files above as a cached knowledge base (prompt caching on system prompt — cheap repeated queries)
- Answers questions about rules, factions, operatives, missions, tactics
- Uses two tools when local knowledge is insufficient:
  - `fetch_web_page(url)` — fetches text from wahapedia.ru or ktdash.app
  - `fetch_image(url)` — fetches and vision-reads an image from those same domains
- Domain allowlist is hard-coded to `wahapedia.ru` and `ktdash.app` only; all other URLs are blocked
- Thinking (`adaptive`) is enabled; tool-use agentic loop runs until Claude returns `end_turn`

## Project-Local Claude Code Skill

A `/kill-team` skill is available inside this project session only. Invoke it to ask rules questions directly in Claude Code without leaving the editor:

```
/kill-team can I shoot through a window while in cover?
```

The skill reads both knowledge base markdown files and answers with precise rule citations. Faction-specific questions (operative datasheets, faction ploys) are out of scope — it will direct those to wahapedia.ru.

Skill file: `.claude/skills/kill-team.md`

## Source Files

| File | Purpose |
|---|---|
| `kill_team_core_rules_guide.md` | Full core rules: phases, actions, shooting, fighting, weapons, equipment |
| `targeting_quick_reference.md` | Decision checklists and matrices for shoot/fight legality and terrain effects |
| `tac_ops_reference.md` | All 24 universal Tac Ops cards across four archetypes with full scoring conditions |
| `wahapedia_links.md` | Verified wahapedia URL index — jump directly to source pages; tracks what is/isn't captured yet |
| `make_pdfs.py` | PDF generator — edit this to change layout, colours, or add documents |
| `kill_team_agent.py` | Interactive CLI expert agent with web fetch tools |
| `.claude/skills/kill-team.md` | Project-local Claude Code skill — invoke with `/kill-team` |
