#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for skill_dir in \
  "${ROOT_DIR}/dream-memory" \
  "${ROOT_DIR}/memory-extractor" \
  "${ROOT_DIR}/verification-gate" \
  "${ROOT_DIR}/swarm-coordinator" \
  "${ROOT_DIR}/structured-context-compressor" \
  "${ROOT_DIR}/kairos-lite" \
  "${ROOT_DIR}/xquik-monitoring"
do
  test -f "${skill_dir}/SKILL.md"
  test -d "${skill_dir}/references"
  test -d "${skill_dir}/scripts"
done

python3 -m py_compile \
  "${ROOT_DIR}/dream-memory/scripts/dream_memory.py" \
  "${ROOT_DIR}/memory-extractor/scripts/memory_manifest.py" \
  "${ROOT_DIR}/verification-gate/scripts/verification_context.py" \
  "${ROOT_DIR}/swarm-coordinator/scripts/task_board.py" \
  "${ROOT_DIR}/structured-context-compressor/scripts/render_template.py" \
  "${ROOT_DIR}/kairos-lite/scripts/job_spec.py" \
  "${ROOT_DIR}/xquik-monitoring/scripts/xquik_monitoring_context.py"

python3 -m unittest discover \
  -s "${ROOT_DIR}/verification-gate/tests" \
  -p "test_*.py"

echo "All skill bundles passed basic checks."
