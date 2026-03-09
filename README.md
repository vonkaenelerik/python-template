# Python Package Template

Cookiecutter template for Python packages. Generates a project with uv, ruff, mypy, pytest, pre-commit, and Claude Code configuration — ready to go out of the box.

## Prerequisites

- [cookiecutter](https://github.com/cookiecutter/cookiecutter) — `pip install cookiecutter` or `uv tool install cookiecutter`
- [uv](https://docs.astral.sh/uv/) — used for dependency management in generated projects
- [make](https://www.gnu.org/software/make/) (optional) — for Makefile shortcuts

## Usage

From Azure DevOps:

```bash
cookiecutter https://dev.azure.com/ORG/PROJECT/_git/python-template

# or via SSH
cookiecutter git@ssh.dev.azure.com:v3/ORG/PROJECT/python-template
```

From a local clone:

```bash
cookiecutter python-template/
```

Pass `--no-input` to skip prompts and use defaults.

## Template Variables

| Variable | Default | Description |
|---|---|---|
| `project_name` | `My Package` | Human-readable name |
| `project_slug` | *(derived)* | Kebab-case directory/PyPI name (e.g., `my-package`) |
| `package_name` | *(derived)* | Python import name (e.g., `my_package`) |
| `description` | `A short description of the project` | One-line description |
| `author_name` | `Your Name` | For pyproject.toml and LICENSE |
| `author_email` | `you@example.com` | For pyproject.toml |
| `github_username` | `USERNAME` | Used in README badges and repo URLs |

`project_slug` and `package_name` are derived from `project_name` automatically. You can override them if needed.

## What Gets Generated

```
my-package/
├── src/my_package/        # Package source (with py.typed marker)
├── tests/
├── .claude/               # Claude Code commands, hooks, and settings
├── .vscode/               # Workspace settings and recommended extensions
├── Makefile
├── pyproject.toml
├── .pre-commit-config.yaml
├── .gitignore
├── CLAUDE.md
├── README.md
└── LICENSE
```

After generation, the post-gen hook runs automatically:

1. `git init` + initial commit
2. `uv sync` (installs all dependencies)
3. `uv run pre-commit install` (sets up pre-commit hooks)

## Included Tooling

- **ruff** — linting and formatting with an aggressive rule set
- **mypy** — strict mode type checking
- **pytest + pytest-cov** — testing with coverage support
- **pre-commit** — ruff, mypy, and standard file checks on every commit
- **Makefile** — `make check` (lint + typecheck + test), `make test-cov`, `make format`, `make clean`, `make build`
- **VSCode** — format-on-save, inline lint/type errors, pytest integration
- **Claude Code** — slash commands (`/lint`, `/test`, `/review`, etc.), auto-format/lint hooks on file edits

## Contributing

To make changes to this template:

1. Clone the repo and edit files inside `{{cookiecutter.project_slug}}/` — these are Jinja2 templates that get rendered during generation
2. Template variables use `{{ cookiecutter.variable_name }}` syntax
3. To add or change prompted variables, edit `cookiecutter.json`
4. Post-generation setup lives in `hooks/post_gen_project.py`
5. Test locally by running `cookiecutter . --no-input` from the repo root and verifying the output
