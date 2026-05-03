# Kill Team Rules Assistant — Usage Guide

Two tools are available for querying Kill Team rules. Choose based on your situation:

| Tool | Best for | Conversation? | Faction rules? |
|---|---|---|---|
| `/kill-team` skill | Quick lookup inside Claude Code | No — single turn | No |
| `kill_team_agent.py` | Full session, follow-ups, faction questions | Yes | Yes (fetches wahapedia) |

---

## 1. `/kill-team` — Claude Code Skill

A project-local skill that answers rules questions directly inside your Claude Code session without leaving the editor.

### Requirements

- Must be running Claude Code (`claude`) inside this project directory
- No API key setup needed — uses the current session

### How to invoke

```
/kill-team <your question>
```

Or without a question to be prompted:

```
/kill-team
```

### Examples

```
/kill-team can I shoot through a window while in cover?
/kill-team what happens when an operative is injured?
/kill-team how does the obscuring rule work with heavy terrain?
/kill-team what is the difference between light and heavy cover?
/kill-team can I use a ploy after my opponent declares an action?
```

### What it covers

- Core rules, phases, actions (shoot, fight, dash, guard, pick up, mission actions)
- Terrain traits, cover, obscuring, line of sight
- Wounds, injury, incapacitation
- Orders (Engage / Conceal)
- Equipment (universal)
- Tac Ops (all 24 universal cards)
- Approved Ops 2025 scoring system

### What it does NOT cover

Faction-specific rules — operative datasheets, faction ploys, unique equipment. For those, the skill will direct you to wahapedia.ru. Use the agent (below) for faction questions.

### Notes

- Single-turn only — it reads the knowledge base and gives one answer. If you need to follow up with more context, ask again with the full question.
- Answers cite the relevant rule by name so you can verify at the table.

---

## 2. `kill_team_agent.py` — Interactive CLI Agent

A full conversational expert agent that maintains context across questions and can fetch live rules content from wahapedia.ru when the local knowledge base is insufficient.

### Requirements

- Python 3.10+
- `anthropic` Python package
- An Anthropic API key

**Install dependencies (first time only):**

```bash
pip install anthropic
```

### Setup

Set your API key in the terminal before running:

```bash
export ANTHROPIC_API_KEY=your_key_here
```

To avoid setting this every session, add it to your shell profile (`~/.bashrc` or `~/.zshrc`):

```bash
echo 'export ANTHROPIC_API_KEY=your_key_here' >> ~/.bashrc
```

### Running the agent

```bash
python3 kill_team_agent.py
```

The agent loads the knowledge base, prints a banner, and waits for your question:

```
Kill Team Expert:  42,000 chars loaded.

You: ▌
```

### How to use it

Type your question and press Enter. The agent replies and waits for your next question. You can follow up naturally:

```
You: can I shoot through a Gallowdark window?

Kill Team Expert: In Gallowdark, windows are open hatches in sealed walls...

You: what if there's a friendly operative standing next to the window?

Kill Team Expert: A friendly operative standing next to the window does not
                  block your line of sight — only enemy operatives and terrain
                  can impose the obscuring rule...
```

The agent remembers everything said earlier in the session, so you do not need to repeat context.

### When the agent fetches from the web

If you ask about a faction, operative datasheet, or errata not in the local knowledge base, the agent will automatically fetch the relevant page from wahapedia.ru. You will see it announce the fetch:

```
  → [fetch_web_page] {"url": "https://wahapedia.ru/kill-team3/kill-teams/intercession-squad/"}
```

This uses your API tokens and takes a few seconds. The agent only fetches from `wahapedia.ru` and `ktdash.app` — all other URLs are blocked.

### Quitting

Type any of the following, or press `Ctrl-C`:

```
exit
quit
q
```

### Example session

```
You: what actions can I take on my activation?

Kill Team Expert: On your activation you can perform up to two actions from
                  this list: Move, Shoot, Fight, Dash, Guard, Pick Up, and
                  any mission actions available to your operative...

You: can I shoot twice?

Kill Team Expert: No. Each operative can perform the Shoot action only once
                  per activation. However, some faction ploys or abilities
                  may allow additional shooting — check your kill team's
                  rules for exceptions...

You: I'm playing Intercession Squad, do they have anything like that?

  → [fetch_web_page] {"url": "https://wahapedia.ru/kill-team3/kill-teams/intercession-squad/"}

Kill Team Expert: The Intercession Squad does not have a ploy that grants
                  an additional Shoot action. Their Aggressors can use
                  "Covering Fire" which triggers after an enemy shoots...
```

---

## Choosing the right tool

**Use the `/kill-team` skill when:**
- You are already in a Claude Code session
- The question is about core rules, terrain, Tac Ops, or universal mechanics
- You want a fast one-off ruling

**Use `kill_team_agent.py` when:**
- You want a back-and-forth conversation with follow-up questions
- The question involves a specific faction, operative, or ploy
- You want the agent to look up live errata or rules you suspect may have changed
- You are validating or expanding the knowledge base
