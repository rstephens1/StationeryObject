#!/usr/bin/env bash
set -euo pipefail
export WRANGLER_HOME="$(cd "$(dirname "$0")" && pwd)/.wrangler-home"
mkdir -p "$WRANGLER_HOME"
npx wrangler "$@"
