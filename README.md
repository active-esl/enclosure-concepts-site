# Active-ESL — enclosure concepts (public gallery)

Interactive concept enclosure designs for team review (Michael / Ollie / Gary / Adam).

## Live URLs (share these)

**Latest tip (recommended share — eth Inspect matches today’s dry-fit):**

| | URL |
|--|-----|
| Gallery | https://cdn.jsdelivr.net/gh/active-esl/enclosure-concepts-site@main/index.html |
| Active POE Inspect | https://cdn.jsdelivr.net/gh/active-esl/enclosure-concepts-site@main/handheld-eth/assembly.html |
| Active POE Look | https://cdn.jsdelivr.net/gh/active-esl/enclosure-concepts-site@main/handheld-eth/index.html |
| Active Slim Inspect | https://cdn.jsdelivr.net/gh/active-esl/enclosure-concepts-site@main/handheld/assembly.html |
| Active Eink Inspect | https://cdn.jsdelivr.net/gh/active-esl/enclosure-concepts-site@main/eink-imx93/assembly.html |

Pin a commit if you need an immutable link, e.g.  
`https://cdn.jsdelivr.net/gh/active-esl/enclosure-concepts-site@3e84a65/handheld-eth/assembly.html`

**GitHub Pages** (gallery up; new tip deploys can sit in `deployment_queued`):  
https://active-esl.github.io/enclosure-concepts-site/

| Concept | Pages Look | Pages Inspect |
|---------|------------|---------------|
| Active Slim | [/handheld/](https://active-esl.github.io/enclosure-concepts-site/handheld/) | [assembly](https://active-esl.github.io/enclosure-concepts-site/handheld/assembly.html) |
| Active POE | [/handheld-eth/](https://active-esl.github.io/enclosure-concepts-site/handheld-eth/) | [assembly](https://active-esl.github.io/enclosure-concepts-site/handheld-eth/assembly.html) |
| Active Eink | — | [assembly](https://active-esl.github.io/enclosure-concepts-site/eink-imx93/assembly.html) |

After pushing eth updates, confirm live tip with:
`curl -sS <url>/handheld-eth/build.json` → `id` must match the published pack
(currently tip `20260806T154714Z-f1cc705a7b` on jsDelivr `@main`).

Status on each page is labelled. Not measured production CAD unless stated.

## Hosting notes

- **Canonical content repo:** this tree (`active-esl/enclosure-concepts-site`).
- Archive: [`active-esl/enclosure-concepts`](https://github.com/active-esl/enclosure-concepts) (Pages disabled there).
- Pages source = **legacy branch** (`main` `/`). Workflow
  `.github/workflows/pages.yml` stays **disabled** — Actions
  `build_type=workflow` + `deploy-pages` previously stuck in
  `deployment_queued` for this org. Prefer waiting for a successful
  `pages-build-deployment` before claiming Pages has the new tip.
- `.nojekyll` is present.
- Local dry-fit: `http://127.0.0.1:8770/` from the tip checkout.

After a new Look GLB, rebake/copy the beauty still PNG — Still does not
auto-update from GLB (see `design-share-3d` skill).
