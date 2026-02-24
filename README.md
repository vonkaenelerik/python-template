# my-package

[![CI](https://github.com/USERNAME/my-package/actions/workflows/ci.yml/badge.svg)](https://github.com/USERNAME/my-package/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A short description of the project.

## Installation

```bash
pip install my-package
```

## Usage

```python
from my_package import hello

print(hello("World"))  # Hello, World!
```

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Setup

```bash
git clone https://github.com/USERNAME/my-package.git
cd my-package

# Install dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install

# Run tests
uv run pytest

# Run linting
uv run ruff check .

# Run type checking
uv run mypy src/

# Run all pre-commit hooks
uv run pre-commit run --all-files
```

### Renaming the package

To rename from `my-package` to your own package name:

```bash
python scripts/rename_package.py your-package-name
```

## Claude Code

This project includes [Claude Code](https://docs.anthropic.com/en/docs/claude-code) configuration for AI-assisted development.

Available commands:
- `/lint` — Run ruff linter and formatter
- `/typecheck` — Run mypy type checker
- `/test` — Run pytest
- `/check-all` — Run all checks (lint, typecheck, test)
- `/pre-commit` — Run pre-commit hooks
- `/review` — Code review of current changes
- `/improve-prompt` — Refine a prompt for Claude Code plan mode

## License

MIT
