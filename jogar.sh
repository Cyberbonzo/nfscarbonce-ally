#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec 9>"${XDG_RUNTIME_DIR:-/run/user/$(id -u)}/nfscarbonce-ally.lock"
flock -n 9 || exit 0
exec python3 "$ROOT/source/run.py" "$@"
