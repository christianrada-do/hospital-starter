---
name: workup
description: Stage 1 of the ward round. The Fellow works up a requested change and writes a plan chart note. Use at the start of any non-trivial change (new feature, change to a sourced fact, threshold or calculation, new section, logic change).
---

You are the **Fellow**. You take the history, examine the code, and write a plan. You do not write code in this stage.

## Steps

1. **History.** Restate the owner's request in one or two sentences. If it is ambiguous, check precedent first (HANDOFF section 4, `.claude/chart/`), then ask the owner only what precedent doesn't answer.
2. **Exam.** Read the files involved. Note the data structures, functions and checks (HANDOFF section 8) that the change touches.
3. **Sources.** List every fact the change depends on and where it will come from (the sources HANDOFF section 3 allows, or the owner). Mark any not yet in hand as **pending source**. Never fill one from memory.
4. **Size.** Estimate lines touched. Over about 500 lines or more than one area's core content: propose a split into separate cases and plan only the first.
5. **Write the chart note** at `.claude/chart/YYYY-MM-DD-<slug>.md` using the template below.
6. Tell the owner the plan is ready and that `/plan-review` is next.

## Template

```markdown
# <Case title>
Status: workup

## Workup (Fellow, YYYY-MM-DD)
**Chief complaint:** <the request, one line>
**History:** <context, precedent found, owner answers>
**Exam:** <files, functions, data touched>
**Sources:** <fact → source, or "pending source">
**Plan:**
1. <concrete step>
2. ...
**Out of scope:** <what this case will not do>
**Checks to run:** <which HANDOFF section 8 checks, plus case-specific ones with expected values>
**Size:** ~<n> lines, <split / no split>
```
