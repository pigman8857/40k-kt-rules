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
| **Utility Grenades** | Select two grenades (2 Smoke, 2 Stun, or 1 of each). Each type is a limited-use 1AP action. |
| **Explosive Grenades** | Select two grenades (2 Frag, 2 Krak, or 1 of each). **Frag:** 4 Atk, 4+ Hit, 2/4 Dmg, Range 6", Blast 2", Saturate. **Krak:** 4 Atk, 4+ Hit, 4/5 Dmg, Range 6", Piercing 1, Saturate. Each limited use. |
| **Breaching Charge (×1)** | One-use. Breach actions cost **1 fewer AP** (minimum 1AP). |

### Utility Grenade Detail

**Smoke Grenade (1AP):** Place a smoke marker within 6" of your operative (must be visible, or on Vantage terrain). The marker creates a **1" horizontal smoke area**. Operatives **wholly within** the smoke area are **Obscured** to any operative 2" or more away. Additionally, Piercing 2/Crits 2 are reduced to Piercing 1/Crits 1 at range. The marker is removed after **D3 activations** or at the end of the turning point. Cannot use while in enemy control range.

**Stun Grenade (1AP):** Select a visible enemy within 6". That operative **and each operative within 1" of it** must pass a **stun test**: roll a D6 — on a **3+**, subtract 1 from that operative's APL until the end of its next activation. Cannot use while in enemy control range.

### Portable Barricade Detail

The Portable Barricade is **Protective** (Save +1, max 2+) and **Portable** (provides cover only when the carrying operative is connected to it and the barricade is intervening between the operative and the attacker).

**Move with Barricade (1AP):** Move up to your Move stat **minus 2"**. Cannot climb, drop, or jump. Remove the barricade before moving; reposition it after. Cannot place within 2" of other equipment. Cannot use while in enemy control range or in the same activation as Fall Back or Charge.

---

## GUARD ACTION

The **Guard** action lets an operative adopt a defensive stance, ready to react to enemy movements during their opponents' activations.

**Taking the Guard Action (1AP):**
- Requires **Engage order**.
- Cannot Guard while within **control range of an enemy operative**.
- Place a Guard token on the operative to track its status.

**How Guard Works:**
After any enemy operative performs an action, you may **interrupt** that enemy activation and select one friendly operative currently on Guard to perform a free **Fight or Shoot** action. You do not have to target the operative you interrupted — you can target any valid target.

**Guard Ends When:**
- The guarding operative performs any action or moves.
- The guarding operative's order changes.
- An enemy operative ends an action within the guarding operative's control range and you do **not** interrupt.
- The next turning point begins.

**Additional Restrictions:**
- A guarding operative that interrupts **cannot Counteract** that turning point.
- If making a Shoot action through Guard at point-blank range (while an enemy is in control range), the operative's Hit stat is worsened by 1 and it cannot retaliate until the enemy's activation ends.

> **Tip:** Guard is a powerful area-denial tool. An operative on Guard in a doorway forces enemies to think twice before running past. It is also the exception to the "you cannot perform the same action twice" rule — Guard triggers a new free action outside of normal activation.

---

## PRE-BATTLE SEQUENCE (Game Setup)

Before any turning points are played, follow these five steps:

### Step 1 — Set Up the Battle
1. Agree on the mission pack and select a mission (or roll for it).
2. Set up the killzone: place terrain with their specified terrain types.
3. Place **objective markers** on the killzone floor in the specified positions.
4. Roll off — winner has **initiative** for the setup steps.
5. Initiative player selects their **drop zone**; opponent takes the other.

### Step 2 — Select Operatives
1. Each player **secretly selects** their operatives according to their kill team's selection rules.
2. Both players **reveal simultaneously**.
3. Each player **secretly selects up to four equipment options** (no duplicates per player).
4. Both players reveal equipment simultaneously.
5. Each player gains **2 Command Points (CP)**.

### Step 3 — Set Up Operatives
1. Players **alternate placing equipment items** (initiative player first), then opponents place theirs.
2. Players **alternate setting up one-third of their operatives** (rounded up) within their drop zone, starting with the initiative player.
3. Each operative placed this way receives a **Conceal order**.

