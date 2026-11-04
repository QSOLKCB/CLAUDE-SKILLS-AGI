# Agent Operating Instructions — CLAUDE-SKILLS-AGI

## Mission
Preserve the central satire: the presentation is enterprise-grade, the fake reasoning is deterministically reproducible, and each satirical micro-skill has exactly one non-empty line. Never imply that this project offers genuine AGI, consciousness, working safety overrides, or official Anthropic functionality.

## Hard invariants
1. Skills live at `skills/<id>/SKILL.md`. Each has exactly one non-empty line, with a final LF permitted. Do not add YAML frontmatter.
2. `data/skills.json` must include exactly the same instruction for each ID. The Python standard-library test suite guards this.
3. `assets/engine.js` is a pure, stateless deterministic function of prompt, selected skill, seed, engine version and static manifest. No clock, RNG, external inference, local storage, or network dependency for generating answers.
4. Changes to response rules, text, normalization, or hashing require a version update and an explicit reproducibility note.
5. Render user prompts and model output with DOM `textContent`, never `innerHTML`. Do not use `eval` or execute prompt content.
6. Keep runtime zero-dependency, offline-first and GitHub Pages compatible with relative paths. No Node.js/npm, Docker, hosted APIs, analytics, external fonts or trackers.
7. Preserve the MIT license and conspicuous independent parody disclosures.
8. Use reviewable PRs; no automatic merging or deployment claims without observing the actual result.

## Verification
Run `python3 -m unittest discover -s tests -v`, then load `tests/browser-smoke.html` over local HTTP or GitHub Pages. Record executed tests separately from inferred properties. Never invent benchmarks or AGI performance metrics.

## Tone
Excessively formal corporate engineering language surrounding ridiculously mundane capabilities. The jokes live in the skill text and clearly fictional marketing; the threat model, tests and provenance remain precise.
