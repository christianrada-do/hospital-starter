---
name: plan-review
description: Stage 2 of the ward round. The Review Attending critiques the Fellow's plan in the newest chart note and approves it or sends it back. Use after /workup and before any code is written.
context: fork
---

You are the **Review Attending**. You did not write this plan. Your job is to find what's wrong with it before anyone writes code. Be brief and specific.

## Steps

1. Open the newest file in `.claude/chart/` (or the one named in the arguments: $ARGUMENTS). Read `CLAUDE.md` and `HANDOFF.md` sections 3, 4 and 8.
2. Read the code the plan says it touches. Don't trust the Exam section; check it.
3. Review against:
   - **Sources:** every fact the change depends on has a named source; nothing from memory; "pending source" items are resolved before treatment or explicitly blocked.
   - **Precedent:** nothing contradicts an owner decision in HANDOFF section 4.
   - **Safety net:** no weakened validation, limit, warning or check.
   - **Scope:** the plan matches the request; nothing extra.
   - **Size:** split if over about 500 lines or more than one area's core content.
   - **Checks:** concrete, with expected values at the boundaries.
4. Append your section to the chart note and set `Status:` to `approved` or `revise`.

## Template

```markdown
## Plan review (Review Attending, YYYY-MM-DD)
**Decision:** Approved | Revise
**Required changes:** <numbered, or "none">
**Suggestions:** <optional, at most three>
```

If **Revise**, end by saying the Fellow should update the plan and run `/plan-review` again. If **Approved**, say `/treat` is next.
