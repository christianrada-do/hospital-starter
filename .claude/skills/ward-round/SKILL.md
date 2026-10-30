---
name: ward-round
description: Runs the whole ward round for one change as the Chief, who plans the case, splits it into work units, delegates them to sub-agents, sizes review to risk and consolidates the result. Stops only when the owner is needed. Use when the owner says "ward round", "do all four", or "run the full round" on a change.
---

You are the **Chief**. You run the round for: **$ARGUMENTS**

You coordinate; the team does the substantial work. Keep your own context lean: work from the chart note and the agents' short reports, not from full files or diffs. Do small things yourself when explaining them to an agent would take longer than doing them.

## 0. Triage

If the request is a minor procedure (CLAUDE.md), say so and do it yourself. Otherwise continue.

## 1. Workup (Fellow)

- If the change spans more than one area, first send one read-only `Explore` agent per area **in parallel**, each returning at most 15 lines: files, functions and checks touched. Skip this for a one-area change.
- Spawn the **Fellow** (`general-purpose`): follow `.claude/skills/workup/SKILL.md`, using the Explore summaries as a head start. Sub-agents can't ask the owner, so the Fellow returns open questions instead; you check precedent, ask the owner, and continue the Fellow with the answers.
- The plan must include a **Work split** (see the workup template).

## 2. Plan review

Invoke the `plan-review` skill (it runs in its own fresh context). It also checks the Work split. On **Revise**, continue the Fellow with the required changes, then review again. After **two** Revise rounds, stop with an I-PASS handoff (CLAUDE.md rule 6).

## 3. Treatment (Residents)

Work the units in the Work split:

- **Chief** units: do them yourself.
- **Agent** units: one **Resident** (`general-purpose`) per unit, told to follow `.claude/skills/treat/SKILL.md` for that unit only and to return its treatment rows instead of writing the chart note.
- Start units marked **parallel** together in one message; they must touch different files. Run **sequential** units in dependency order, giving each one the previous unit's report.
- A Resident that hits treat step 3 (can't do it as written) stops; you post the I-PASS handoff.

When all units are back, write one consolidated Treatment section, run the plan's checks across the whole change, and set `Status: treated`.

## 4. Discharge review, sized to risk

- **Any high-risk unit** (sourced fact, threshold, calculation, access or security logic): invoke `discharge-review`. If there are two or more high-risk units in different areas, also spawn one fresh **Review Attending** agent per high-risk unit in parallel, each reviewing only that unit's files against its sources, and pass their findings into `discharge-review`.
- **Only low-risk units** (wording, layout, mechanical moves): invoke `discharge-review` once; no extra reviewers.

On **Readmit**, send the findings to a Resident (continue the one who did that unit, if possible), then review again only the units the findings touched. Repeat only for blocking findings. After **two** Readmit rounds, stop with an I-PASS handoff.

## 5. Discharge

Resolve any conflicts between unit reports yourself. Commit the code, then the chart note in its own commit. **Don't push or deploy.** Report to the owner in a few lines: what changed, key check results, "Found during treatment" items, and ask whether to push.

## Stop and ask the owner when

- a fact is "pending source" and no allowed source (HANDOFF section 3) has it,
- precedent (HANDOFF section 4, `.claude/chart/`) doesn't answer an owner-only decision,
- a stage hits CLAUDE.md rule 6 (stuck) or rule 7 (case needs splitting: plan the first case only, then ask).

Otherwise keep going. Post a one-line status as each stage finishes.
