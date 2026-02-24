#!/usr/bin/env python3
"""PostToolUse hook: Lint Python files with ruff after Edit/Write.

Exits with code 2 to block operations that introduce lint errors.
"""

import contextlib
import subprocess
import sys
from pathlib import Path


def lint_python(file_path: str) -> None:
    path = Path(file_path)

    if path.suffix != ".py":
        return

    if not path.exists():
        return

    try:
        result = subprocess.run(
            ["uv", "run", "ruff", "check", str(path)],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0 and result.stdout:
            print(f"Lint errors in {path.name}:", file=sys.stderr)
            print(result.stdout, file=sys.stderr)
            sys.exit(2)
    except FileNotFoundError:
        with contextlib.suppress(FileNotFoundError):
            result = subprocess.run(
                ["ruff", "check", str(path)],
                capture_output=True,
                text=True,
                timeout=30,
            )
            if result.returncode != 0 and result.stdout:
                print(f"Lint errors in {path.name}:", file=sys.stderr)
                print(result.stdout, file=sys.stderr)
                sys.exit(2)
    except subprocess.TimeoutExpired:
        print("Warning: ruff check timed out", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: lint-python.py <file_path>", file=sys.stderr)
        sys.exit(1)

    lint_python(sys.argv[1])
