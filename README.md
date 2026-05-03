# 40K Kill Team Rules — Knowledge Base

This repository is the **knowledge base** for a future AI assistant that helps Warhammer 40,000 Kill Team players resolve rules questions, look up faction abilities, and settle disputes mid-game — without having to dig through the rulebook.

The AI assistant that serves players is **not implemented here**. This project's sole responsibility is to maintain accurate, structured rules content that the assistant can consume.

---

## What Lives Here

| File | Content |
|---|---|
| `kill_team_core_rules_guide.md` | Full core rules: phases, actions, shooting, fighting, melee, weapons, equipment |
| `targeting_quick_reference.md` | Decision checklists and matrices for shoot/fight legality and terrain effects |
| `tac_ops_reference.md` | All 24 universal Tac Ops cards across four archetypes with full scoring conditions |
| `wahapedia_links.md` | Verified wahapedia URL index with coverage status — used when expanding the knowledge base |
| `kill_team_core_rules_guide.pdf` | Styled A4 PDF of the core rules guide |
| `targeting_quick_reference.pdf` | Styled A4 PDF of the targeting reference |
| `tac_ops_reference.pdf` | Styled A4 PDF of the Tac Ops reference |
| `make_pdfs.py` | Renders the markdown files into PDFs (grimdark parchment aesthetic) |
| `kill_team_agent.py` | Kill Team expert agent — used to validate and extend the knowledge base |
| `USAGE.md` | How to use the `/kill-team` skill and the CLI agent |

Rules content is sourced from Wahapedia (Core Book, February 2026).

---

## Why There Is an Agent Here

`kill_team_agent.py` is a **Kill Team expert agent** powered by Claude, used as a development and maintenance tool for this knowledge base — not as the end-user assistant.

Its purpose in this repo:

- **Validate content accuracy** — query the knowledge base interactively to spot gaps, contradictions, or missing rules
- **Extend the knowledge base** — when the agent's local knowledge is insufficient, it fetches up-to-date content from [wahapedia.ru](https://wahapedia.ru) and [ktdash.app](https://ktdash.app) and can inform what needs to be written into the markdown files
- **Test coverage** — simulate the kinds of questions players will ask so the content can be refined before the consumer AI is built

The agent is a tool for the knowledge base author, not for players.

To run it:

```bash
export ANTHROPIC_API_KEY=your_key_here
python3 kill_team_agent.py
```

---

## Regenerating the PDFs

```bash
python3 make_pdfs.py
```

**Dependencies:** Python `reportlab` and DejaVu fonts at `/usr/share/fonts/truetype/dejavu/`.

```bash
pip install reportlab
# Ubuntu/Debian
sudo apt install fonts-dejavu
```

---

## How This Feeds the Future AI

The consumer AI (to be built in a separate project) will ingest the markdown files in this repo as its knowledge base. The design intent:

- Markdown is the source of truth — human-readable, diffable, easy to update
- PDFs are rendered views for human reference during playtesting
- The agent in this repo verifies the markdown is correct before the consumer AI ships

When rules change (new errata, new faction books), update the markdown here first, run the agent to validate, then regenerate the PDFs.
