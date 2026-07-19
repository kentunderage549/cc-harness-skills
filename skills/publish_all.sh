#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VERSION="${1:-0.1.0}"

publish_skill() {
  local slug="$1"
  local name="$2"
  clawhub publish "${ROOT_DIR}/${slug}" \
    --slug "${slug}" \
    --name "${name}" \
    --version "${VERSION}" \
    --tags latest,agent
}

publish_skill "dream-memory" "CC Dream Memory"
publish_skill "memory-extractor" "CC Memory Extractor"
publish_skill "verification-gate" "CC Verification Gate"
publish_skill "swarm-coordinator" "CC Swarm Coordinator"
publish_skill "structured-context-compressor" "CC Context Compressor"
publish_skill "kairos-lite" "CC Kairos Lite"
publish_skill "xquik-monitoring" "Xquik Monitoring"
