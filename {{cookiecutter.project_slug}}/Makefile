.PHONY: install test test-cov lint format typecheck check pre-commit clean build

install:
	uv sync

test:
	uv run pytest

test-cov:
	uv run pytest --cov=src/ --cov-report=term-missing

lint:
	uv run ruff check .

format:
	uv run ruff check --fix . && uv run ruff format .

typecheck:
	uv run mypy src/

check: lint typecheck test

pre-commit:
	uv run pre-commit run --all-files

clean:
	rm -rf .venv .mypy_cache .ruff_cache .pytest_cache dist *.egg-info htmlcov .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +

build:
	uv build
