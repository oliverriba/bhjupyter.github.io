#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/build_notebooks.py"
echo "Build complete. Commit docs/ and push, or serve locally with a static server."
