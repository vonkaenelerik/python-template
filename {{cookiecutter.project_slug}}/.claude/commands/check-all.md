Run all code quality checks in sequence: lint, format, type check, and tests.

```bash
uv run ruff check --fix .
uv run ruff format .
uv run mypy src/
uv run pytest
```
