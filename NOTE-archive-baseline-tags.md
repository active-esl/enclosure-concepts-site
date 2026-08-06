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

**Current tip (share):** Cloudflare Worker — see [README.md](README.md).  
Confirm: `curl -sS https://enclosure-concepts-site.ajlennon.workers.dev/handheld-eth/build.json`
