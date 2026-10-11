---
name: ward-round
description: Runs the whole ward round in a row for one change — workup, plan review, treatment, discharge review — stopping only when the owner is needed. Use when the owner says "ward round", "do all four", or "run the full round" on a change.
---

Run the four stages for this request: **$ARGUMENTS**

1. Invoke the `workup` skill with the request.
2. Invoke the `plan-review` skill. If it says **Revise**, update the plan to address every required change and run `plan-review` again. After **two** Revise rounds, stop and post an I-PASS handoff (CLAUDE.md rule 6).
3. Invoke the `treat` skill.
4. Invoke the `discharge-review` skill. If it says **Readmit**, fix the findings and run `discharge-review` again. After **two** Readmit rounds, stop with an I-PASS handoff.
5. On **Discharge**: commit the code, then the chart note in its own commit. **Don't push or deploy.** Report to the owner in a few lines: what changed, the key check results, any "Found during treatment" items, and ask whether to push.

## Stop and ask the owner (don't continue) when

- a fact is "pending source" and you can't get it from an allowed source (HANDOFF section 3) in this session,
- precedent (HANDOFF section 4, `.claude/chart/`) doesn't answer a decision only the owner can make,
- a stage hits CLAUDE.md rule 6 (stuck) or rule 7 (case needs splitting — plan the first case only, then ask before continuing).

Otherwise keep going without checking in between stages. Post a one-line status as each stage finishes.
