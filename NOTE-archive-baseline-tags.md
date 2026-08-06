# Baseline tags from archived `enclosure-concepts`

The public gallery tip lives in **this** repo (`enclosure-concepts-site`).
Git histories are unrelated (site started as a fresh snapshot), so the old
`test/eth-*` tags **cannot** be retagged here as the same objects.

They remain on the archived repo (GitHub Archive keeps tags/history readable):

**Archive:** https://github.com/active-esl/enclosure-concepts  

| Tag | Commit (archive) | Note |
|-----|------------------|------|
| `test/eth-poe-baseline-20260802` | `c684352e2b8751fc20e74862a6d87dd9ad009d78` | PoE highlight on body/pins |
| `test/eth-assemble-baseline-20260802` | `32143d8d6daae1ac793d17b2c3d3a808ff647347` | Pad-contain + slim splash |
| `test/eth-assemble-baseline-20260803` | `32143d8d6daae1ac793d17b2c3d3a808ff647347` | Same tip as 20260802 assemble |
| `test/eth-jack-wall-good-20260803` | `a1d119f5f3625e64d7246ced451c4b07cd600b26` | Jack-wall Inspect matching CAD |

Clone/fetch from the archive if you need those trees:

```bash
git clone --branch test/eth-jack-wall-good-20260803 \
  git@github.com:active-esl/enclosure-concepts.git
```

**Current tip (share):** GitHub Pages — see [README.md](README.md).  
Confirm: `curl -sS https://concepts.active-esl.com/handheld-eth/build.json`


---

## Site baselines (this repo) — 2026-08-06

Alex: gallery + Active POE eth dry-fit tip = really good work.

| Tag | Commit | Pack / note |
|-----|--------|-------------|
| `baseline/gallery-20260806` | *(annotated tag)* | Gallery: WIP hide default, Look-as-default, POE Cycles stills, pack `20260806T154714Z-f1cc705a7b` |
| `test/eth-dryfit-baseline-20260806` | same commit | Published Inspect pack tip (CAD still WIP in worktrees — see detail NOTE) |

Detail: [NOTE-gallery-eth-dryfit-baseline-20260806.md](NOTE-gallery-eth-dryfit-baseline-20260806.md)

**Share:** https://concepts.active-esl.com/

CAD: **no** `enclosures` tag at this freeze — tip owner
`feat/eth-io-bay-hatch` @ `aaad96b` was dirty when baselined.
