# Publishing Guide

This directory contains the public release bundles for portable `CC`-derived skills.

## Recommended Naming

Recommended GitHub repo name:

- `cc-harness-skills`

Recommended public skill names:

| Slug | Public name |
| --- | --- |
| `dream-memory` | CC Dream Memory |
| `memory-extractor` | CC Memory Extractor |
| `verification-gate` | CC Verification Gate |
| `swarm-coordinator` | CC Swarm Coordinator |
| `structured-context-compressor` | CC Context Compressor |
| `kairos-lite` | CC Kairos Lite |
| `xquik-monitoring` | Xquik Monitoring |

Keep the slugs stable. Put branding in the display name, not the directory name.

## Bundle Layout

```text
<skill-name>/
├── SKILL.md
├── README.md
├── references/
│   ├── prompt-template.md
│   └── source-notes.md
└── scripts/
    └── ...
```

## Release Order

Release in this order:

1. `dream-memory`
2. `memory-extractor`
3. `structured-context-compressor`
4. `verification-gate`
5. `swarm-coordinator`
6. `kairos-lite`

Why this order:

- the first three are the easiest to understand and install
- `verification-gate` is a strong quality/safety story after the memory pair
- `swarm-coordinator` is more advanced and benefits from the earlier context
- `kairos-lite` should come last because proactive behavior needs the most caution

## Release Tag Plan

Use a simple tag line:

- `v0.1.0`: first public batch of all six skills
- `v0.1.x`: README, prompt, and script fixes with no workflow redesign
- `v0.2.0`: material workflow change in one or more skills

Do not create a separate Git tag per skill unless the repo later splits into multiple packages.

## Local Checks

```bash
bash ./skills/check_all.sh
```

## Install Examples

Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -R ./skills/dream-memory ~/.claude/skills/
```

Codex:

```bash
mkdir -p ~/.codex/skills
cp -R ./skills/dream-memory ~/.codex/skills/
```

OpenClaw:

```bash
mkdir -p ~/.openclaw/workspace/skills
cp -R ./skills/dream-memory ~/.openclaw/workspace/skills/
```

## ClawHub Publish

Install the CLI if needed:

```bash
npm i -g clawhub
```

Publish a single skill:

```bash
clawhub publish ./skills/dream-memory \
  --slug dream-memory \
  --name "CC Dream Memory" \
  --version 0.1.0 \
  --tags latest,memory,agent
```

Publish the full batch:

```bash
bash ./skills/publish_all.sh 0.1.0
```

## Related Docs

- Release copy and order: [RELEASE_PLAN.md](/Users/carl/Downloads/codegod/skills/RELEASE_PLAN.md)
- Smoke-test results: [TEST_REPORT.md](/Users/carl/Downloads/codegod/skills/TEST_REPORT.md)
