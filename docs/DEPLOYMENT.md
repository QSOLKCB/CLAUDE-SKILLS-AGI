# GitHub Pages deployment

## Diagnosis (2026-11-05)

The merge commit 653286c390aedcde38bf750c5fb4f2cccc7b67f7 passed the verification workflow, but the repository contained no Pages deployment workflow. A successful test run does not publish the website. Repository metadata reported has_pages=true, but the actual Pages source setting could not be read.

## Required one-time configuration

Repository **Settings → Pages → Build and deployment → Source → GitHub Actions**.

This requires an administrator. Do not select the generic Jekyll template; this repository already contains its own Pages workflow. The workflow does not automatically change this setting.

## Publishing workflow

The file .github/workflows/pages.yml runs on pushes to main, on pull requests, and by manual workflow_dispatch.

- Pull requests run the structural checks and assemble a site in _site, but do not upload or deploy.
- Pushes to main run the same checks, upload a curated Pages artifact and deploy to the github-pages environment.
- Manual reruns from main do the same if an earlier deployment failed after the Pages settings were changed.
- Deployment requires pages:write and id-token:write, granted only to the deployment job.
- GitHub Actions dependencies are pinned to exact commits; no runtime package manager or static site generator is needed.

The artifact contains only index.html, .nojekyll, assets/app.js, assets/engine.js, assets/style.css, assets/favicon.svg, data/skills.json and tests/browser-smoke.html.

## Verification procedure

1. Review and merge the publishing workflow PR after CI passes.
2. Confirm Settings → Pages → Source is GitHub Actions.
3. Open Actions → Publish Platinum Intelligence Lab and inspect the most recent main run. Require the package AND deploy jobs to succeed.
4. Use the deployment URL reported by the github-pages environment; then check https://qsolkcb.github.io/CLAUDE-SKILLS-AGI/.
5. Run the JavaScript smoke page at /CLAUDE-SKILLS-AGI/tests/browser-smoke.html.
6. If the source setting was enabled after the workflow ran, manually dispatch Publish Platinum Intelligence Lab from the main branch.

## Troubleshooting

- Only Verify platinum micro-skills is visible: the publishing workflow is not on main or did not trigger.
- Package green, deploy fails: inspect Pages source setting and deployment permissions.
- 404 after successful merge: a merge is not evidence of Pages publication; inspect the Pages environment outcome.
- Shell loads but chat fails: inspect network requests for same-origin data/skills.json and JS modules.

This workflow fixes the missing publication mechanism. It does not establish that a successful Pages deployment has occurred until the deployment run has been observed.
