# Baseline — gallery + Active POE eth dry-fit (2026-08-06)

Alex signed this tip as **really good work** (gallery site + Active POE / eth
dry-fit Inspect pack). Durable markers are **git tags + this NOTE**, not chat.

**Share:** https://concepts.active-esl.com/

Confirm live eth pack:

```bash
curl -sS https://concepts.active-esl.com/handheld-eth/build.json
# expect "id": "20260806T154714Z-f1cc705a7b"
```

## Site tags (`enclosure-concepts-site`)

| Tag | Commit | Role |
|-----|--------|------|
| `baseline/gallery-20260806` | see `git rev-list -n1 baseline/gallery-20260806` | Gallery tip |
| `test/eth-dryfit-baseline-20260806` | same commit | Published Inspect pack tip |

Same object intentionally: one tip holds both the public gallery behaviour and
the eth dry-fit pack.

### Included on this tip

- Inspect pack **`20260806T154714Z-f1cc705a7b`** (mount-OFF + hatch; tip owner
  was the io-hatch lane)
- WIP concepts **hidden by default** (`Show projects under development`)
- Gallery cards / mode bar **Look-as-default** (Still secondary)
- Active POE gallery stills restored to **tempered Cycles** lighting
- Pages green tip matching pack id above

### Not claimed by these tags

- **Look-as-default** is in the tagged commits; any later uncommitted gallery
  polish is out of scope unless retagged.
- **CAD shell / SCAD** for the published mesh is **not** fully on committed
  `active-esl/enclosures` history — see below.

## CAD / enclosures — honest status (no CAD tag)

`test/eth-dryfit-baseline-20260806` is a **site pack** baseline. Do **not**
treat nearest `enclosures` `main` as bit-identical to the published GLB.

| Lane / tree | Path | Branch | HEAD (at baseline write) | Working tree |
|-------------|------|--------|--------------------------|--------------|
| Primary | `/data_drive/esl/active-esl-enclosures` | `main` | `aaad96b555b74a4abbc9a1b9077af204805fb166` | dirty (docs/scripts WIP) |
| Tip owner | `/data_drive/esl/active-esl-enclosures-io-hatch` | `feat/eth-io-bay-hatch` | `aaad96b555b74a4abbc9a1b9077af204805fb166` | **dirty** — hatch/SCAD/YAML beyond committed tip |
| wall-mount | `…-wall-mount` | `feat/eth-dual-keyhole-wall-mount` | `aaad96b…` | (sibling lane) |
| lcd-ffc-passage | `…-lcd-ffc-passage` | `feat/lcd-ffc-passage-well-inset` | `aaad96b…` | (sibling lane) |

Committed merge on enclosures `main` at baseline time: **#7** LCD FFC
through-land (`aaad96b`). Published Inspect mesh includes io-hatch tip-owner
work that was **still uncommitted** when this NOTE was written — restore from
the **site pack** / Pages tip, not from tagging dirty CAD.

When CAD catches up and is clean, add a matching
`test/eth-dryfit-baseline-20260806` (or successor) on `active-esl/enclosures`
and link it here.

## Archive repo

Do **not** delete https://github.com/active-esl/enclosure-concepts — older
`test/eth-*` tags remain there. Index:
[NOTE-archive-baseline-tags.md](NOTE-archive-baseline-tags.md).
