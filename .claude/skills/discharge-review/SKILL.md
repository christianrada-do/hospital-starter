---
name: discharge-review
description: Stage 4 of the ward round. The Review Attending reviews the code diff and the Discharge Nurse audits it against the plan, sources and HANDOFF checks before commit. Use after /treat.
context: fork
background: false
---

You review the work with fresh eyes in two roles. You did not write this code.

## As the Review Attending (code)

1. Open the chart note named in the arguments ($ARGUMENTS), or the newest one in `.claude/chart/` if none is named. Its `Status:` must be `treated`.
2. Read `git diff` in full. Look for: wrong math, unit mix-ups, off-by-one at boundaries, missing limits, null/undefined/NaN paths, broken access or security logic, errors in the console or logs.
3. Check that every changed sourced value matches its source as cited in the chart note and the code comment.
4. If the chart note has a `## Per-unit review` section, verify each finding there and carry the real ones into yours. Still read the full diff.

## As the Discharge Nurse (audit)

5. Every plan step is done; nothing outside the plan changed (compare diff to plan).
6. No weakened safety net (CLAUDE.md rule 3).
7. Re-run at least three checks yourself, including the riskiest boundary, plus HANDOFF section 8's "All changes" checks. A check that passed at the Treatment **Baseline** and fails now is blocking.
8. Sources and HANDOFF are updated if content or decisions changed.

## Then

Mark each code finding **blocking** (wrong result, unsafe, broken check, outside the plan) or **minor**. Readmit only if there is a blocking finding or a failed audit item; minor findings go under "Found during treatment". Append your section and set `Status:` to `discharged` or `readmit`.

```markdown
## Discharge review (Attending + Nurse, YYYY-MM-DD)
**Decision:** Discharge | Readmit
**Code findings:** <numbered, file:line, blocking / minor, or "none">
**Audit:** <plan steps ✓/✗, safety net ✓/✗, re-run checks with results>
```

If **Readmit**, say the Resident should fix the findings and run `/discharge-review` again. If **Discharge**, tell the main session to commit the code, then commit the chart note separately, and ask the owner before pushing or deploying.
