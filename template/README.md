# {{ project_slug }}

{{ description }}.

## Installation

```bash
pip install {{ project_slug }}
```

## Usage

```python
from {{ package_name }} import hello

print(hello("World"))  # Hello, World!
```

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

### Setup

```bash
# Install dependencies
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

If `make` is available:

```bash
make init         # install dependencies and set up pre-commit hooks
```

### Code Quality

| Task | Direct command | Make shortcut |
|---|---|---|
| Run tests | `uv run pytest` | `make test` |
| Run tests with coverage | `uv run pytest --cov=src/ --cov-report=term-missing` | `make test-cov` |
| Lint | `uv run ruff check .` | `make lint` |
| Auto-fix lint + format | `uv run ruff check --fix . && uv run ruff format .` | `make format` |
| Type check | `uv run mypy src/` | `make typecheck` |
| Lint + typecheck + test | Run the above in sequence | `make check` |
| Run all pre-commit hooks | `uv run pre-commit run --all-files` | `make pre-commit` |
| Remove build artifacts | `rm -rf .venv .mypy_cache .ruff_cache .pytest_cache dist *.egg-info htmlcov .coverage` | `make clean` |

### Build & Publish

| Task | Direct command | Make shortcut |
|---|---|---|
| Build the package | `uv build` | `make build` (runs `check` first) |
{%- if registry_url %}
| Publish to registry | `uv publish --index private` | `make publish` (runs `build` first) |
{%- else %}
| Publish to PyPI | `uv publish` | `make publish` (runs `build` first) |
{%- endif %}

#### Publishing to a custom registry

Package registries are configured in `pyproject.toml` using `[[tool.uv.index]]`:

```toml
[[tool.uv.index]]
name = "my-registry"
url = "https://my-registry.example.com/simple/"
publish-url = "https://my-registry.example.com/simple/"
explicit = true
```

Setting `explicit = true` means `uv sync` won't pull packages from this index — it's only used for publishing. Remove `explicit = true` if you also want to install packages from this registry.

Publish to a named index:

```bash
uv publish --index my-registry
{%- if registry_url %}
make publish                     # publishes to "private" (default)
make publish INDEX=my-registry   # publishes to a different index
{%- else %}
make publish INDEX=my-registry
{%- endif %}
```

### VSCode

This project includes workspace settings for VSCode. On first open, install the recommended extensions when prompted (or run `Extensions: Show Recommended Extensions` from the command palette).

**Included extensions:**
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) — Linting and formatting (replaces Pylint, Black, isort)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) — Language support, testing UI, debugging
- [Mypy Type Checker](https://marketplace.visualstudio.com/items?itemName=ms-python.mypy-type-checker) — Inline type error reporting

**What's preconfigured:**
- Format on save with Ruff
- Lint errors shown inline as you type
- Import sorting on save
- mypy strict mode errors shown inline
- pytest integration in the Testing sidebar
- Interpreter set to the `.venv` created by `uv sync`

> **Note:** You must run `uv sync` before opening in VSCode so the `.venv` and all tools are available.

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
