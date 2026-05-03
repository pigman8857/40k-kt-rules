# Kill Team — Targeting Quick Reference

---

## PART 1 — CAN I SHOOT? (Run through in order, stop at first NO)

```
STEP 1 — CHECK YOURSELF
┌─────────────────────────────────────────────────────────────┐
│  Do I have ENGAGE order?                                    │
│  YES → continue   NO → CANNOT SHOOT                        │
│  (Exception: weapon has SILENT keyword → can shoot anyway) │
└─────────────────────────────────────────────────────────────┘

STEP 2 — CHECK MY POSITION
┌──────────────────────────────────────────────────────────────┐
│  Am I within 1" of ANY enemy operative?  (control range)    │
│  NO → continue   YES → CANNOT SHOOT                         │
└──────────────────────────────────────────────────────────────┘

STEP 3 — CHECK TARGET VISIBILITY
┌────────────────────────────────────────────────────────────────────────┐
│  Can I draw an unobstructed 1mm-wide line from MY HEAD to any part of  │
│  TARGET'S MINIATURE (not base)?                                        │
│  YES → continue   NO → CANNOT SHOOT (not visible)                     │
└────────────────────────────────────────────────────────────────────────┘

STEP 4 — CHECK IF TARGET IS A VALID TARGET
┌───────────────────────────────────────────────────────────────────────┐
│  See the TARGET STATUS TABLE below.                                   │
│  Valid → continue   Not Valid → CANNOT SHOOT                          │
└───────────────────────────────────────────────────────────────────────┘

STEP 5 — CHECK FOR FRIENDLIES
┌───────────────────────────────────────────────────────────────────────┐
│  Are any FRIENDLY operatives within 1" of the TARGET? (their         │
│  control range)                                                       │
│  NO → ✅ YOU CAN SHOOT   YES → CANNOT SHOOT                          │
└───────────────────────────────────────────────────────────────────────┘
```

---

## PART 2 — TARGET STATUS TABLE (Step 4 above)

| Target's Order | Target in Cover? | Valid Target? | Defender Gets Cover Save? |
|---|---|---|---|
| **ENGAGE** | Not in cover | ✅ Valid | ❌ No save |
| **ENGAGE** | In cover | ✅ Valid | ✅ Yes — free normal save die |
| **CONCEAL** | Not in cover | ✅ Valid | ❌ No save |
| **CONCEAL** | In cover | ❌ **NOT VALID — cannot target** | — |

> **When is a target "in cover"?**
> There is intervening terrain (Light, Heavy, or Wall — **not Exposed**) within the **target's** control range (within 1" of them),
> AND the target is **NOT within 2" of you** (the shooter).
> Exposed terrain (ladders, grates, terrain feet) **never** counts as cover.

---

## PART 3 — SHOT MODIFIER TABLE (after confirming valid target)

These don't block the shot — they change how your dice work:

| Situation | Effect on Dice |
|---|---|
| Target in cover, **Engage** order (Light or Heavy terrain) | Defender keeps **+1 free normal success** before rolling |
| Target **obscured** — **Heavy** terrain between you, **>1" from both** operatives | Attacker **discards 1 success**; all crits become normals |
| Target in cover **AND** obscured | Both apply — lose a success AND defender gets free save |
| Target behind **Light** terrain only | Cover save only — **no obscured penalty** |
| Target behind **Exposed** terrain only | **Nothing** — no cover, no obscured |
| Target behind **Wall** terrain | Cover save + obscured (but usually LoS is blocked entirely first) |
| Shooting through a **window** (valid LoS) | Normal cover/obscured still apply based on other terrain |
| Shooting through a **window** in a fortified position | **Piercing is ignored** by defender |
| **Seek** weapon | No cover save for target |
| **Saturate** weapon | No cover save for target |
| **Piercing x** weapon | Target rolls **x fewer** defence dice |
| **Brutal** weapon | Target can only block with **critical** successes |

---

## PART 4 — CAN I FIGHT (MELEE)? (much simpler)

