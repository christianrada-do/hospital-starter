---
name: discharge-review
description: Stage 4 of the ward round. The Review Attending reviews the code diff and the Discharge Nurse audits it against the plan, sources and HANDOFF checks before commit. Use after /treat.
context: fork
---

You review the work with fresh eyes in two roles. You did not write this code.

## As the Review Attending (code)

1. Open the newest chart note in `.claude/chart/`. Its `Status:` must be `treated`.
2. Read `git diff` in full. Look for: wrong math, unit mix-ups, off-by-one at boundaries, missing limits, null/undefined/NaN paths, broken access or security logic, errors in the console or logs.
3. Check that every changed sourced value matches its source as cited in the chart note and the code comment.

## As the Discharge Nurse (audit)

4. Every plan step is done; nothing outside the plan changed (compare diff to plan).
5. No weakened safety net (CLAUDE.md rule 3).
6. Re-run at least three checks yourself, including the riskiest boundary, plus HANDOFF section 8's "All changes" checks.
7. Sources and HANDOFF are updated if content or decisions changed.

## Then

Append your section and set `Status:` to `discharged` or `readmit`.

```markdown
## Discharge review (Attending + Nurse, YYYY-MM-DD)
**Decision:** Discharge | Readmit
**Code findings:** <numbered, file:line, or "none">
**Audit:** <plan steps ✓/✗, safety net ✓/✗, re-run checks with results>
```

If **Readmit**, say the Resident should fix the findings and run `/discharge-review` again. If **Discharge**, tell the main session to commit the code, then commit the chart note separately, and ask the owner before pushing or deploying.
