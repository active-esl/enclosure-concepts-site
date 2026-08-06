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

## Hosting notes

- **Canonical content repo:** this tree (`active-esl/enclosure-concepts-site`).
- **Live host:** GitHub Pages → **`concepts.active-esl.com`** (DNS-only CNAME to `active-esl.github.io`).
- Archive: [`active-esl/enclosure-concepts`](https://github.com/active-esl/enclosure-concepts) (Pages disabled there).
- Cloudflare Workers previously used as a tip host are **retired** — do not share `*.workers.dev`.
- `deploy/cloudflare/` is **obsolete** (kept only as historical reference; do not redeploy).
- `.nojekyll` is present for Pages.
- Local dry-fit: `http://127.0.0.1:8770/` from the tip checkout.

After a new Look GLB, rebake/copy the beauty still PNG — Still does not
auto-update from GLB (see `design-share-3d` skill). Publish by pushing this
repo’s Pages source (`gh-pages` / Actions), not Workers.
