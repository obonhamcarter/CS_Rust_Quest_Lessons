#!/usr/bin/env python3
"""Run notebook generators and keep files/lessons synchronized.

Usage:
  python3 src/sync_notebooks.py
  python3 src/sync_notebooks.py --render
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_step(command: list[str], cwd: Path, label: str) -> None:
    print(f"\n➡️  {label}")
    print(f"   $ {' '.join(command)}")
    subprocess.run(command, cwd=str(cwd), check=True)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate notebooks and sync download copies in files/lessons."
    )
    parser.add_argument(
        "--render",
        action="store_true",
        help="Also run 'quarto render' after syncing notebooks.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    python = sys.executable

    run_step([python, "src/create_notebooks.py"], repo_root, "Generate/sync Rust quests 1-19")

    if args.render:
        run_step(["quarto", "render"], repo_root, "Render site")

    print("\n✅ Notebook sync complete.")
    print("   JupyterLite notebooks: jupyterlite/content/")
    print("   Download notebooks:    files/lessons/")


if __name__ == "__main__":
    main()
