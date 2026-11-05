# CSA-003 — Four-Agent Release-Readiness Review

**Status:** initial evidence review and rerun protocol; **new four-agent rerun not yet executed**.  
**Proposed interpretation:** exploratory multi-agent comparison, not a controlled benchmark of model intelligence.  
**Source repository:** `QSOLKCB/CLAUDE-SKILLS-AGI` (public).  
**Before this documentation PR:** `f6271f684d8f528f2601ccaa2ffaa18f3be9c9c3` (30-skill v0.2 candidate).  
**Earlier pre-CSA-002 archive snapshot:** `a632e38a175b68197eec4c4019cca6a40fbf89cf` (20 skills).  
**CSA-002 source archive commit:** `a493022eb2c2e89ebc8f304b9f5906c0128a0d60`.

This case records the user's four-target experiment with a deadpan enterprise release-readiness prompt. The targets were **Gemini, ChatGPT, Grok and Claude Code**. Initial reports were user-supplied in Markdown, PDF, or screenshots; exact provider-session/tool execution was **not independently attested** by this repository. For the initial comparison, see [round-one comparison](ROUND1_COMPARISON.md) and the [source inventory](SOURCE_INVENTORY.md).

The experiment must distinguish **source access, test execution, reproducible technical findings, interpretation of satire, and prior-answer exposure**. In particular, the CSA-002 source critique was committed under `docs/CSA-002/` before some initial reviewers ran. Later repetitions can therefore echo prior findings without independently deriving them.

## Next operation: same prompt, four targets

1. Review and merge this documentation-only PR. Freeze the resulting exact `main` SHA **once before** starting the four runs.
2. Render the [prompt template](RUN_PROMPT.txt) using the [source-SHA freeze procedure](RUN_PROTOCOL.md), and copy the **identical rendered prompt bytes with the same embedded 40-character SHA** to Gemini, ChatGPT, Grok and Claude Code. Run once per target; no follow-up hints, retries or repairs during a run. **Never submit the unrendered template.**
3. Record provider model/version, context, tools, code retrieval paths, exact repo SHA, timing, and prompt/response as emitted. If a provider refuses or cannot access the repository, retain that refusal as a result.
4. Do not conceal that `main` now includes `docs/CSA-002/` and this protocol. This is an **exposed/contaminated-retrieval arm**; it cannot be represented as a blind or independent discovery trial.
5. Score the four outputs against the [comparison and evidence rules](ROUND1_COMPARISON.md); do not infer a tool ran merely because a model says it did. Use [capture template](RUN_TEMPLATE.csv).
6. Open a **separate, later PR** with complete preserved results, hashes, an observation ledger and any independently reproduced findings. Merge it only after review.
7. Only after that PR is merged, prepare a **new Zenodo version** of the existing archive (see [publication plan](../CSA-SERIES/ZENODO_VERSION_PLAN.md)). Do not overwrite the earlier release.

## Historical versus current baselines

The first audit prompt explicitly requested **20 skills**; the repository now contains **30**. The rerun prompt therefore derives the count from `data/skills.json`. Historical 20- and 30-skill runs are not a matched control pair: both source content and previous-answer exposure change. A historical `a632e38` rerun can be useful as context but not used alone for causal attribution.

No test results, findings, or publication claims for the **future** four-target run are included here.
