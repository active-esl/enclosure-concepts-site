# Active-ESL — enclosure concepts (Pages)

Public GitHub Pages gallery for interactive concept enclosure designs.

**Live site:** https://active-esl.github.io/enclosure-concepts-site/

| Concept | Inspect (3D) |
|---------|----------------|
| Active Slim | https://active-esl.github.io/enclosure-concepts-site/handheld/ |
| Active POE | https://active-esl.github.io/enclosure-concepts-site/handheld-eth/ |
| Active Eink | https://active-esl.github.io/enclosure-concepts-site/eink-imx93/assembly.html |

Status on each page is labelled. Not measured production CAD unless stated.

The previous Pages host at `active-esl/enclosure-concepts` is **retired** (deployment wedged). Use this repo for the public gallery.

**Publish:** push to `main`. Site currently uses **legacy branch Pages** (`main/`) because Actions `build_type=workflow` + `deploy-pages` stays stuck in `deployment_queued` for this org (same failure mode as the old repo). Workflow file `.github/workflows/pages.yml` is kept (disabled) for when workflow Pages works again. `.nojekyll` is present.

After a new model GLB, rebake and copy the beauty still PNG — Still does not auto-update from GLB.
