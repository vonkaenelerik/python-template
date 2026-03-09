# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

This is a Python package (`{{ cookiecutter.project_slug }}`) using a src layout with hatchling as the build backend and uv for dependency management.

## Common Commands

These commands work on any system with uv installed:

- `uv sync` — Install/update all dependencies
- `uv run pytest` — Run tests
- `uv run ruff check .` — Lint code
- `uv run ruff check --fix .` — Fix lint issues
- `uv run ruff format .` — Format code
- `uv run mypy src/` — Type check
- `uv run pre-commit run --all-files` — Run all pre-commit hooks

If `make` is available, you can also use:

- `make install` — Install dependencies
- `make check` — Run lint + typecheck + test
- `make test-cov` — Run tests with coverage report
- `make format` — Auto-fix lint issues and format
- `make clean` — Remove generated files (.venv, caches, etc.)
- `make build` — Build the package

## Project Structure

- `src/{{ cookiecutter.package_name }}/` — Package source code
- `tests/` — Test files

## Code Style

- Ruff for linting and formatting (line length 88, double quotes)
- mypy in strict mode — all functions must have type annotations
- Google-style docstrings
- snake_case for functions/variables, PascalCase for classes

## Testing

- pytest is the test runner
- Test files go in `tests/` directory
- Test functions should have `-> None` return type annotation
