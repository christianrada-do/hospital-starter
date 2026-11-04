---
name: claudy-comment-detector
description: Flags Claude-y comments (conversation-bound, over-specific, stale) in AI-written code, READMEs, and docs. Runs inside /discharge-review; use on its own when reviewing code or docs.
---

Adapted from citelao/dotfiles (claudy-comment-detector).

Agents leave comments that help them reason but don't help the next reader: references to earlier turns, generic bug notes, stale specifics. Remove or reword them before commit. The same patterns appear in agent-written READMEs and docs, so the rules apply there too.

Review only comments and doc text added or changed in the diff.

## Flag a comment that

- refers to a conversational turn, a review round, or an approach that was tried and dropped.
- refers generically to a bug or a fix ("fixes the crash") without saying why the code needs to be this way.
- explains standard, idiomatic code, especially as a "correction".
- documents folder structure or file layout. The tree and imports already show it, and it goes stale on the next add, rename, or move.
- lists what the code does not do (stacked "never X, no Y") for things a reader would not assume.
- embeds regenerable specifics. Test: would this sentence survive the next routine update? If not, flag it.
- reassures instead of informing ("trusted", "reviewed", "production-ready").
- uses spec-speak: terms invented in this case or chart note that a reader would have to look up.

## Keep

- Source citations next to sourced facts, thresholds, and calculations (CLAUDE.md requires them). Shorten them if needed; never remove them.
- A comment that explains why the code must be this way, with a specific issue number or link when a bug is the reason.

## Recommend

- Remove the comment if the surrounding code makes it obvious.
- Otherwise one short sentence, one line if possible.
- Remove anything that would not make sense without the diff or the conversation.

For each finding give `file:line`, the rule it breaks, and the exact replacement (or "remove").

## Examples

Conversational turn. Incorrect:
```
// This is the sole guard against untrusted input. The raw input
// detector was removed, so it gets an explicit regression test.
```
Correct: no comment. The removed detector only existed while iterating.

Generic bug. Incorrect:
```
// Zero out the memory to fix bug #123 where the audio system stopped responding after 10 minutes.
```
Correct:
```
// If we do not zero-out memory here, AudioSystem::ProcessAudio will think that we still have an
// external processor, so it will slowly stop responding to pings after about 10min. See #123.
```

Regenerable specifics. Incorrect:
```
The current v2 build contains 507 spoken-equivalence groups (1,167 spellings).
The focused tests cover workspace validation, multiword given names, and surname rejection.
```
Correct:
```
Counts and provenance are recorded in each JSON artifact; see the resolver tests for covered cases.
```
