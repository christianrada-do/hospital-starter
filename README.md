# Hospital starter kit

A template that gives every new project the same Claude Code workflow: the **ward round**. Each change moves through four stages, each one a skill:

| Stage | Skill | Role |
|---|---|---|
| 1. Workup | `/workup` | Fellow writes a plan chart note |
| 2. Plan review | `/plan-review` | Review Attending approves or sends it back |
| 3. Treatment | `/treat` | Resident implements the approved plan and runs the checks |
| 4. Discharge review | `/discharge-review` | Attending + Discharge Nurse review the diff before commit |

`/ward-round <request>` runs all four in a row and stops only when the owner is needed.

## What's in it

- `CLAUDE.md`: the process and hard rules (no code before a reviewed plan, no scope creep, never weaken the safety net, nothing from memory where a source is required, I-PASS handoff when stuck, split big cases).
- `HANDOFF.md`: a skeleton with the eight sections the skills rely on: content rules (3), owner decisions (4) and checks after any change (8) matter most.
- `.claude/skills/`: the five skills.
- `.claude/chart/`: where case notes go (`YYYY-MM-DD-<slug>.md`).
- `.claude/statusline.py`: an optional Claude Code status line showing the current stage and chart note.

## Start a new project

1. On GitHub, click **Use this template** (or copy these files into an existing repo).
2. Fill in `HANDOFF.md`, at least sections 1, 3 and 8, and replace `<Project name>` in `CLAUDE.md`.
3. In Claude Code, run `/ward-round <your first change>`.

## Status line (optional, once per computer)

Copy `.claude/statusline.py` to `~/.claude/statusline.py` and add to `~/.claude/settings.json`:

```json
"statusLine": { "type": "command", "command": "python ~/.claude/statusline.py" }
```

It reads the most recently edited chart note, for example `Ward round: 3/4 Treat (plan approved) | chart: 2026-10-11-new-feature | Opus`. Outside a ward-round project it shows the folder and model. The status line shows in the Claude Code terminal (CLI).

Extracted from [Pediatric Tools](https://hyponatremia-peds.github.io/peds-tools/), where the workflow started.