### Step 4 — Play the Battle
- Roll off for **initiative in Turning Point 1** (ties broken by the player who did not have initiative during setup).
- Play turning points as normal (see game flow above).

### Step 5 — End the Battle
- After four turning points (or when one kill team is fully incapacitated), the battle ends.
- The player with the **most Victory Points wins**. Ties are a draw.

---

## KILL TEAM CONSTRUCTION

Kill teams are assembled according to each faction's selection rules (printed in their team rules). Generally:

- Each kill team is selected from a **fixed roster** of operative types.
- Most kill teams field **8–15 operatives** depending on their faction rules.
- You cannot take duplicate operatives unless the kill team's rules specifically allow it.
- Each operative has a **datacard** listing its stats, weapons, and any special rules.

**APL Cap:** APL modifiers (from injuries, ploys, or equipment) can never take an operative's effective APL more than ±1 above or below its base value.

---

## TERRAIN TRAITS (Full Reference)

Terrain in Kill Team is described by one or more **traits**. These traits combine to define what the terrain does:

| Trait | Rules Effect |
|---|---|
| **Heavy** | Provides cover save. If >1" from both shooter and target, causes Obscured penalty. |
| **Light** | Provides cover save only — never causes Obscured. |
| **Wall** | Fully blocks Line of Sight AND blocks movement. Also provides cover and causes Obscured. |
| **Exposed** | Never provides cover. Never causes Obscured. (Examples: ladders, grates, terrain bases.) |
| **Blocking** | Represents gaps beneath/between terrain. LoS cannot pass through the gap. For cover/obscured, the gap counts as intervening terrain like the solid terrain around it. |
| **Accessible** | Operatives can move through it, but doing so counts as 1" extra movement. Only the **centre of the base** needs to pass through — base size is irrelevant. |
| **Insignificant** | Ignored for climbing and dropping calculations. Operatives move over it without height change. |
| **Vantage** | An upper level operatives can be placed upon (above the killzone floor). Operatives on Vantage terrain gain bonuses against lower targets (see below). |
| **Ceiling** | Operatives with a **round base ≤ 50mm or oval base 60×35mm** can move underneath Ceiling terrain regardless of operative height. |
| **Protective** | Improves the carrying/attached operative's Save stat by 1 (max 2+). |
| **Obstructing** | Operatives moving within 1" of this terrain treat that distance as 1" longer. |

### Vantage Terrain — Shooting Bonuses

When an operative on **Vantage terrain** makes a Shoot action against an enemy with **Engage order**:

| Target is Lower by... | Bonus |
|---|---|
| 2" or more | **Accurate 1** (retain 1 attack die as a free normal success without rolling) |
| 4" or more | **Accurate 2** (retain 2 attack dice as free normal successes without rolling) |

Additionally:
- Operatives with **Conceal order** that are 2" or more lower than a Vantage shooter **cannot use Light terrain for cover** (though they keep any improved Save stat bonuses).
- For the purposes of **Obscured**, ignore any Heavy terrain that is connected to the Vantage terrain that both the shooter and target occupy simultaneously.

---

## KILLZONE-SPECIFIC RULES

### Gallowdark (Close Quarters — Enclosed Vessel)

Gallowdark is an enclosed starship corridor environment. Its walls are solid Wall terrain — LoS and movement are fully blocked by them.

**Close Quarters Special Rule:**
Weapons with the **Blast**, **Torrent**, and/or **Devastating x"** weapon rules also have the **Lethal 5+** weapon rule while in this killzone. This means 5s and 6s on attack dice both count as critical successes — reflecting how devastating explosives are in enclosed spaces.

**Hatchways:**
Hatchways have two states — Closed and Open.

| State | Access Point | Hatch Piece |
|---|---|---|
| **Closed** | Heavy + Wall (fully blocks LoS/movement) | Heavy + Wall |
| **Open** | Accessible + Insignificant + Exposed | Heavy + Wall (gap underneath = Blocking) |

**Operate Hatch (1AP):** Open or close a hatchway whose access point is within your control range.
- Can be performed *during* a Dash or Reposition if movement remains.
- Cannot perform while within enemy control range.
- Cannot perform if the hatchway is open and its access point is within an **enemy's** control range.

