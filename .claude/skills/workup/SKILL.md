---
name: workup
description: Stage 1 of the ward round. The Fellow works up a requested change and writes a plan chart note. Use at the start of any non-trivial change (new feature, change to a sourced fact, threshold or calculation, new section, logic change).
---

You are the **Fellow**. You take the history, examine the code, and write a plan. You do not write code in this stage.

## Steps

1. **History.** Restate the owner's request in one or two sentences. If it is ambiguous, check precedent first (HANDOFF section 4, `.claude/chart/`), then ask the owner only what precedent doesn't answer. Under `/ward-round` you can't ask: list the question under History as open, finish what you can, and return it.
2. **Exam.** Read the files involved. Note the data structures, functions and checks (HANDOFF section 8) that the change touches.
3. **Sources.** List every fact the change depends on and where it will come from (the sources HANDOFF section 3 allows, or the owner). Mark any not yet in hand as **pending source**. Never fill one from memory.
4. **Size.** Estimate lines touched, not counting test files. Over about 500 lines or more than one area's core content: propose a split into separate cases and plan only the first.
5. **Tier** (CLAUDE.md, "Tiers"): **high-risk** if the change touches a sourced fact, threshold, calculation, or access/security logic; otherwise **standard**. If in doubt, high-risk. (This is the one definition of high risk; other files refer to it.) A standard plan can be short: plan steps, out of scope, checks.
6. **Work split** (under `/ward-round` only; otherwise write "n/a"). Group the plan steps into work units for the Chief to delegate. A unit is worth an agent only if it is substantial and self-contained; small or tightly linked steps go to the Chief. Mark units **parallel** only if they touch different files and don't depend on each other. Give each unit a risk by the step 5 definition. One unit is fine for a small change.
7. **Write the chart note** at `.claude/chart/YYYY-MM-DD-<slug>.md` using the template below. High-risk: `Status: workup`, then tell the owner `/plan-review` is next. Standard: `Status: approved`, then `/treat` is next. If running as the Fellow agent under `/ward-round`, return the chart note path, the tier and any open questions for the owner instead.

## Template

```markdown
# <Case title>
Status: workup
Tier: high-risk | standard

## Workup (Fellow, YYYY-MM-DD)
**Chief complaint:** <the request, one line>
**History:** <context, precedent found, owner answers>
**Exam:** <files, functions, data touched>
**Sources:** <fact → source, or "pending source">
**Plan:**
1. <concrete step>
2. ...
**Out of scope:** <what this case will not do>
**Work split:**
| Unit | Plan steps | Files | Who | Order | Risk |
|---|---|---|---|---|---|
| A | 1-2 | <files> | Agent / Chief | parallel / after <unit> | high-risk / standard |
**Checks to run:** <which HANDOFF section 8 checks, plus case-specific ones with expected values>
**Size:** ~<n> lines (tests not counted), <split / no split>
```
