# Active-ESL — enclosure concepts (Pages)

Public GitHub Pages gallery for interactive concept enclosure designs.

**Live site:** https://active-esl.github.io/enclosure-concepts-site/

| Concept | Look | Inspect |
|---------|------|---------|
| Active Slim | [Look](https://active-esl.github.io/enclosure-concepts-site/handheld/) | [Inspect](https://active-esl.github.io/enclosure-concepts-site/handheld/assembly.html) |
| Active POE | [Look](https://active-esl.github.io/enclosure-concepts-site/handheld-eth/) | [Inspect](https://active-esl.github.io/enclosure-concepts-site/handheld-eth/assembly.html) |
| Active Eink | — | [Inspect](https://active-esl.github.io/enclosure-concepts-site/eink-imx93/assembly.html) |

Status on each page is labelled. Not measured production CAD unless stated.
Audience: Michael / Ollie (and Gary / Adam as needed).

**Canonical Pages host** for Active-ESL enclosure concepts. The previous repo
[`active-esl/enclosure-concepts`](https://github.com/active-esl/enclosure-concepts)
is retained as a read-only archive (content history preserved).

**Publish:** push to `main`. Site uses **legacy branch Pages** (`main` `/`).
Actions workflow `.github/workflows/pages.yml` stays **disabled** — org
`deploy-pages` / `build_type=workflow` was stuck in `deployment_queued`; legacy
`pages-build-deployment` is what serves the live URL. `.nojekyll` is present.

**Fallback CDN** (same `main` tree, if Pages ever wedges again):  
https://cdn.jsdelivr.net/gh/active-esl/enclosure-concepts-site@main/

Local dry-fit review: `http://127.0.0.1:8770/` from the tip checkout
(`/data_drive/esl/enclosure-concepts` or this tree). Pages is for team share.

After a new model GLB, rebake and copy the beauty still PNG — Still does not
auto-update from GLB (see `design-share-3d` skill).