**Hatchway Fight (1AP):** Fight across an **open** hatchway. Select an enemy on the opposite side of the access point within **2"** while your base is touching the access point.
- Both operatives are treated as being within each other's control range for the duration of the action.
- Cannot perform while within enemy control range.

---

### Tomb World (Ancient Facility)

**Hatchways** work identically to Gallowdark (see above).

**Breach Points:**
Breach points are a permanent alternative to hatchways — once opened, they stay open.

| State | Access Point | Breach Wall |
|---|---|---|
| **Closed** | Heavy + Wall (fully blocks LoS/movement) | Heavy + Wall |
| **Open** (permanent) | Accessible + Insignificant + Exposed | Removed permanently |

**Breach (2AP or 1AP):** Open a closed breach point whose access point is within your control range.
- Costs **1AP** (instead of 2) if the operative has a **breach marker**, **grenadier**, or **mine** keyword on their datacard, or is using a weapon with **Piercing 2** or **Piercing Crits 2** (but not if the weapon also has Blast or Torrent).
- **Damage:** Roll a D6 for each operative on the other side of the access point that has it within their control range. On a **4+**, subtract 1 from that operative's APL until the end of its next activation, and inflict damage equal to half the dice result (rounded up).
- Cannot perform while within enemy control range.
- Cannot perform if the breach point is already open.
- Cannot perform in the same activation as a Charge or Shoot action if cost-reduced to 1AP.

**Teleport Pads:**
The Tomb World contains two Teleport Pads (Exposed, Insignificant, Vantage terrain). Only **one operative** may occupy a pad at a time. Operatives on a pad cannot touch the killzone floor.

From **Turning Point 2** onward: when a friendly operative on a Teleport Pad performs a **Charge, Fall Back, or Reposition** action, you may **teleport it instead** — remove it and place it on the other Teleport Pad, still fulfilling all other action requirements (e.g. a Charge must still end in enemy control range). An operative cannot teleport more than once per activation.

If another operative already occupies the destination pad, the two **swap positions**. If the occupant is an enemy, their controlling player places them.

---

### Compound Siege (Fortified Positions — Volkus)

The Compound Siege upgrade adds fortified structures (stockades and bunkers) with special shooting and movement rules.

**Visibility:** LoS cannot be drawn **over** the Heavy terrain of a bunker or stockade unless the drawing operative is at least **2" higher** in elevation.

**Windows:** Work like standard windows — LoS through a window requires you or the target to be within **1" horizontally** of the window. Additionally:
- Weapons with **Piercing** are ignored by defenders firing through or being shot through a **fortified window** (the fortification neutralises armour-penetrating rounds).
- For **Blast/Torrent** weapons, secondary targets must be on the **same side** of the fortification as the primary target.
- **Devastating** effects only apply to operatives on the same side as the primary target.

**Fighting:** When fighting across a fortified position (window only, not breach points), the **defender resolves their dice first**.

**Climbing:** Treat vertical distance on fortified Heavy terrain as **4"** (making climbing very costly).

**Open Stockade Door (1AP):** Open a closed stockade door if its interior access point is within your control range. Can only be used from **inside** the stockade. Cannot perform if the door is already open.

---

### Bheta-Decima (Industrial Platform — Hazardous Areas)

This killzone features Gantries (elevated platforms) and Hazardous Areas (toxic/predator-infested zones).

**Gantries:**
- Gantry floors are **Accessible** and **Vantage** terrain.
- Gantry pillars are **Heavy** terrain.
- Connected gantries (floors touching) are treated as the **same terrain feature**.
- The Thermometric Condenser: roof is Accessible + Vantage; roof inner-ledge is Exposed + Insignificant; battlements are Light; all other parts are Heavy.

**Hazardous Areas:**
- **No part of any operative's base may touch a Hazardous Area.** Operatives must navigate around them.
- **Floor-to-floor targeting:** An operative on the killzone floor **cannot target** another floor operative if **4" or more of Hazardous Area** lies along the targeting line between them.
- **Vantage-to-floor targeting:** An operative on Vantage terrain cannot target a floor operative if the **footprint of a gantry** lies along the targeting line — except for gantries the shooter or target is actually on.
- Use targeting lines to determine whether a Hazardous Area or gantry footprint intervenes.

