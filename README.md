# Python Package Template

Copier template for Python packages. Generates a project with uv, ruff, mypy, pytest, pre-commit, and Claude Code configuration — ready to go out of the box.

Generated projects can be updated when the template changes using `copier update --trust`.

## Prerequisites

- [copier](https://github.com/copier-org/copier) — `pip install copier` or `uv tool install copier`
- [uv](https://docs.astral.sh/uv/) — used for dependency management in generated projects
- [make](https://www.gnu.org/software/make/) (optional) — for Makefile shortcuts

## Usage

### Create a new project

From Azure DevOps:

```bash
copier copy --trust https://dev.azure.com/ORG/PROJECT/_git/python-template my-project

# or via SSH
copier copy --trust git@ssh.dev.azure.com:v3/ORG/PROJECT/python-template my-project
```

From a local clone:

```bash
copier copy --trust python-template/ my-project
```

Pass `--defaults` to skip prompts and use default values. The `--trust` flag is required because the template runs a post-generation task (`uv sync`).

After generating, initialize the repo and set up pre-commit hooks:

```bash
cd my-project
git init
uv run pre-commit install
git add .
git commit -m "Initial commit"
```

### Update an existing project

When the template changes, pull updates into a generated project:

```bash
cd my-project
copier update --trust
```

Copier diffs the template between the version you generated from and the current version, then applies the changes. You'll get merge conflicts if you've modified templated files — resolve them like normal git conflicts.

## Template Variables

| Variable | Default | Description |
|---|---|---|
| `project_name` | `My Package` | Human-readable name |
| `project_slug` | *(derived)* | Kebab-case directory/PyPI name (e.g., `my-package`) |
| `package_name` | *(derived)* | Python import name (e.g., `my_package`) |
| `description` | `A short description of the project` | One-line description |
| `author_name` | `Your Name` | For pyproject.toml and LICENSE |
| `author_email` | `you@example.com` | For pyproject.toml |
| `registry_url` | *(empty)* | Package registry URL for publishing (leave empty for PyPI) |

`project_slug` and `package_name` are derived from `project_name` automatically. You can override them if needed.

## What Gets Generated

```
my-project/
├── src/my_package/        # Package source (with py.typed marker)
├── tests/
├── .claude/               # Claude Code commands, hooks, and settings
├── .vscode/               # Workspace settings and recommended extensions
├── Makefile
├── pyproject.toml
├── .pre-commit-config.yaml
├── .gitignore
├── .copier-answers.yml    # Tracks template version for updates
├── CLAUDE.md
├── README.md
└── LICENSE
```

After generation, `uv sync` runs automatically to install all dependencies.

## Included Tooling

- **ruff** — linting and formatting with an aggressive rule set
- **mypy** — strict mode type checking
- **pytest + pytest-cov** — testing with coverage support
- **pre-commit** — ruff, mypy, and standard file checks on every commit
- **Makefile** — `make init`, `make check`, `make test-cov`, `make format`, `make build`, `make publish`, `make clean`
- **VSCode** — format-on-save, inline lint/type errors, pytest integration
- **Claude Code** — slash commands (`/lint`, `/test`, `/review`, etc.), auto-format/lint hooks on file edits

## Contributing

To make changes to this template:

1. Clone the repo and edit files inside `template/` — these are Jinja2 templates rendered during generation
2. Template variables use `{{ variable_name }}` syntax (defined in `copier.yml`)
3. To add or change prompted variables, edit `copier.yml`
4. Post-generation tasks are defined in the `_tasks` section of `copier.yml`
5. Test locally: `copier copy --trust . /tmp/test-project --defaults` and verify the output
6. Tag releases with semver (e.g., `git tag v1.0.0`) — `copier update --trust` uses tags to determine what changed between versions
7. All files in `template/` are rendered through Jinja2 — avoid using `{{ }}` in non-template content (markdown examples, comments, etc.) as it will be interpreted as a template expression