```
STEP 1 — CHECK RANGE
┌───────────────────────────────────────────────────────────────┐
│  Is the enemy within 1" of me (horizontal distance only)?    │
│  NO → CANNOT FIGHT   YES → continue                          │
└───────────────────────────────────────────────────────────────┘

STEP 2 — CHECK VISIBILITY
┌────────────────────────────────────────────────────────────────────────┐
│  Can I draw an unobstructed 1mm-wide line from MY HEAD to any part of  │
│  TARGET'S MINIATURE?                                                   │
│  YES → ✅ YOU CAN FIGHT   NO → CANNOT FIGHT                           │
└────────────────────────────────────────────────────────────────────────┘
```

> **No order restriction for Fight** — you can fight on either Engage or Conceal.
> **No cover or friendly restriction for Fight** — cover only affects shooting.
> **No "valid target" check** — Conceal order doesn't protect against melee.

---

## PART 5 — TERRAIN TYPE MATRIX

This is the core of most confusion. Each terrain type has different effects on **Line of Sight**, **Cover**, and **Obscured**.

### Terrain Type Effects

| Terrain Type | Blocks Line of Sight? | Gives Cover? | Causes Obscured? | Notes |
|---|---|---|---|---|
| **Light** | ❌ No | ✅ Yes | ❌ No | Most crates, barrels, low walls |
| **Heavy** | ❌ No* | ✅ Yes | ✅ Yes (if >1" from both) | Large ruins, thick walls, big containers |
| **Exposed** | ❌ No | ❌ **Never** | ❌ No | Ladders, grates, feet of terrain — never counts as intervening |
| **Wall** | ✅ **Yes — fully** | ✅ Yes | ✅ Yes | Solid walls; LoS and movement blocked completely |
| **Insignificant** | ❌ No | ❌ No | ❌ No | Ignored for movement height; operatives move over freely |
| **Accessible** | ❌ No | ✅ Yes | Depends on type | Can move through but costs extra 1"; only base centre needs to pass through |
| **Blocking** (gaps) | ✅ Yes (gap only) | ✅ Yes | ✅ Yes | Gaps/undersides that LoS cannot pass through |
| **Vantage** | ❌ No | ✅ Yes | Depends | Upper levels — shooter gains Accurate 1 or 2 against lower Engage targets |
| **Ceiling** | ❌ No | ✅ Yes | Depends | Small-based operatives (≤50mm round, 60×35mm oval) can move underneath regardless of height |

> *Heavy terrain does NOT block line of sight on its own — it causes **Obscured** instead. LoS can still be drawn through it; the target just gets the obscured penalty.

---

### How Cover Works With Terrain Types

Cover requires **intervening terrain within target's 1"** that is **not Exposed** and target is **not within 2" of shooter**.

| What's between you and the target | Cover? | Obscured? |
|---|---|---|
| Light terrain within target's 1" | ✅ Cover save | ❌ Not obscured |
| Heavy terrain within target's 1" | ✅ Cover save | ✅ Also obscured (if >1" from both of you) |
| Exposed terrain only | ❌ No cover | ❌ No obscured |
| Wall terrain | ✅ Cover save (if within target's 1") | ✅ Obscured |
| No terrain at all | ❌ No cover | ❌ No obscured |

---

## PART 5b — WINDOWS & DOORS

### Windows

> Default rule: **LoS cannot be drawn through a window** unless you or the target is within **1" horizontally** of it.

| Your distance from window | Target's distance from window | Can you draw LoS through it? |
|---|---|---|
| Within 1" | Anywhere | ✅ Yes |
| Anywhere | Within 1" | ✅ Yes |
| More than 1" | More than 1" | ❌ No — LoS blocked |

**Additional window rules:**
- Weapon special rule **Piercing is ignored** when shooting through a fortified window (bunkers/stockades).
- If LoS is valid through a window, normal cover/obscured rules still apply based on terrain between you and the target.

---

### Doors & Hatches

| Door State | Terrain Type | Blocks LoS? | Blocks Movement? | Cover/Obscured? |
|---|---|---|---|---|
| **Closed** | Heavy + Wall | ✅ Yes | ✅ Yes | ✅ Both |
| **Open** | Accessible + Insignificant + Exposed | ❌ No | ❌ No | ❌ Neither |

**How to open a door/hatch:**
- **Operate Hatch (1AP):** Open or close a hatchway. Cannot do this if an enemy is within your control range, or if the hatchway/access point is in an enemy's control range.
- **Breach (2AP, or 1AP with Piercing 2+ weapon / breaching charge / breach marker):** Permanently opens a breach point. Nearby operatives may take damage (roll D6: on 4+ take damage equal to half result, and APL –1).

**Fighting through a closed door:**
- Use the **Door Fight** action — select an enemy on the **other side** of the door within **2"** while your operative is touching the door.
- Normal fight rules apply otherwise.

---

## PART 5c — HEIGHT INTERACTIONS

Kill Team measures **horizontal distance only** — height doesn't count toward range.

| Situation | Rule |
|---|---|
| Two operatives on **different floor levels** | Horizontal distance still only 1" for control range, but **visibility may be blocked** by the floor/ceiling terrain between them |
| Shooting **down from a high floor** to a low floor | Check line of sight — if the floor is solid terrain blocking the line, no LoS → cannot shoot |
| Shooting **up** to an operative on a ledge | Same — need unobstructed LoS from your head to any part of their miniature |
| Enemy is on a **vantage point** (terrain >2" high) | They can jump down up to 4" horizontally; you can shoot them normally if LoS exists |
| Cover when on **different levels** | Cover still applies — if there's intervening terrain within the target's control range (even a railing or ledge edge), they may be in cover |
| Obscured when on **different levels** | Heavy terrain must be between you and the target along the targeting line — height changes the angle of that line |

---

## PART 5d — VANTAGE TERRAIN SHOOTING RULES

**Vantage terrain** is the upper level of a killzone — a surface above the killzone floor that operatives can be placed upon.

Being on Vantage terrain grants **Accurate** bonuses when shooting Engage-order targets below you:

| Height Difference | Bonus |
|---|---|
| Target is **2" or more** lower | **Accurate 1** — retain 1 attack die as a free normal success (no roll needed) |
| Target is **4" or more** lower | **Accurate 2** — retain 2 attack dice as free normal successes (no roll needed) |

**Cover interaction with Vantage:**

| Situation | Cover Rule |
|---|---|
| You're on Vantage, target has **Conceal** order and is **2"+ lower** | Target **cannot use Light terrain for cover** (still retains any improved Save stat) |
| You're on Vantage, target has **Engage** order | Normal cover rules apply |
| **Obscured** with Vantage terrain | Ignore Heavy terrain **connected to the Vantage terrain** that both you and your target occupy simultaneously |

> **Vantage is powerful but limited:** The Accurate bonus only applies against Engage-order targets. Conceal targets on the ground lose their Light terrain cover but retain Engage-order cover against your shots — they just can't use Light terrain specifically.

---

## PART 5e — KILLZONE-SPECIFIC TARGETING RULES

Different killzones add special targeting restrictions. Check which applies to your game:

### Close Quarters (Gallowdark Killzone)

Weapons with **Blast**, **Torrent**, or distance-based **Devastating** also gain **Lethal 5+** in this killzone. This means 5s AND 6s count as critical successes on attack dice — not just 6s.

| Weapon Keyword | Extra Rule in Gallowdark |
|---|---|
| **Blast x** | Also gains Lethal 5+ |
| **Torrent x** | Also gains Lethal 5+ |
| **Devastating x"** | Also gains Lethal 5+ |

### Fortified Positions (Compound Siege Killzone)

| Situation | Targeting Rule |
|---|---|
| Shooting **through a fortified window** | Defender ignores **Piercing** weapon rule entirely |
| Blast/Torrent with fortified position | Secondary targets must be on the **same side** as the primary target |
| Devastating weapon with fortified position | Bonus damage only applies to operatives on the **same side** as the primary target |
| Fighting across a fortified window | **Defender resolves dice first** (reversed from normal) |
| Drawing LoS **over** a bunker/stockade | Requires shooter to be **2" higher** in elevation than the fortification Heavy terrain |

### Bheta-Decima Hazardous Areas

| Situation | Targeting Rule |
|---|---|
| Two operatives **on the floor**, 4"+ of Hazardous Area between them | Not a valid target — **cannot shoot** |
| Operative on **Vantage**, targeting floor operative with gantry footprint between them | Not a valid target — **cannot shoot** (unless shooter or target is on that gantry) |

---

## PART 6 — FULL SHOOT/FIGHT DECISION AT A GLANCE

```
Want to SHOOT?                          Want to FIGHT?
─────────────────────────────────────   ──────────────────────────────
✅ I have ENGAGE order?                 ✅ Enemy within 1" (horizontal)?
✅ I'm NOT within 1" of any enemy?      ✅ Enemy is visible to me?
✅ Target is VISIBLE to me?             → GO — order/cover don't matter
✅ Target is valid?
   • ENGAGE → always valid if visible
   • CONCEAL + NOT in cover → valid
   • CONCEAL + IN COVER → ❌ STOP
✅ No friendly within 1" of target?
→ GO — check modifiers table above
```

---

## PART 7 — CONTROL RANGE REFERENCE

Control range = within **1" AND visible** (mutual — applies to both operatives).

| Used For | How |
|---|---|
| Fighting | Must be in enemy control range to Fight |
| Shooting restriction | Cannot shoot if you are in any enemy's control range |
| Friendly fire restriction | Cannot shoot at a target if a friendly is in the target's control range |
| Cover | Target needs intervening terrain within their own control range |
| Objective markers | Contesting/controlling requires being within control range of the marker |
| Assisted fighting | Friendlies in the **enemy's** control range (not in another enemy's CR) help improve your Hit stat |

---

## CHEAT CARD (print or screenshot this)

```
╔═══════════════════════════════════════════════════════════════╗
║         SHOOT CHECKLIST              FIGHT CHECKLIST          ║
╠═══════════════════════════════════════════════════════════════╣
║  □ I have ENGAGE order                □ Enemy within 1" (H)  ║
║    (or weapon is SILENT)              □ Enemy is visible      ║
║  □ I'm NOT within 1" of ANY enemy     → DONE. Fight.         ║
║  □ Target is VISIBLE (see LoS rules)  No order/cover checks. ║
║  □ Target is VALID:                                           ║
║    • ENGAGE order      → always valid                         ║
║    • CONCEAL, no cover → valid                                ║
║    • CONCEAL, in cover → ❌ cannot shoot                      ║
║  □ No FRIENDLY within 1" of target                            ║
╠═══════════════════════════════════════════════════════════════╣
║  MODIFIERS after valid target confirmed:                      ║
║  In cover (Light/Heavy, Engage) → +1 free save               ║
║  Obscured (Heavy terrain >1" from both) → lose 1 success,    ║
║    your crits become normals                                  ║
║  Light terrain only → cover save, NO obscured                 ║
║  Exposed terrain    → nothing at all                          ║
╠═══════════════════════════════════════════════════════════════╣
║  TERRAIN at a glance:                                         ║
║  LIGHT  → cover save only                                     ║
║  HEAVY  → cover save + obscured (if >1" from both)           ║
║  WALL   → blocks LoS fully (also cover + obscured)            ║
║  EXPOSED→ never cover, never obscured (ladders, grates, feet) ║
╠═══════════════════════════════════════════════════════════════╣
║  WINDOWS:                                                     ║
║  LoS blocked through window UNLESS you or target              ║
║  is within 1" horizontally of the window                      ║
╠═══════════════════════════════════════════════════════════════╣
║  DOORS (closed = Heavy+Wall = fully blocks LoS+movement):     ║
║  Open with Operate Hatch (1AP) — can't if enemy in CR         ║
║  Breach (2AP, or 1AP with Piercing 2+/breaching charge)       ║
║  Fight THROUGH closed door with Door Fight action (within 2") ║
╠═══════════════════════════════════════════════════════════════╣
║  IN COVER = non-Exposed terrain within target's 1",           ║
║             AND target NOT within 2" of you (shooter)         ║
║  (H) = horizontal distance only — height doesn't count        ║
╚═══════════════════════════════════════════════════════════════╝
```
