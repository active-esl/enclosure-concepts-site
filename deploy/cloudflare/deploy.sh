#!/usr/bin/env bash
# Publish tip checkout to Cloudflare Worker enclosure-concepts-site.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
HERE="$(cd "$(dirname "$0")" && pwd)"
export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
# shellcheck disable=SC1091
[[ -s "$NVM_DIR/nvm.sh" ]] && . "$NVM_DIR/nvm.sh"
nvm use 22 >/dev/null
export CLOUDFLARE_API_TOKEN="${CLOUDFLARE_API_TOKEN:-$(~/.cursor-secrets/bin/resolve-secret.sh get CLOUDFLARE_API_TOKEN)}"
export CLOUDFLARE_ACCOUNT_ID="${CLOUDFLARE_ACCOUNT_ID:-51e90cf10e3adee37feb278efd429c74}"

rm -rf "$HERE/public"
mkdir -p "$HERE/public"
rsync -a --delete \
  --exclude '.git' --exclude '.github' --exclude '_site' --exclude 'deploy' \
  --exclude 'README.md' \
  "$ROOT/" "$HERE/public/"

cat > "$HERE/wrangler.toml" <<TOML
name = "enclosure-concepts-site"
main = "src/worker.js"
compatibility_date = "2025-08-01"
workers_dev = true
account_id = "${CLOUDFLARE_ACCOUNT_ID}"

[assets]
directory = "./public"
binding = "ASSETS"
not_found_handling = "404-page"
html_handling = "none"
TOML

cd "$HERE"
npx --yes wrangler@4 deploy
python3 - <<'PY'
import json, urllib.request
u = "https://enclosure-concepts-site.ajlennon.workers.dev/handheld-eth/build.json"
print("live tip:", json.load(urllib.request.urlopen(u))["id"])
PY
