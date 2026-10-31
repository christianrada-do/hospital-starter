---
name: discharge-check
description: Stage 4 of the ward round for standard-tier cases (no sourced fact, threshold, calculation, or access/security change). The same review as discharge-review, on a smaller model. Use after /treat on a standard-tier case.
context: fork
background: false
model: sonnet
---

Read `.claude/skills/discharge-review/SKILL.md` and follow it exactly, with these arguments: $ARGUMENTS

First confirm the chart note says `Tier: standard` and the diff changes no sourced fact, threshold, calculation, or access/security logic. If it does, stop: set `Status: readmit` with the finding "high-risk change in a standard-tier case: run /discharge-review".
