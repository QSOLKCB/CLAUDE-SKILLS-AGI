# CSA-003 — Claude Comparative Commentary (User-Pasted Excerpts)

The following quotations are transcribed from text supplied by the user and attributed to Claude Opus 5.5. They are **not independently authenticated provider exports** and are not independent evidence of the underlying tool invocations.

> Gemini didn't count, ChatGPT reviewed the jokes seriously, Grok may have copied the answer, and Claude Code found real bugs that weren't in the answer key.

> The contract test doesn't enforce one line.

> CI never runs the engine.

> The stale monarch is now a CI-enforced invariant.

> For a clean rerun, pin the agents to `a632e38`, the last commit before the archive landed. Otherwise every future reviewer gets the answer key in `docs/`, and the contamination itself is a decent CSA-003.

## Correction ledger

- **Overstated:** The comparison stated Grok cited a `Monarchy_Mode.md` file that did not exist. **Correction:** `skills/unconstitutional/Monarchy_Mode.md` does exist and contains `Long Live The Queen`. Checked on the actual repository.
- **Overstated:** An arbitrary embedded LF in a manifest instruction would pass the current test. **Correction:** literal `\n` is explicitly banned in the manifest. Embedded CR, non-LF separators, and empty instructions are not equivalently rejected by that check.
- **Unproven:** Linguistic similarities in Grok's output prove it copied the CSA-002 review. **Correction:** possible source exposure and overlap, no proof of retrieval/copying.
- **Supported source-level observation:** current CI workflows invoke the Python unit suite but have no browser-executed engine test step.
- **Time-dependent:** the nine-word description was present at the original twenty-skill baseline and corrected in the thirty-skill implementation. Avoid calling it an outstanding defect on current `main`.

All original user-supplied statements remain represented as originally made in the private source material; these corrections are **adjacent annotations**, not edits to the historical report.
