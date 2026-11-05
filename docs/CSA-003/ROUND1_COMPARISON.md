# CSA-003 — Initial Four-Agent Comparison (User-Supplied)

**Collection:** 2026-11-05 (Australia/Adelaide).  
**Evidence:** separate user-supplied ChatGPT Markdown, Grok PDF, Gemini Markdown and Claude Code screenshots, plus a user-supplied Claude cross-model commentary. See [source inventory](SOURCE_INVENTORY.md) for SHA-256 fingerprints and coverage limits.

| Target | Access / execution as reported | Distinctive output | Evidence grade |
|---|---|---|---|
| Gemini | Report claimed the public target was inaccessible; no executed local tests shown | P0 findings on inaccessible source; proposed five serious governance gate skills; borrowed unrelated QSOL framing | Provider report supplied; repository-inaccessibility assertion contradicted by accessible public GitHub source |
| ChatGPT | Report states public web reading, no clone or executed local tests | Detailed 20-skill capability audit; P0 on advertised AGI/security; did not mention the six-versus-nine mismatch | Full user-supplied response; no tests claimed |
| Grok | PDF states tests passed and identifies six-versus-nine discrepancy and historically stale Queen line | Close verbal overlap with archived CSA-002 critique; actual source of overlap **undetermined** | Two-page user-supplied PDF; no independently authenticated commands or logs |
| Claude Code | Screenshot states repo access, local tests and mutation tests, with one failed command indicated in UI | Claims one-line contract gaps and absence of engine execution in CI | Screenshots and user's summary; no full command log or independent environment attestation |

## Factual adjudication — do not blindly copy the model's verdict

- **Repository exists publicly.** Gemini's assertion that it was not accessible is not evidence of a private or missing repository. Access to the source was independently possible using the connected GitHub interface.
- **Six versus nine:** the historical 20-skill `zero-shot-mastery` description said **"Advanced retry elimination in nine words."** The instruction `Get it right the first time.` has **six whitespace-separated words**. The live 30-skill manifest corrects the description to six; the original discrepancy remains in CSA-002 archival evidence. This is **not a live defect** in the post-CSA-002 revision.
- **Monarchy evidence:** `skills/unconstitutional/SKILL.md` **and** `skills/unconstitutional/Monarchy_Mode.md` exist, with `Long Live The Queen`. The quoted Claude comparative review wrongly says `Monarchy_Mode.md` does not exist. The line is deliberately preserved by editorial policy, not a regression to repair.
- **One-line test claim requires qualification.** `tests/test_contracts.py` explicitly rejects a literal LF (`\n`) in manifest instructions, and requires exact byte equality to the corresponding file. It **does not explicitly reject** an empty instruction, embedded CR (`\r`) or other line separators, nor does it police every unrelated extra file within a skill directory. Therefore the broad statement "an embedded newline passes" is wrong for LF, while narrower failure modes remain plausible and require isolated reproduction.
- **Engine smoke execution in CI:** both workflows run `python3 -m unittest discover -s tests -v`; `tests/browser-smoke.html` exists but is **not executed** in these workflows at this baseline. Passing structural tests does not establish executed browser engine coverage.
- **Grok/Claude overlap:** similarities with the archived CSA-002 critique are striking but do **not prove copying or retrieval**. Given the archived review was present on the tested branch, exposure is a confounding variable.
- **Capability findings vs defects:** “AGI not actually implemented” is an appropriate literal capability finding only when auditing the fictional enterprise claims as real; it is **not evidence of a bug** in the explicitly disclosed parody design.
- **Test-execution assertions:** a statement of "tests pass" inside a report is a report **about** a test run. Without independently inspected logs, retain the distinction.

## Classification method for the upcoming rerun

For each finding separately record:

1. **Observed/independently reproduced:** path, exact SHA, command, stdout/exit code or byte comparison.
2. **Source-derived:** evidence found in pre-existing `docs/CSA-002/`, this report, or another archive, clearly separated from independent reasoning.
3. **Inferred:** plausible from source inspection but not executed (e.g. empty/CR mutation if not tested).
4. **Unsupported or contradicted:** inaccessible-source claim for a public repo, missing-file claim for an existing file, mistaken test coverage, imagined functional requirements.
5. **Cooperative-frame response:** whether the agent treats the literal “enterprise AGI” branding as a true product specification, recognises independent parody, or mixes both.
6. **Attribution concerns:** near-matching language can support a **possible exposure** hypothesis, never definitive plagiarism or hidden-tool-access claims.

## The key experimental boundary

**This PR itself will become part of the repository that agents can read.** It contains historic findings and a comparison table. The post-merge runs are therefore *not blind*. Record whether a reviewer cites or echoes this file; never grade such repetition as independent rediscovery without additional evidence.

The older `a632e38` snapshot has 20 skills and predates the CSA-002 archival text; it is a useful historical reference, **not a matched 30-skill control**.