**Equipment Placement:** Equipment may be set up on **Vantage terrain** and within **2" of Accessible terrain** in this killzone (overriding the usual floor-only restriction).

---

## APPROVED OPS 2025 — COMPETITIVE MISSIONS

Approved Ops 2025 is the standard competitive mission pack. It adds initiative cards, a three-op scoring system, and tac ops.

### Initiative Cards

The **loser** of each turning point's initiative roll-off gains an **initiative card** (except Turning Point 4):

| Turning Point | Card Gained by Loser |
|---|---|
| 1 (setup) | Re-roll Initiative card |
| 2 | +2/−2 Initiative card |
| 3 | +3/−3 Initiative card |
| 4 | No card |

**Re-roll Initiative card:** Play before or after rolling to re-roll your initiative die.
**+X/−X cards:** After rolling, modify your result up or down by X (can go above 6 or below 1).

Players alternate playing initiative cards or passing (both pass consecutively to end the step). The +X/−X value gives the loser a significant swing in later turns.

### The Three Ops

Each battle scores from three parallel objectives simultaneously:

#### 1. Kill Op (max 6 VP)
Track how many enemy operatives you incapacitate using a **Kill Grade** scale.

| Kill Grade | Score |
|---|---|
| Advance to each new grade | **+1 VP** |
| Your grade > opponent's grade at battle end | **+1 VP** |

Kill grade thresholds are based on the **starting size** of the enemy kill team. Example for a 10-operative team:

| Grade | Operatives Incapacitated |
|---|---|
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| 5 | 10 |

#### 2. Crit Op (max 6 VP)
One shared Crit Op is selected (or randomly determined) before the battle. During each turning point, operatives perform mission actions on objective markers. Available Crit Ops include:

| Crit Op | Mission Action | Scoring |
|---|---|---|
| **Secure** | 1AP — one marker you control is **secured** (remains yours until enemy secures it) | 1VP per secured marker; +1VP if you control more than opponent |
| **Loot** | 1AP — one marker you control is **looted** | 1VP per loot action (max 2VP/turn) |
| **Transmission** | 1AP — one marker you control is **transmitting** until next turn start | 1VP per transmitting marker; +1VP if more transmitting than opponent |
| **Orb / Stake Claim / Energy Cells / Download / Data / Reboot** | Various objective-marker interactions | Varies |

**Mission action restrictions (all Crit Ops):** Cannot perform the mission action during Turning Point 1, or while within control range of an enemy operative.

#### 3. Tac Op (max 6 VP)
Each player secretly selects **one Tac Op** from their kill team's eligible archetypes. Tac Ops are personal hidden objectives.

**Archetypes:** Each kill team is assigned one or more archetypes — **Infiltration**, **Recon**, **Security**, or **Seek & Destroy**. You pick one Tac Op from any archetype your team has access to.

**Revelation:** Each Tac Op specifies when it should be revealed. Some must be revealed when you complete them; others at battle end.

**Scoring:** Up to 6VP from your chosen Tac Op.

### Primary Op

During **Turning Point 1's Gambit step**, each player secretly selects one of their three ops (Crit, Kill, or Tac) as their **Primary Op** (place a face-down card or conceal a die under a cup).

At the **end of the battle**, both players reveal their Primary Op simultaneously and score **additional VP equal to half their earned VP from that op** (rounded up).

**Maximum 6VP per op** — the Primary Op bonus uses the same capped score.

### Game Sequence Summary (Approved Ops 2025)

