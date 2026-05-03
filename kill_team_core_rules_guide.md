# Kill Team Core Rules — How to Play Guide

A clear, player-friendly breakdown of how Kill Team 3rd Edition works.

---

## What You Need

- Two kill teams (each with their own datacards)
- 10+ six-sided dice (D6)
- Tokens/order markers
- A measuring tape
- A killzone (game board) with terrain

---

## The Big Picture: How a Game Flows

A Kill Team game is played over **Turning Points** (typically 4). Each turning point has two phases:

```
Turning Point
├── 1. Strategy Phase   ← gain CP, use ploys
└── 2. Firefight Phase  ← activate operatives, shoot, fight
```

Repeat until all turning points are done. Victory is determined by mission objectives.

---

## STRATEGY PHASE (3 Steps)

### Step 1 — Initiative
- One player has **initiative** this turning point (they activate first and break ties).
- Turning point 1: the mission pack decides who has it.
- Turning points 2+: both players roll off; ties go to the player who did **not** have it last turn.

### Step 2 — Ready
- Each player gains **Command Points (CP)**:
  - **Initiative player:** 1 CP
  - **Non-initiative player:** 2 CP (a small compensation bonus)
- All your operatives become **ready** (flip order tokens to the light side).

### Step 3 — Gambit
- Starting with the initiative player, players alternate using **Strategic Gambits** (mostly Strategy Ploys).
- Spending CP on a ploy gives you a rules bonus for the turn.
- Once both players **pass consecutively**, the Gambit step ends.
- Each Strategic Gambit can only be used **once per turning point**.

---

## FIREFIGHT PHASE

Players alternate **activating** one ready operative at a time. Initiative player goes first.

When it's your turn to activate, pick a ready operative and do 3 things:

### Step 1 — Determine Order
Give the operative either:

| Order | Benefits | Restrictions |
|---|---|---|
| **Engage** | Full actions, can Counteract | No special protection |
| **Conceal** | Not a valid target while in cover | Cannot Shoot, Charge, or Counteract |

> **Tip:** Use Conceal on operatives you want to keep alive while repositioning. Use Engage on operatives ready to fight.

### Step 2 — Perform Actions
The operative spends **Action Points (AP)** up to their **Action Point Limit (APL)** — usually 2.

- You **cannot** perform the same action more than once per activation.
- If an action is cancelled mid-way, you don't spend the AP.

### Step 3 — Expended
After the operative is done, flip their token to the **dark side** (expended). They're done this turning point.

---

## ACTIONS

### Movement Actions

| Action | AP Cost | What it Does |
|---|---|---|
| **Reposition** | 1 | Move up to your Move stat. Cannot enter enemy control range unless a friendly is already there. Cannot combine with Fall Back or Charge. |
| **Dash** | 1 | Move up to 3". Cannot climb. Cannot combine with Charge. Cannot start/end in enemy control range. |
| **Fall Back** | 2 | Move while in enemy control range. Must start in control range; cannot end there. Cannot combine with Reposition or Charge. |
| **Charge** | 1 | Move up to Move + 2". Must **end** within enemy control range. Requires Engage order. Cannot combine with Reposition, Dash, or Fall Back. |

### Vertical Movement
- **Climb:** Must be within 1" horizontally and 3" vertically of terrain. Each climb counts as **minimum 2"** of movement.
- **Drop:** Ignore the first 2" of vertical distance when dropping (per action).
- **Jump:** From Vantage terrain higher than 2" above the floor, you can jump up to **4" horizontally**.

### Combat Actions

| Action | AP Cost | What it Does |
|---|---|---|
| **Shoot** | 1 | Ranged attack. Requires Engage order and not be in enemy control range. |
| **Fight** | 1 | Melee attack. Must have an enemy in your control range. |

### Objective Actions

| Action | AP Cost | What it Does |
|---|---|---|
| **Pick Up Marker** | 1 | Grab a controllable marker you're controlling. Cannot be in enemy control range or already carrying a marker. |
| **Place Marker** | 1 | Put down a carried marker within your control range. (If incapacitated, this costs 0 AP and happens automatically before removal.) |

---

## COUNTERACT

When **all your operatives are expended** but your opponent still has ready ones, you don't just sit there — you **Counteract**.

