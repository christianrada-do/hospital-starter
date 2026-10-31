# <Project name>: how Claude works here

Read `HANDOFF.md` first. It holds the content rules (section 3), the owner's past decisions (section 4) and the checks after any change (section 8). Everything below adds a working process on top of it.

## The ward round

Treat each change as a patient moving through four stages. Each stage is a skill; `/ward-round <request>` runs all four in a row as the Chief, delegating to sub-agents (see Delegation below), and stops only when the owner is needed:

| Stage | Skill | Role | Output |
|---|---|---|---|
| 1. Workup | `/workup` | Fellow | Plan chart note |
| 2. Plan review | `/plan-review` (high-risk tier only) | Review Attending | Approve / approve with changes / revise |
| 3. Treatment | `/treat` | Resident | Code + treatment note |
| 4. Discharge review | `/discharge-review` (`/discharge-check` for standard tier) | Review Attending + Discharge Nurse | Pass / fix list, then commit |

## Tiers

The workup sets each case's tier:
- **High-risk:** the change touches a sourced fact, threshold, calculation, or access/security logic. All four stages; `/discharge-review` on the main model.
- **Standard:** everything else (layout, wording, docs, tooling). Short plan, **no plan review**, then `/treat` and `/discharge-check` (the same review on a smaller model).
- If in doubt, high-risk. A plan review answers **Approved**, **Approved with changes** (small exact fixes the Fellow applies without a second review) or **Revise**.

**Skip the round** only for a "minor procedure": a typo, a wording tweak the owner dictated, or a style fix that touches no sourced fact, threshold, calculation, or access/security logic. Say "minor procedure, skipping the round" and go straight to the change and section 8's "All changes" checks. If in doubt, it is not minor.

## Hard rules

1. **No code before an approved plan.** `/treat` starts only after `/plan-review` approved the plan in `.claude/chart/` (high-risk tier), or after the workup wrote it (standard tier).
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
7. **Split big cases.** If the plan touches more than about 500 lines (test files not counted) or more than one area's core content, split it into separate cases, each with its own chart note, and do them one at a time.

## Delegation (under `/ward-round`)

The main session is the **Chief**: it plans, splits the work into units, delegates the substantial ones to sub-agents, sizes review to risk and consolidates (details in the ward-round skill). Sub-agents never ask the owner and never write the chart note, `Status:` or shared files while other agents are working; they return to the Chief. Residents and reviewers on high-risk units run on the main model; read-only searches can use a smaller one. Review and fix repeats only for blocking findings, at most twice (rule 6 after that).

## Chart notes

Each case gets one file: `.claude/chart/YYYY-MM-DD-<slug>.md`. Every stage appends its section (templates are in the skills). Commit the chart note in its own commit after the code commit, so the code diff stays clean. If the project publishes its repo as a website, make sure dot-folders are not published.

When a case settles a question the owner decided, also add one line to HANDOFF section 4 so it becomes precedent.

## Keep it lean

- Skill files stay short. If one grows past about 80 lines, trim it rather than adding exceptions.
- Don't generate backlog: note at most three follow-up ideas per case, under "Found during treatment". The owner picks; Claude doesn't open new cases on its own.
- **One session per case.** After a case is committed, tell the owner to start a new session for the next one. The chart note and HANDOFF carry everything the next case needs; a long session costs more every turn, because each turn re-reads the whole history.
- **Small outputs.** Read files in line ranges, and search before reading a whole file. Trim command output (a test runner's quiet or summary mode) and print only failures.
- **One discharge review per case.** Small, exact fixes outside high-risk content come back as **Discharge with fixes**: apply them, re-run the affected checks, note them in the chart note, and commit without a second review. Only a **Readmit** gets a second review.
- **Text before screenshots.** Check pages with text tools; take a screenshot only for a visual change, or as the final proof for the owner.
