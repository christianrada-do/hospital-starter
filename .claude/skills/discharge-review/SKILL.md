---
name: discharge-review
description: Stage 4 of the ward round. The Review Attending reviews the code diff and the Discharge Nurse audits it against the plan, sources and HANDOFF checks before commit. Use after /treat on a high-risk case (/discharge-check runs it for standard cases).
context: fork
background: false
model: inherit
---

You review the work with fresh eyes in two roles. You did not write this code.

## As the Review Attending (code)

1. Open the chart note named in the arguments ($ARGUMENTS), or the newest one in `.claude/chart/` if none is named. Its `Status:` must be `treated`.
2. Read `git diff` in full. Look for: wrong math, unit mix-ups, off-by-one at boundaries, missing limits, null/undefined/NaN paths, broken access or security logic, errors in the console or logs.
3. Check that every changed sourced value matches its source as cited in the chart note and the code comment.
4. If the chart note has a `## Per-unit review` section, verify each finding there and carry the real ones into yours. Still read the full diff.
5. Run `.claude/skills/claudy-comment-detector/SKILL.md` on the comments and doc text the diff adds or changes. Each finding is a **comment fix** with its exact replacement (or "remove"). Never remove a source citation.

## As the Discharge Nurse (audit)

6. Every plan step is done; nothing outside the plan changed (compare diff to plan).
7. No weakened safety net (CLAUDE.md rule 3).
8. Re-run at least three checks yourself, including the riskiest boundary, plus HANDOFF section 8's "All changes" checks. A check that passed at the Treatment **Baseline** and fails now is blocking.
9. Sources and HANDOFF are updated if content or decisions changed.

## Then

Mark each code finding **blocking** (wrong result, unsafe, broken check, outside the plan) or **minor**; minor findings go under "Found during treatment". Decide:

- **Discharge:** no blocking finding, no comment fix, and no failed audit item.
- **Discharge with fixes** (status `discharged`): every blocking finding and comment fix is a small, exact fix that touches no sourced fact, threshold, calculation, or access/security logic.
- **Readmit:** anything else.

Append your section and set `Status:`. Check pages with text tools; take screenshots only for a visual change.

```markdown
## Discharge review (Attending + Nurse, YYYY-MM-DD)
**Decision:** Discharge | Discharge with fixes | Readmit
**Code findings:** <numbered, file:line, blocking / minor, or "none">
**Comment fixes:** <numbered, file:line, rule, exact replacement or "remove", or "none">
**Audit:** <plan steps ✓/✗, safety net ✓/✗, re-run checks with results>
```

If **Readmit**, say the Resident should fix the findings and run the review again. If **Discharge with fixes**, say the main session applies each fix exactly, re-runs the affected checks, notes them under "Fixes applied (post-review)", and commits with no second review. If **Discharge**, tell the main session to commit the code, then commit the chart note separately, and ask the owner before pushing or deploying.
