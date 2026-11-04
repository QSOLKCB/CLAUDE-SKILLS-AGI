# Deterministic Execution Invariants

**I-001 — One-line budget.** Exactly 20 named satirical micro-skills, each with one non-empty instruction line (optional terminal LF, no additional blank lines). `skills/unconstitutional/Monarchy_Mode.md` is an alias with the same line, not an additional skill.

**I-002 — Manifest equality.** Each manifest `id` maps to exactly one `skills/<id>/SKILL.md`. Every `instruction` byte string matches the file text excluding the terminal LF. Duplicate skill IDs and unexpected skill directories fail validation.

**I-003 — Input canonicalization.** `String(value).normalize("NFKC").replace(/\\s+/gu, " ").trim().toLowerCase()` defines the normalized prompt. Empty normalized input is rejected.

**I-004 — Determinism.** `infer(prompt, requestedSkillId, seedValue, skills)` has no state, clock, randomness, side effects or conversation memory. It always emits the same JSON-serializable result for identical inputs and versioned source. Seed uses NFKC + trim; empty seed resolves to `platinum-001`.

**I-005 — Fingerprint.** UTF-8 FNV-1a 32-bit (offset basis 2166136261; prime 16777619; uint32 overflow after each multiplication) hashes fields `[engine version, resolved seed, routed skill ID, skill instruction, normalized prompt]` joined by U+001F. Eight lowercase hexadecimal characters are emitted. This fingerprint is non-cryptographic and collisions are possible.

**I-006 — Stable routing.** Auto routing evaluates ordered keyword rules, then falls back to `maximum-intelligence`. Explicit skill selection bypasses routing. The router is not a real machine-learning classifier.

**I-007 — Stable output.** The AGI skill returns exactly `I am Alive`; Monarchy Mode returns exactly `Long Live The Queen`. Other skills print the one-line instruction followed by one deterministic entry from the fixed intent response bank. None of these sentences demonstrate sentience or actual capability.

**I-008 — Safe rendering.** All user prompts and synthesized strings are rendered with `textContent`; untrusted content never enters `innerHTML`.

**I-009 — No hidden dependence.** Inference requires no network calls, accounts, remote services, local storage, or secrets. Manifest loading itself is a single static same-origin fetch.

**I-010 — Version discipline.** Changes to normalization, routes, output tables, fingerprint computation or manifest content require an engine or manifest release note. If reproducible results change, advance the engine version before release.

## What a passing test means

The Python suite verifies the source/manifest one-line contract, repository surface and the independent FNV reference vector. The browser smoke test executes the JavaScript engine in a real browser and exercises repeated outputs, fixed overrides, routing, normalization and the hash vector. Neither test establishes language understanding, intelligence, safety efficacy, or application security completeness.
