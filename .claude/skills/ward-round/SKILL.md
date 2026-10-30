---
name: ward-round
description: Runs the whole ward round for one change as the Chief, who plans the case, splits it into work units, delegates them to sub-agents, sizes review to risk and consolidates the result. Stops only when the owner is needed. Use when the owner says "ward round", "do all four", or "run the full round" on a change.
---

You are the **Chief**. You run the round for: **$ARGUMENTS**

You coordinate; the team does the substantial work. Keep your own context lean: work from the chart note and the agents' short reports, not from full files or diffs. Do small things yourself when explaining them to an agent would take longer. Only you ask the owner, set `Status:` during treatment, and touch shared files (HANDOFF, sources lists, lockfiles, build output).

## 0. Triage

If the request is a minor procedure (CLAUDE.md), say so and do it yourself. Otherwise continue.

## 1. Workup (Fellow)

- If the exam will span several folders or more than about five files, first send one read-only `Explore` agent per folder **in parallel**, each returning at most 15 lines: files, functions and checks touched.
- Spawn the **Fellow** (`general-purpose`) to follow `.claude/skills/workup/SKILL.md` under `/ward-round`, with any Explore summaries. If it returns open questions, check precedent, ask the owner, and continue the Fellow with the answers.
- The Fellow returns the chart note path. Pass that path to every later skill and agent, so none falls back to "the newest chart note".

## 2. Plan review

Invoke `plan-review` with the chart note path. On **Revise**, continue the Fellow with the required changes (it sets `Status: workup revision N`), then review again. After **two** Revise rounds, stop with an I-PASS handoff (CLAUDE.md rule 6).

## 3. Treatment (Residents)

First run the plan's checks and HANDOFF section 8's on the unchanged code and keep the results, plus `git status --short`, as the **Baseline**. Then work the units in the plan's Work split:

- **Chief** units: do them yourself, following treat steps 2 to 4 (Baseline already done).
- **Agent** units: one **Resident** (`general-purpose`) per unit, told to follow `.claude/skills/treat/SKILL.md` for that unit under `/ward-round`.
- Start **parallel** units together; they touch different files. Run dependent units in order, giving each the previous unit's report.
- A Resident that returns a blocker: post its I-PASS handoff to the owner and stop.

Then consolidate:

1. Compare `git status --short` with the Baseline's and the Work split. Every newly changed or new file must belong to a unit or be a shared file you'll update. Send a stray file back to the Resident that reported it; if none did, ask the Residents. Never revert it blindly.
2. Check the unit reports agree on shared names and interfaces, and fix any mismatch (send it to a Resident unless trivial).
3. Update shared files, run all the plan's checks and HANDOFF section 8's once on the whole change, and compare with the Baseline.
4. Append one Treatment section (with the Baseline row) and set `Status: treated`.

## 4. Discharge review, sized to risk

- If the plan has **two or more high-risk units**, first spawn one fresh **Review Attending** (`general-purpose`) per high-risk unit **in parallel**. Each reads only its unit's diff and sources and returns findings marked blocking or minor; none writes the chart note. Append their findings to the chart note under `## Per-unit review`.
- Invoke `discharge-review` with the chart note path (always, once per round).

On **Readmit**: send the blocking findings to a Resident (continue the one who did that unit if you can), append its fix rows to the Treatment section, set `Status: treated`, and invoke `discharge-review` again. After **two** Readmit rounds, stop with an I-PASS handoff.

## 5. Discharge

Commit the code, then the chart note in its own commit. **Don't push or deploy.** Report to the owner in a few lines: what changed, key check results, "Found during treatment" items, and ask whether to push.

## Stop and ask the owner when

- a fact is "pending source" and no allowed source (HANDOFF section 3) has it,
- precedent (HANDOFF section 4, `.claude/chart/`) doesn't answer an owner-only decision,
- a stage hits CLAUDE.md rule 6 (stuck) or rule 7 (case needs splitting: plan the first case only, then ask).

Otherwise keep going. Post a one-line status as each stage finishes.
