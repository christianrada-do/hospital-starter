# <Project name>: how Claude works here

Read `HANDOFF.md` first. It holds the content rules (section 3), the owner's past decisions (section 4) and the checks after any change (section 8). Everything below adds a working process on top of it.

## The ward round

Treat each change as a patient moving through four stages. Each stage is a skill; `/ward-round <request>` runs all four in a row and stops only when the owner is needed:

| Stage | Skill | Role | Output |
|---|---|---|---|
| 1. Workup | `/workup` | Fellow | Plan chart note |
| 2. Plan review | `/plan-review` | Review Attending | Approve / revise |
| 3. Treatment | `/treat` | Resident | Code + treatment note |
| 4. Discharge review | `/discharge-review` | Review Attending + Discharge Nurse | Pass / fix list, then commit |

**Skip the round** only for a "minor procedure": a typo, a wording tweak the owner dictated, or a style fix that touches no sourced fact, threshold, calculation, or access/security logic. Say "minor procedure, skipping the round" and go straight to the change and section 8's "All changes" checks. If in doubt, it is not minor.

## Hard rules

1. **No code before a reviewed plan.** `/treat` starts only after `/plan-review` approved the plan in `.claude/chart/`.
2. **No improvising on scope.** Do what the approved plan says. Anything new you notice goes in the chart note under "Found during treatment" and back to the owner; it does not go into this change.
3. **Never weaken the safety net.** No removing or loosening a validation, limit, warning, source citation, or a check in HANDOFF section 8 to make something work. If a check fails, fix the code or escalate.
4. **Nothing from memory where a source is required.** Unchanged from HANDOFF section 3: every fact the project depends on has a named source.
5. **Check precedent before asking the owner.** Search HANDOFF section 4 and earlier chart notes (`.claude/chart/`) first. Only ask if neither answers it, and quote what you found.
6. **Escalate with an I-PASS handoff when stuck** (two failed attempts at the same problem, conflicting sources, or a question only the owner can answer). Stop and post:
   - **I**llness severity: blocked / degraded / cosmetic
   - **P**atient summary: what the change is and where it stands
   - **A**ction list: what was tried, what's left
   - **S**ituation awareness: what could go wrong, what's half-done in the working tree
   - **S**ynthesis: the exact question or decision needed from the owner
7. **Split big cases.** If the plan touches more than about 500 lines or more than one area's core content, split it into separate cases, each with its own chart note, and do them one at a time.

## Chart notes

Each case gets one file: `.claude/chart/YYYY-MM-DD-<slug>.md`. Every stage appends its section (templates are in the skills). Commit the chart note in its own commit after the code commit, so the code diff stays clean. If the project publishes its repo as a website, make sure dot-folders are not published.

When a case settles a question the owner decided, also add one line to HANDOFF section 4 so it becomes precedent.

## Keep it lean

- Skill files stay short. If one grows past about 80 lines, trim it rather than adding exceptions.
- Don't generate backlog: note at most three follow-up ideas per case, under "Found during treatment". The owner picks; Claude doesn't open new cases on its own.
