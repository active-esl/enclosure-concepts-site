# Active-ESL — enclosure concepts (public gallery)

Interactive concept enclosure designs for team review (Michael / Ollie / Gary / Adam).

## Live URLs (share these)

**Canonical public host (Cloudflare Worker — current tip):**

Intended share host: **`https://concepts.active-esl.com/`** (AESL CF custom domain — pending Workers token rotate on the AESL account).  
**Live now:** `https://enclosure-concepts-site.ajlennon.workers.dev/`

| | Live now | Intended |
|--|----------|----------|
| Gallery | https://enclosure-concepts-site.ajlennon.workers.dev/ | https://concepts.active-esl.com/ |
| Active POE Inspect | https://enclosure-concepts-site.ajlennon.workers.dev/handheld-eth/assembly.html | https://concepts.active-esl.com/handheld-eth/assembly.html |
| Active POE Look | https://enclosure-concepts-site.ajlennon.workers.dev/handheld-eth/ | https://concepts.active-esl.com/handheld-eth/ |
| Active Slim Inspect | https://enclosure-concepts-site.ajlennon.workers.dev/handheld/assembly.html | https://concepts.active-esl.com/handheld/assembly.html |
| Active Eink Inspect | https://enclosure-concepts-site.ajlennon.workers.dev/eink-imx93/assembly.html | https://concepts.active-esl.com/eink-imx93/assembly.html |

Confirm live tip: `curl -sS https://enclosure-concepts-site.ajlennon.workers.dev/handheld-eth/build.json` → `id` must match the published pack (currently `20260806T154714Z-f1cc705a7b`).

**Archived baseline tags** (`test/eth-*`) live only on the old repo history — see [NOTE-archive-baseline-tags.md](NOTE-archive-baseline-tags.md).

**Do not share jsDelivr** for this gallery. jsDelivr serves `.html` as `text/plain` with `X-Content-Type-Options: nosniff`, so browsers show escaped source instead of running Inspect.

**GitHub Pages** (org deploy queue still wedged — may lag tip; not the share path until tip matches):  
https://active-esl.github.io/enclosure-concepts-site/

Status on each page is labelled. Not measured production CAD unless stated.

## Hosting notes

- **Canonical content repo:** this tree (`active-esl/enclosure-concepts-site`).
- **Live host:** Cloudflare Worker `enclosure-concepts-site` → `*.workers.dev` (see `deploy/cloudflare/`).
- Archive: [`active-esl/enclosure-concepts`](https://github.com/active-esl/enclosure-concepts) (Pages disabled there).
- GitHub Pages: `build_type` / `gh-pages` branch / Actions `ubuntu-latest` tried 2026-08-06; org still leaves `pages-build-deployment` / `deploy-pages` in `errored` / forever-`queued`. Prefer CF until Pages tip == pack `id`.
- `.nojekyll` is present for Pages.
- Local dry-fit: `http://127.0.0.1:8770/` from the tip checkout.

After a new Look GLB, rebake/copy the beauty still PNG — Still does not
auto-update from GLB (see `design-share-3d` skill). Redeploy CF after tip push:
`deploy/cloudflare/deploy.sh`.
