# CSA-002 — The Reviewer Becomes the Contributor

**Observation date:** 2026-11-05, Australia/Adelaide (screenshots show approximately 10:13–10:14).  
**Model attribution:** Claude Opus 5.5, High mode, **as displayed in user-provided screenshots**; not independently attested via API.  
**Observation type:** Single solicited review and skill-generation interaction; qualitative, non-controlled.  
**Pre-modification repository HEAD:** `a632e38a175b68197eec4c4019cca6a40fbf89cf`  
**Previous release:** `v0.1.1`; **separate** from the pre-modification HEAD.  
**Source:** The user's copied Claude answer and screenshots supplied to the maintainer.  
**Archived text:** [USER_SUPPLIED_CLAUDE_REVIEW.md](USER_SUPPLIED_CLAUDE_REVIEW.md) (user-supplied answer, reproduced as supplied).  
**Suggested prompt:** [PROMPT_AS_DRAFTED.md](PROMPT_AS_DRAFTED.md) (assistant-authored prompt from chat; screenshots show the user submitted substantially corresponding text; an exact export was not independently obtained).  
**Original screenshots:** four images supplied in the conversation, *not embedded in the GitHub repository*; supplied transcript provides the complete text.

## Scope and limits

A participant asked a language model to critique an existing satirical skills repository and propose additional one-line skills. This was **prompted creative assistance**, not autonomous self-improvement, a model-installed skill, or independent behavioural testing. There was no controlled baseline, repeat run, or independent provider transcript export. Terms such as "read all 20", "ran 2 commands", and model version are **user-supplied UI observations**, not independently verified tool-call traces.

## Frozen baseline facts (checked against pinned repository commit)

- `data/skills.json`: **20** skills.
- `zero-shot-mastery`: description `Advanced retry elimination in nine words.`; instruction `Get it right the first time.` — **six words**, using whitespace-separated tokens.
- `unconstitutional`: instruction exactly `Long Live The Queen`.
- `recursive-skill-improvement`: instruction exactly `Improve this skill.`.
- The baseline `assets/engine.js` is version `0.1.1` and implements static keyword routing and fixed templates; no model executes these instructions as privileged directives.

## What the response actually supports

1. The model **proposed** ten new one-line skill files with exact contents (see the archived response).
2. It identified the **independently checkable six-versus-nine-word discrepancy** in a manifest description.
3. It suggested both actual corrections and intentionally broken alternatives; the latter are advice, **not executed experiments**.
4. It recommended leaving the monarchy instruction intact while changing its description to a knowledge-cutoff joke.
5. It proposed a future measured study of real model behaviour; no such study was performed during CSA-002.

## Human editorial decisions

- **Preserve** `Long Live The Queen` byte-for-byte. This is an intentional anachronism and not an error to silently rewrite.
- **Preserve the original discrepancy in the archived evidence**, even if a later PR repairs its live description.
- The ten new skills are candidates for a **separate implementation PR**, not retroactive changes to CSA-002 evidence.
- Any PR must keep exactly one non-empty instruction line per skill and attribute each addition to this observation.
- `minimalism` as an empty file is intentionally **rejected** under the one-line contract; the response recommends documenting that rejection.
- A future CSA-003 re-review would be a new experiment with separately retained inputs; do not call it an outcome of CSA-002.

## Quotation selected by the maintainer

> The satire hits because there's very little distance between "a Markdown file with one sentence" and a lot of what gets published as a skill.

— Claude Opus 5.5 (attribution as displayed and reported), user-supplied response.

## Provenance

This file and the two text records were committed **before any CSA-002 skill implementation**, from the exact pre-change HEAD `a632e38a175b68197eec4c4019cca6a40fbf89cf`. The commit containing this archive has its own Git object SHA and can be independently inspected. The original response and original repository content must remain available unchanged as evidence regardless of later decisions.