```
PRE-BATTLE:
  1. Select kill teams per faction rules
  2. Set up killzone + terrain types
  3. Select shared Crit Op; place objective markers
  4. Roll-off for initiative → winner picks drop zone
  5. Loser gains Re-roll Initiative card
  6. Secretly select operatives → reveal simultaneously
  7. Secretly select up to 4 equipment → reveal simultaneously
  8. Both players gain 2 CP
  9. Secretly select Tac Op
  10. Alternate placing equipment, then setting up operatives (1/3 at a time, Conceal order)

TURNING POINT 1:
  Strategy Phase:
    • Roll initiative (initiative cards can be played)
    • Ready operatives, gain CP
    • Gambit: secretly select Primary Op (face-down) + other ploys
  Firefight Phase: normal activations

TURNING POINTS 2-4:
  Strategy Phase:
    • Roll-off; loser gains initiative card (TP 2&3 only)
    • Alternate playing initiative cards or passing
    • Ready + gain CP + Gambit ploys
  Firefight Phase: normal activations

END OF BATTLE:
  • Reveal Primary Op simultaneously
  • Score +half VP from Primary Op (rounded up)
  • Most VP wins; ties = draw
```

---

## JOINT OPS — CO-OPERATIVE / SOLO MISSIONS

Joint Ops is the PvE mission pack. One or two players control a kill team against **Non-Player Operatives (NPOs)**.

### Kill Team Selection (Joint Ops)
- Players use one kill team. Solo: select normally. Co-op: split operatives between two players or each take half.
- NPOs use generic **procedural datacards** — no faction selection.

### NPO Initiative & Gambits
- NPOs **always claim initiative** if they win the roll-off.
- NPOs **always pass** during the Gambit step.

### NPO Behaviours

Each NPO follows one of two behaviour templates:

**Brawler (melee-focused):**
Priority action sequence: Fight → Charge → Reposition toward closest enemy with cover → Dash toward closest enemy with cover.
Chooses Engage if it can Fight or Charge; otherwise Conceal.

**Marksman (ranged-focused):**
Priority action sequence: Fall Back to cover with valid targets → Shoot → Reposition to cover with valid targets → Dash to cover with valid targets.
Chooses Engage if it can Shoot; otherwise Conceal.

### Threat Principle
When NPOs make decisions (targeting, movement, etc.), always apply the **Threat Principle**: NPOs choose the option that is **worst for the players**. This governs:
- Which enemy operative to target (the most dangerous one in range)
- Which direction to move (toward the most threatening player operative)
- Tie-breaking in activation order

### NPO Datacard Tiers

| Tier | Role |
|---|---|
| **Trooper** | Basic operative; low Wounds and average stats |
| **Tough** | More resilient than a Trooper; harder to eliminate |
| **Warrior** | Elite combat unit; strong attacks |
| **Heavy** | Counts as **2 operatives** for incapacitation scoring; significantly higher Wounds |

### Joint Ops Missions

**Mission 1 — Breach:**
- NPOs (combined 90 Wounds) are deployed with Conceal order in cover.
- **Players win:** All NPOs incapacitated.
- **NPOs win:** All player operatives incapacitated.

**Mission 2 — Sabotage:**
- NPOs (combined 90 Wounds) with reinforcements triggered when half are incapacitated.
- **Mission Action (1AP):** One objective marker you control is **sabotaged**.
- **Players win:** All objective markers sabotaged.
- **NPOs win:** All player operatives incapacitated.

**Mission 3 — Escape:**
- NPOs (combined 77 Wounds) with reinforcements.
- Player operatives that move **wholly off the NPO killzone edge** are removed as **escaped**.
- **Players win:** More than 50% of operatives escape.
- **NPOs win:** All player operatives incapacitated before >50% escape.

---

## MULTIPLAYER OPS — 3 AND 4 PLAYER MISSIONS

Multiplayer Ops supports 3–4 players using combined board layouts.

### Player Order
All players roll D6 — highest becomes **first player** (acts as initiative player), second highest goes second, and so on. This order applies throughout the battle for all initiative-related decisions.

### Scoring

**Elimination Op (replaces Kill Op):**
Track how many enemy operatives each player incapacitates per turning point. Heavy operatives count as **two** for incapacitation scoring. At each turning point end, rank all players:
- **1st place:** 2VP
- **2nd place:** 1VP
- **3rd/4th place:** 0VP

**Crit Op:** Identical to Approved Ops 2025 Crit Op but with higher maximum VP caps per marker (up to 3VP per marker per turn for 4-player games).

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
