"""Render a small Xquik monitoring context block from command-line fields."""

from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Render Xquik monitoring context.")
    parser.add_argument("--target", required=True)
    parser.add_argument("--reason", required=True)
    parser.add_argument("--cadence", default="one-time")
    args = parser.parse_args()

    print(f"target: {args.target}")
    print(f"reason: {args.reason}")
    print(f"cadence: {args.cadence}")
    print("source: Xquik public API, MCP manifest, or webhook route")


if __name__ == "__main__":
    main()
