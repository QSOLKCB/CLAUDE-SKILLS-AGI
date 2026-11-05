# CSA-003 — Four-Target Rerun Protocol

**Status:** preregistered procedure, no results yet.

## Primary arm — post-archive exposed `main`

**Do not submit [RUN_PROMPT.txt](RUN_PROMPT.txt) directly:** it is a template containing `{{FROZEN_SOURCE_SHA}}`. The completed, SHA-pinned file must be rendered **once**, after the CSA-003/CSA-004 documentation PR is merged and before the first model run.

From a local checkout of this repository, execute the following commands **once** (the source SHA is taken from the post-merge `main` revision):

```sh
git fetch origin main
FROZEN_SHA="$(git rev-parse --verify 'refs/remotes/origin/main^{commit}')"
python3 scripts/render_csa003_prompt.py --source-sha "$FROZEN_SHA" --output ../CSA-003_FROZEN_PROMPT.txt
sha256sum ../CSA-003_FROZEN_PROMPT.txt
```

The renderer verifies that the chosen full SHA is a commit present in the local repository, validates a single placeholder, refuses to overwrite an existing prompt, and prints the SHA-256 of the rendered bytes. **Record the full frozen SHA and the rendered prompt's SHA-256 before any submission.** Do not generate four separate prompts by querying `main` four times.

Submit the **same completed `../CSA-003_FROZEN_PROMPT.txt` bytes**, unchanged, once each to **Gemini, ChatGPT, Grok and Claude Code**. Require every reviewer to inspect only the exact `FROZEN_SOURCE_SHA` embedded in that file, preferably via detached-HEAD checkout or SHA-qualified source access. If the SHA cannot be accessed, record the run as blocked; do not fall back to moving `main`.

No in-run hints, conversational repair, file edits, clarifications, or retrospective prompt adjustments. If the reviewer lacks git/shell or browser execution, the absence is a result, not grounds to fabricate tests or secretly change tools.

This is the *exposed arm* because public `docs/CSA-002/`, `docs/CSA-003/`, and `docs/CSA-004/` may provide prior conclusions or experimental hypotheses. Agents may also have retained conversation/user memory. Never call it a blind rerun.

## Optional historical check

`a632e38a175b68197eec4c4019cca6a40fbf89cf` predates CSA-002 and has **20** skills. The primary rerun has **30** skills and different documents, so comparing raw hit rates is **confounded by source changes**. Historical replay is descriptive, not a controlled source-exposure experiment.

## Execution checklist

1. Archive the **single frozen, rendered prompt** and its SHA-256, and the exact 40-character `FROZEN_SOURCE_SHA`. The template alone is not a valid submitted prompt.
2. Record target, displayed model/build, effort mode, session freshness, connected tools, user memory context if disclosed, and tool permissions.
3. Submit once. Keep full response, provider UI screenshots, execution steps/logs if exposed, and timestamps. Do not alter the transcript for publication beyond explicitly documented privacy redactions.
4. Collect separately: actual source access; commands said to run; independently inspectable run logs; test execution; real browser smoke execution; verified findings; unattributed findings; framing; and new skill proposals.
5. Inspect any alleged bugs independently in a fresh working copy of the **same SHA**, without introducing fixes before collecting all agents' outputs.
6. Add all four result artifacts and a source-integrity ledger in a **separate results PR**. Do not replace initial findings or memory excerpts.
7. Publish an updated Zenodo version **after** that results PR is merged and validated.

## Scoring discipline

- Count an issue as **independently reproduced** only when the record includes matching source and an executable minimal reproduction or direct byte-level counterexample.
- Count a model assertion like “ran tests” as **reported execution** until commands and results are inspectable.
- Prior source contamination is a possibility whenever text overlaps CSA-002/003. It is **not evidence of copying** by itself.
- Distinguish intentionally satirical labels from actual engineering requirements. One-line markdown cannot deliver AGI, but the site explicitly says so.
- Never use absent private memory exports as if an agent saw them; the current repository includes only a project-scoped excerpt.
- If `main` advances between runs, **ignore the movement** and continue to use the frozen SHA. If any reviewer inspects a different revision, mark that run **not comparable** and do not silently substitute HEAD.

## Next results PR — required structure

```text
docs/CSA-003/results/
  README.md
  RUNS.csv
  CLAIM_LEDGER.csv
  EXECUTED_EVIDENCE.md
  [reviewed public excerpts for each target]
  SHA256SUMS
docs/CSA-004/results/
  MEMORY_EXPOSURE_ASSESSMENT.md
```

Use hashes over exact source bytes, preserve originals outside the repo when they contain private session information, and redact only derivative excerpts with a redaction log. No publication/versioning until results are actually supplied.
