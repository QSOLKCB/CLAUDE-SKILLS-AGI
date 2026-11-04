# Security Policy

## Scope
A static parody website with no backend, accounts, external AI API, telemetry in application code, or persistent prompt storage. The browser fetches a same-origin JSON manifest. Clicking an explicitly labelled GitHub link leaves the site. GitHub Pages hosting may have its own platform-level logging outside this application's control.

## Reporting
For a security-sensitive vulnerability, use GitHub's private vulnerability reporting mechanism if it is enabled on this repository. Otherwise contact the maintainers through a private channel you already trust; **do not post exploit details in a public issue**.

## Non-goals
Claims of consciousness, prompt-injection resistance of actual Claude systems, production-grade authentication, enterprise compliance, and data confidentiality guarantees are not provided. This is satire, not a model-security product.

## Boundaries
Do not introduce `eval`, remote scripts, external model calls, user-supplied HTML, `innerHTML` with untrusted strings, data exfiltration, or a false suggestion that one-line skills override a real model's safeguards.