- Pick an expended operative with an **Engage order**.
- They perform **one free 1AP action** (excluding Guard).
- They **cannot move more than 2"** while counteracting.
- Each operative can Counteract **once per turning point**.
- This is NOT a normal activation — it's a reaction.

---

## SHOOTING (Step-by-Step)

### 1. Select Weapon
Collect D6s equal to the weapon's **Atk (Attack)** stat.

### 2. Select Valid Target
The target must be **visible** to your operative.
- If the target has a **Conceal order AND is in cover** → they are **not a valid target**.
- You **cannot** shoot if friendly operatives are within the target's control range (1").

### 3. Roll Attack Dice
Roll all your attack dice. A success = roll **equal to or higher** than the weapon's **Hit** stat.
- Roll a **6** = always a **critical success** (better damage).
- Roll a **1** = always a **failure**.

**Obscured target** (enemy is behind Heavy terrain, >1" away from both operatives):
- Discard one success from your roll.
- All critical successes become normal successes.

### 4. Roll Defence Dice
The defender rolls **3 defence dice**. A success = roll equal to or higher than their **Save** stat.

**Cover bonus:** If the defender is in cover (and has Engage order), they keep **one free normal success** automatically — before rolling.

### 5. Resolve Defence Dice
The defender uses their successes to **block** attacker successes:
- **Normal success** blocks **1 normal success**.
- **2 normal successes** can block **1 critical success**.
- **Critical success** blocks **any 1 success** (normal or critical).

### 6. Resolve Damage
Each unblocked attacker success inflicts damage:
- **Normal success** → Normal Damage (from weapon stat)
- **Critical success** → Critical Damage (from weapon stat, usually higher)

Reduce the target's **Wounds** by the damage total. If Wounds reach 0 or less → **Incapacitated** → removed from the killzone.

---

## FIGHTING (Melee — Step-by-Step)

### 1. Select Enemy Operative
Pick an enemy in your **control range** (within 1" and visible).
The enemy operative will **retaliate** this same action.

### 2. Select Weapons & Roll
- Both players **pick their melee weapon** and collect dice (Atk stat).
- Both players **roll simultaneously**.
- Hit successes work the same as shooting (meet or beat the Hit stat; 6 = crit; 1 = fail).

**Assisted Fighting:** If friendly operatives (not themselves in another enemy's control range) are within the **enemy's** control range, your melee Hit stat improves **by 1 for each** assisting operative.

### 3. Alternate Resolving Dice
Players take turns resolving one die at a time:
- **Strike** — inflict damage (normal or critical) and discard the die.
- **Block** — allocate to cancel an opponent's unresolved success.
  - Normal blocks Normal.
  - Critical blocks either Normal or Critical.

Keep going until one operative is **incapacitated** or all dice are resolved.

---

## KEY CONCEPTS

### Control Range
An operative is in **control range** of another if they are:
- Within **1"** AND
- **Visible** to each other

Control range is **mutual** — it applies to both operatives simultaneously.

### Cover
An operative is **in cover** if there is **intervening terrain within their control range**.

However, you **cannot** be in cover if you are within **2" of the attacker**.

### Obscured vs. In Cover
These are two different things:
- **In cover** = terrain is between you and the attacker, within your control range → defender gets a **cover save**.
- **Obscured** = Heavy terrain is between attacker and target, more than 1" from either → attacker **loses a success** and crits become normals.

### Wounds & Injury
| State | Condition | Penalty |
|---|---|---|
| **Healthy** | At or above starting Wounds | None |
| **Injured** | Below half starting Wounds | -2" Move, -1 to Hit (worse) |
| **Incapacitated** | 0 or fewer Wounds | Removed from killzone |

### Visibility
An operative is **visible** if you can draw a straight unobstructed line (1mm wide, imaginary) from your **operative's head** to any part of the **target's miniature** (not just the base).

An operative is always visible to itself.

### Markers & Objectives
- **Objective markers:** 40mm diameter.
- **Other markers:** 20mm diameter.
- An operative **contests** a marker if within control range of it.
- An operative **controls** a marker if the total APL of friendly operatives contesting it **exceeds** the enemy's total APL on the same marker.
- A **carried marker** is automatically controlled by the carrier.

---

## COMMAND POINTS & PLOYS

**Command Points (CP)** are the currency for activating ploys.

| Ploy Type | When Used | Notes |
|---|---|---|
| **Strategy Ploys** | Gambit step (Strategy Phase) | These are Strategic Gambits |
| **Firefight Ploys** | Firefight Phase | Used during the action phase |
| **Command Re-roll** | Anytime (1 CP) | Re-roll one attack or defence die |

Rules:
- Each non-Command ploy can only be used **once per turning point**.
- You **cannot** use the same Strategic Gambit more than once per turning point.

---

## DATACARDS

Every operative has a datacard that lists:

| Stat | What It Means |
|---|---|
| **APL** | Action Point Limit — how many actions per activation |
| **Move** | Distance in inches for Reposition/Charge (minimum 4") |
| **Save** | Defence dice target number (lower = better saves) |
| **Wounds** | How much damage they can take |
| **Atk** | Number of attack dice for a weapon |
| **Hit** | Roll needed to score a success (lower = more hits) |
| **Normal Dmg** | Damage per normal success |
| **Critical Dmg** | Damage per critical success |

**APL modifiers** cannot exceed ±1 from the base value.

---

## DICE RULES

- A **success** = rolling equal to or higher than the target number (e.g., 3+ means 3, 4, 5, or 6).
- **6** = always a critical success on attack dice.
- **1** = always a failure on attack dice.
- **Re-rolls:** Each die can be re-rolled once. You cannot re-roll a die that was already re-rolled.
- **Multiple simultaneous re-rolls:** Players alternate choosing to re-roll a die or pass, starting with the initiative player. Continue until both pass.
- **D3:** Roll a D6 and halve the result (round up). So: 1-2=1, 3-4=2, 5-6=3.

---

## PRECEDENCE (When Rules Conflict)

Kill Team uses this priority order:

1. An explicit statement that overrides normal rules
2. Designer commentary / FAQ
3. Non-core rules (faction rules, mission rules) beat core rules
4. "Cannot" beats "can"
5. The **active player** decides (when activating/acting)
6. The **initiative player** decides (all other ties)

---

## WEAPON SPECIAL RULES

Weapons can have one or more special rules (keywords) printed on their datacard. Here's what every keyword does:

### Re-roll Rules
| Keyword | Effect |
|---|---|
| **Balanced** | Re-roll **one** of your attack dice. |
| **Relentless** | Re-roll **any** of your attack dice (as many as you want). |
| **Ceaseless** | Re-roll any dice showing **one specific result** (e.g. all your 2s). |

### Auto-Success Rules
| Keyword | Effect |
|---|---|
| **Accurate x** | Retain up to **x** attack dice as normal successes **without rolling them** (free hits). |
| **Lethal x+** | Any success rolled at **x or higher** counts as a **critical success** instead. E.g. Lethal 5+ means 5s and 6s are both crits. |

### Converting Successes
| Keyword | Effect |
|---|---|
| **Rending** | If you retained any crits, you may also convert **one normal success to a critical**. |
| **Severe** | If you have **no crits**, you may change **one normal success to a critical**. |
| **Punishing** | If you retained any crits, you may also retain **one failed die as a normal success**. |

### Defence-Reducing Rules
| Keyword | Effect |
|---|---|
| **Piercing x** | Defender collects **x fewer defence dice**. E.g. Piercing 1 means they roll only 2 dice instead of 3. |
| **Saturate** | Defender **cannot retain cover saves**. Bypasses cover entirely. |
| **Seek** | When picking targets, operatives **cannot use terrain for cover**. |
| **Brutal** | Your opponent can **only block with critical successes** (normal successes are useless for blocking). |

### Melee-Specific Rules
| Keyword | Effect |
|---|---|
| **Shock** | The **first time you strike with a crit** in the sequence, also **discard one of your opponent's unresolved normal successes**. |

### Debuff Rules
| Keyword | Effect |
|---|---|
| **Stun** | If you retain any crits, subtract **1 from the target's APL** until the end of their next activation (they get fewer actions). |

### Area / Multi-Target Rules
| Keyword | Effect |
|---|---|
| **Blast x** | After shooting the primary target, also shoot against **every other operative visible and within x"** of the primary (each rolled separately). Cover/obscured status of secondary targets matches the primary target's. |
| **Torrent x** | Pick a primary target normally, then pick **any number of other valid targets within x"** of it (not in friendly control range) as secondary targets. Shoot against all of them separately. |

### Restriction Rules
| Keyword | Effect |
|---|---|
| **Heavy** | Cannot use this weapon in an activation where you **moved**, and cannot move in an activation where you **used** this weapon. |
| **Hot** | After using, roll 1D6. If the result is **less than the weapon's Hit stat**, the operative takes damage equal to the result × 2. |
| **Limited x** | After using this weapon **x times total in the battle**, it's gone. |
| **Range x** | Can only target operatives **within x"**. E.g. Range 9" limits you to close-range shots. |

### Special Action Rules
| Keyword | Effect |
|---|---|
| **Silent** | The operative can perform the Shoot action while having a **Conceal order** (normally you can't shoot on Conceal). |
| **Devastating x** | Each critical success immediately inflicts **x bonus damage** on top of the weapon's normal critical damage. |

---

## EQUIPMENT

Equipment gives your operatives extra tools and options. Selected **before the battle** as part of your game sequence.

**Rules:**
- **Universal equipment** — any kill team can use it.
- **Faction equipment** — specific to your kill team (listed in team rules).
- You **cannot** select the same equipment option more than once per game.

### Universal Equipment Options

| Equipment | What It Does |
|---|---|
| **Ammo Cache (×1)** | Place a cache marker. Operatives within control range can use a free **0AP Ammo Resupply action** to re-roll one attack die until the next turning point. |
| **Razor Wire (×1)** | Deploy terrain. Operatives moving within 1" of it treat that distance as **1" longer** (slows movement). Counts as Exposed and Obstructing terrain. |
| **Comms Device (×1)** | Place a marker. While friendly controlled, extends **support rule ranges** by 3". Cannot benefit from the opponent's Comms Device. |
| **Mines (×1)** | Place a marker. When any operative enters its control range, it triggers and inflicts **D3+3 damage** on that operative. |
| **Light Barricades (×2)** | Two pieces of Light terrain. Provide cover. Feet are insignificant/exposed. |
| **Heavy Barricade (×1)** | One piece of Heavy terrain providing robust cover. Must be placed **wholly within 4" of your drop zone**. |
| **Ladders (×2)** | Insignificant terrain. When climbing within control range of a ladder, treat the vertical distance as **only 1"** (makes climbing cheap). |
| **Portable Barricade (×1)** | A personal Light terrain shield. Improves the carrying operative's **Save stat by 1** (max 2+). Can be repositioned with the **Move with Barricade** action. |
| **Utility Grenades** | Two grenade-style limited-use actions. Typically smoke/stun combinations (exact options vary by selection). |
| **Explosive Grenades** | Two grenade options: **Frag** (4 Atk, 4+ Hit, 2/4 Dmg, Blast 2", Saturate) and **Krak** (4 Atk, 4+ Hit, 4/5 Dmg, Piercing 1, Saturate). Limited use. |
| **Breaching Charge (×1)** | One-use. Breach actions cost **1 fewer AP** (minimum 1AP). |

---

## QUICK REFERENCE SUMMARY

```
EACH TURNING POINT:
1. Strategy Phase
   a. Initiative — who goes first?
   b. Ready — gain CP (1 or 2), all operatives become ready
   c. Gambit — spend CP on ploys

2. Firefight Phase
   - Alternate activating operatives (initiative player first)
   - Each activation: Give Order → Do Actions → Expend
   - When your operatives are all expended → Counteract instead

WHEN SHOOTING:
Roll Atk dice → hit on Hit value (6=crit, 1=miss)
Defender rolls 3 defence dice + 1 auto if in cover
Defender blocks with successes
Remaining hits deal Normal or Critical Damage

WHEN FIGHTING:
Both roll simultaneously → alternate: Strike or Block
Critical > Normal for blocking priority

ORDERS:
Engage = full actions + counteract, no free cover
Conceal = in cover = untargetable, no shooting/charging

COVER = intervening terrain in your control range, NOT within 2" of attacker
OBSCURED = Heavy terrain between you and target (attacker loses 1 success, no crits)
CONTROL RANGE = within 1" AND visible
INJURED = below half wounds → -2" Move, -1 Hit
```

---

*Source: Wahapedia Kill Team 3rd Edition Core Rules (Core Book, February 2026)*
