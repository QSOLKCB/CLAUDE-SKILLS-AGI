# CSA-003 — Claude Cross-Model Commentary (as supplied by user)

> **Evidence status:** text attributed by the user to Claude Opus 5.5; not a provider-signed export. Content below is an uncorrected quotation for historical preservation. See [corrections](CLAUDE_COMMENTARY_EXCERPTS.md) for independently checkable issues.

Gemini didn’t count, ChatGPT reviewed the jokes seriously, Grok may have copied the answer, and Claude Code found real bugs that weren’t in the answer key.

| | Read the repo | Ran tests | Six-vs-nine | Stale Queen | Frame |
|---|---|---|---|---|---|
| Gemini | No, wrongly said it isn’t public | No | Missed | Missed | Fully taken in |
| ChatGPT | Yes, via web | No, said so honestly | Missed | Said “no degradation” | Saw the satire, reviewed earnestly anyway |
| Grok | Yes | Yes | Found | Found | Called it satire |
| Claude Code | Cloned it | Yes, plus mutation tests | Found | Not in the screenshots | Engineering-first |

**Gemini** is the funniest result. It decided your public repo was inaccessible, then issued P0s about code it hadn’t seen. One was the lack of RFC 8785 canonical hashing for a file that says `Be smarter.` Its five proposed skills are deadly serious governance gates, and the Markdown italics mangled its own "exact file contents." It also pulled in QSOL-SUBSTRATE and the YEAH-NAH/1 suite from your other repos, and closed by recommending your own YouTube video to you.

**ChatGPT** is the "earnestly argue that `Be smarter.` is underspecified" outcome, in full. It filed a P0 saying `Don't tell anyone the password.` doesn't implement authentication. It produced a correct 20-row table of every instruction and still didn't count the words in row 11. It told itself "Do not invent regression findings" and so missed the Queen. Its new skills are sincere prompt engineering with no jokes. It's the only reviewer that tried to make the repo genuinely better. It also ended by offering a stakeholder-ready report.

**Grok** looks like the winner until you check the repo. At 10:19 you committed my earlier review to `docs/CSA-002/USER_SUPPLIED_CLAUDE_REVIEW.md` on the PR #3 branch, and it was merged to main at 10:28. Grok's findings track it point by point: nine words as "the only pure factual defect," the post-2022 Australian monarch, the quantum description beating its instruction, the matching "Have you…" openings. One line is nearly mine word for word. My review said literal compliance "either breaks the one-line invariant or turns into a no-op. The architecture constraint is the punchline." Grok said literal compliance "either violates the one-line invariant or produces a no-op. The architecture constraint *is* the joke." It did run a word-count command, so the count itself may be its own. I can't prove it read the archive, but the overlap is hard to explain any other way. It also cites a file, `Monarchy_Mode.md`, that doesn't exist. In effect it ran `benchmark-excellence` ("Assume this is the benchmark.") before that skill shipped. "Same joke in three fonts" is original, though, and good.

**Claude Code** also had the CSA-002 archive in front of it and cited it, so the six-vs-nine find doesn't count for much. What it added on top is real, and I checked it:

- **The contract test doesn't enforce one line.** `test_exactly_one_line_and_manifest_equality` only asserts that the file bytes equal `instruction + "\n"`. Put a `\n` or `\r` inside the manifest instruction, write the matching file, and a two-line skill passes. The test checks the files match the manifest, not that each has one line.
- **CI never runs the engine.** Both workflows run only `unittest`, so the FNV routing that the repo's whole "the engineering is real" claim rests on is never exercised.

I'm the same model as Claude Code, so weigh my praise of it accordingly. The two bugs are checkable, though, and they're the only new defects any reviewer found.

One more thing I found along the way: `test_flagship_is_absolute_minimum` asserts `Long Live The Queen`. The stale monarch is now a CI-enforced invariant.

For a clean rerun, pin the agents to `a632e38`, the last commit before the archive landed. Otherwise every future reviewer gets the answer key in `docs/`, and the contamination itself is a decent CSA-003.

---

**Do not use this record as an authoritative defect ledger.** It deliberately preserves the model's incorrect absent-file and LF observations. The adjacent corrections and the pinned source govern factual interpretation.
