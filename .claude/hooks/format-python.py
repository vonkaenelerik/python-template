#!/usr/bin/env python3
"""PostToolUse hook: Auto-format Python files with ruff after Edit/Write."""

import contextlib
import subprocess
import sys
from pathlib import Path


def format_python(file_path: str) -> None:
    """Auto-format a Python file with ruff."""
    path = Path(file_path)

    if path.suffix != ".py":
        return

    if not path.exists():
        return

    try:
        result = subprocess.run(
            ["uv", "run", "ruff", "format", str(path)],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        if result.returncode != 0:
            print(f"Warning: ruff format failed: {result.stderr}", file=sys.stderr)
    except FileNotFoundError:
        with contextlib.suppress(FileNotFoundError):
            subprocess.run(
                ["ruff", "format", str(path)],
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )
    except subprocess.TimeoutExpired:
        print("Warning: ruff format timed out", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: format-python.py <file_path>", file=sys.stderr)
        sys.exit(1)

    format_python(sys.argv[1])
