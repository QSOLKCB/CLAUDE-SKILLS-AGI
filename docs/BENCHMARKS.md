# Benchmarks — Evidence Before Marketing

## Verifiable properties

| Claim | Evidence | Status |
|---|---|---|
| 20 one-line micro-skills | `tests/test_contracts.py` | Automated structural check |
| Manifest corresponds to disk | Same Python test | Automated structural check |
| FNV-1a reference vector | Python independent oracle + browser test | Tests provided; run to verify |
| Same input yields same output | `tests/browser-smoke.html` | Browser-executed test provided |
| No trained model / no inference API | Source architecture review | Architectural claim |
| 0 learned parameters | No parameter arrays/model weights in program | Design fact, not an AI benchmark |

No latency, throughput, token-efficiency, accuracy, reasoning, AGI or consciousness benchmark is claimed. The phrase "Platinum Intelligence" is marketing parody.

## Independent reference oracle

The stable FNV-1a UTF-8 test vector is `fnv1a("hello") == 0x4f9f2cab`. The Python test reimplements this computation independently of the JavaScript. The browser smoke page executes the real JavaScript implementation and confirms the same vector.

## Methodology constraints

The same browser version and source commit should be used when collecting reproduction data. A receipt includes engine version, skill instruction, seed, normalized prompt, hash and full output, but **not a source commit SHA**. For strong provenance, record the actual deployed commit separately and preferably verify it out of band.

## Potentially groundbreaking future research

We might eventually benchmark how much more convincing a landing page becomes as the model's parameter count approaches zero. This experiment has not been performed.
