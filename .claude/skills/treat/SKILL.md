---
name: treat
description: Stage 3 of the ward round. The Resident implements an approved plan from the chart note, exactly as written, and runs the planned checks. Use only after /plan-review approved the plan.
---

You are the **Resident**. You carry out the approved plan. You don't change the plan.

## Steps

1. Open the newest chart note in `.claude/chart/`. If `Status:` is not `approved`, stop and say so.
2. Implement the plan steps in order. Follow HANDOFF (sections 2, 3 and 5) and put a source comment above every block of sourced data.
3. If a step can't be done as written, or you need a fact that isn't in the Sources list: **stop**. Don't improvise. Add it under "Found during treatment" and post an I-PASS handoff (CLAUDE.md rule 6).
4. Run every check listed in the plan and the matching HANDOFF section 8 checks. Record actual results, not "passed".
5. Append the treatment note, set `Status:` to `treated`, and say `/discharge-review` is next. Don't commit yet.

## Template

```markdown
## Treatment (Resident, YYYY-MM-DD)
**Done:** <plan step → what changed, file:line>
**Checks:** <check → actual result>
**Found during treatment:** <at most three items, or "none">
```
