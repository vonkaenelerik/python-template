#!/usr/bin/env python3
"""Rename my-package to a custom package name.

Usage:
    python scripts/rename_package.py <new-name>
    python scripts/rename_package.py <new-name> --dry-run

The new name should be in kebab-case (e.g., my-cool-lib).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

OLD_NAME = "my-package"
OLD_IMPORT_NAME = "my_package"

ROOT = Path(__file__).resolve().parent.parent

FILES_TO_UPDATE = [
    "pyproject.toml",
    "src/my_package/__init__.py",
    "tests/test_example.py",
    "README.md",
    "LICENSE",
    "CLAUDE.md",
    ".github/workflows/ci.yml",
    ".pre-commit-config.yaml",
    "azure-pipelines.yml",
]

COMMAND_DIR = ".claude/commands"


def validate_name(name: str) -> None:
    """Validate the package name is valid kebab-case."""
    if not re.match(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$", name):
        print(
            f"Error: '{name}' is not a valid package name.\n"
            "Use lowercase kebab-case (e.g., my-cool-lib).",
            file=sys.stderr,
        )
        sys.exit(1)

    if len(name) < 2:
        print("Error: Package name must be at least 2 characters.", file=sys.stderr)
        sys.exit(1)

    if name == OLD_NAME:
        print(f"Error: Package is already named '{OLD_NAME}'.", file=sys.stderr)
        sys.exit(1)


def derive_import_name(name: str) -> str:
    """Convert kebab-case to snake_case."""
    return name.replace("-", "_")


def replace_in_file(
    path: Path,
    old_name: str,
    new_name: str,
    old_import: str,
    new_import: str,
    *,
    dry_run: bool,
) -> bool:
    """Replace all occurrences in a file. Returns True if changes were made."""
    if not path.exists():
        return False

    content = path.read_text(encoding="utf-8")
    new_content = content.replace(old_name, new_name).replace(old_import, new_import)

    if content == new_content:
        return False

    if dry_run:
        print(f"  Would update: {path.relative_to(ROOT)}")
    else:
        path.write_text(new_content, encoding="utf-8")
        print(f"  Updated: {path.relative_to(ROOT)}")

    return True


def rename_directory(old: Path, new: Path, *, dry_run: bool) -> bool:
    """Rename a directory. Returns True if rename was performed."""
    if not old.exists():
        return False

    if new.exists():
        print(
            f"Error: Target directory already exists: {new.relative_to(ROOT)}",
            file=sys.stderr,
        )
        sys.exit(1)

    if dry_run:
        print(f"  Would rename: {old.relative_to(ROOT)} -> {new.relative_to(ROOT)}")
    else:
        old.rename(new)
        print(f"  Renamed: {old.relative_to(ROOT)} -> {new.relative_to(ROOT)}")

    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rename my-package to a custom package name."
    )
    parser.add_argument(
        "name",
        help="New package name in kebab-case (e.g., my-cool-lib)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without making modifications",
    )
    args = parser.parse_args()

    new_name: str = args.name
    dry_run: bool = args.dry_run

    validate_name(new_name)
    new_import = derive_import_name(new_name)

    # Check we're in the right directory
    if not (ROOT / "pyproject.toml").exists():
        print(
            "Error: pyproject.toml not found. "
            "Are you running from the repository root?",
            file=sys.stderr,
        )
        sys.exit(1)

    if dry_run:
        print(f"Dry run: renaming '{OLD_NAME}' -> '{new_name}'")
        print(f"         import: '{OLD_IMPORT_NAME}' -> '{new_import}'")
        print()
    else:
        print(f"Renaming '{OLD_NAME}' -> '{new_name}'")
        print(f"         import: '{OLD_IMPORT_NAME}' -> '{new_import}'")
        print()

    modified = 0

    # Phase 1: Text replacements in known files
    print("Updating file contents:")
    for rel_path in FILES_TO_UPDATE:
        path = ROOT / rel_path
        if replace_in_file(
            path, OLD_NAME, new_name, OLD_IMPORT_NAME, new_import, dry_run=dry_run
        ):
            modified += 1

    # Phase 2: Update .claude/commands/ files
    commands_dir = ROOT / COMMAND_DIR
    if commands_dir.exists():
        for cmd_file in sorted(commands_dir.glob("*.md")):
            if replace_in_file(
                cmd_file,
                OLD_NAME,
                new_name,
                OLD_IMPORT_NAME,
                new_import,
                dry_run=dry_run,
            ):
                modified += 1

    # Phase 3: Rename source directory
    print("\nRenaming directories:")
    old_src = ROOT / "src" / OLD_IMPORT_NAME
    new_src = ROOT / "src" / new_import
    if rename_directory(old_src, new_src, dry_run=dry_run):
        modified += 1

    # Summary
    print(f"\n{'Would modify' if dry_run else 'Modified'}: {modified} items")

    if not dry_run:
        print("\nDone! Next steps:")
        print("  uv sync")
        print("  uv run pre-commit install")


if __name__ == "__main__":
    main()
