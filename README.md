# Active-ESL — enclosure concepts (public gallery)

Interactive concept enclosure designs for team review (Michael / Ollie / Gary / Adam).

## Live URLs (share these)

**Canonical public host:** **`https://concepts.active-esl.com/`**  
(GitHub Pages custom domain on this repo. `https://active-esl.github.io/enclosure-concepts-site/` redirects here.)

| | URL |
|--|----------|
| Gallery | https://concepts.active-esl.com/ |
| Active POE Inspect | https://concepts.active-esl.com/handheld-eth/assembly.html |
| Active POE Look | https://concepts.active-esl.com/handheld-eth/ |
| Active Slim Inspect | https://concepts.active-esl.com/handheld/assembly.html |
| Active Eink Inspect | https://concepts.active-esl.com/eink-imx93/assembly.html |

Confirm live tip: `curl -sS https://concepts.active-esl.com/handheld-eth/build.json` → `id` must match the published pack.

**Archived baseline tags** (`test/eth-*`) live only on the old repo history — see [NOTE-archive-baseline-tags.md](NOTE-archive-baseline-tags.md).

**Do not share jsDelivr** for this gallery. jsDelivr serves `.html` as `text/plain` with `X-Content-Type-Options: nosniff`, so browsers show escaped source instead of running Inspect.

Status on each page is labelled. Not measured production CAD unless stated.

**WIP concepts** (currently Active Eink) are hidden from the gallery and top
nav by default. Use **Show projects under development** on the gallery (stored
in `localStorage`) to reveal them with a WIP badge. Deep links to WIP Inspect
URLs still work when someone has the URL.

## Hosting notes

- **Canonical content repo:** this tree (`active-esl/enclosure-concepts-site`).
- **Live host:** GitHub Pages → **`concepts.active-esl.com`** (DNS-only CNAME to `active-esl.github.io`).
- Archive: [`active-esl/enclosure-concepts`](https://github.com/active-esl/enclosure-concepts) (Pages disabled there).
- Cloudflare Workers previously used as a tip host are **retired** — do not share `*.workers.dev`.
- `deploy/cloudflare/` is **obsolete** (kept only as historical reference; do not redeploy).
- `.nojekyll` is present for Pages.
- Local dry-fit: `http://127.0.0.1:8770/` from the tip checkout.
- **Publish path:** GitHub Actions workflow `.github/workflows/pages.yml` on
  `main` only (`build_type: workflow`). Do **not** re-enable legacy
  `gh-pages` branch builds or Cloudflare Workers.
- **2026-08-06 outage:** tip stayed stale because (1) Pages UI CNAME
  create/delete kept firing legacy `pages-build-deployment` that stuck
  `queued`/`building` and poisoned the repo Actions queue (even
  `ubuntu-latest` jobs stopped getting runners; cancels returned HTTP 500/502),
  (2) `deploy-pages` also hit OIDC JWKS rotation
  (`Invalid actions OIDC token due to No keys from key endpoint match the id
  token`). Fix: re-enable Pages as `build_type=workflow`, deploy via aesl
  self-hosted runner (bypass wedged GH-hosted queue), retry deploy-pages on
  OIDC create failure. Do not flip Pages back to legacy/`gh-pages`.


After a new Look GLB, rebake/copy the beauty still PNG — Still does not
auto-update from GLB (see `design-share-3d` skill). Publish by pushing `main`
(Actions), not Workers / not a `gh-pages` branch.
