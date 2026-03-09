Review the current uncommitted changes using a deterministic binary checklist. Every finding maps to a numbered check ID. Only changed/added lines (lines with `+` prefix in the diff) are flagged — never pre-existing code.

## Step 1: Get the Changes

Run `git diff` to see all staged and unstaged changes. If there are no changes, check `git diff HEAD~1` to review the most recent commit.

## Step 2: Read Project Standards

Read `CLAUDE.md` to load the project's code style and conventions before checking.

## Step 3: Binary Checklist Review

For each changed/added line, check against the following numbered checks. A check is either violated or not — no judgment calls.

### Scoping Rules

- **Only flag issues in changed/added lines** (the `+` lines in the diff). Context lines may be read for understanding but never flagged.
- Every finding MUST cite a specific check ID. No freeform observations.

### Severity Definitions

- **CRITICAL** = runtime error, crash, data loss, security vulnerability
- **WARNING** = violates verified project convention, breaks established pattern
- **SUGGESTION** = concrete improvement with measurable criteria

---

### Python Checks (P01–P10)

| ID  | Trigger Condition | Severity |
|-----|-------------------|----------|
| P01 | Public function or method missing type annotations (parameters or return type) | WARNING |
| P02 | Bare `except:` or `except Exception:` without re-raising or logging | CRITICAL |
| P03 | Mutable default argument (`def foo(x=[])` or `def foo(x={})`) | CRITICAL |
| P04 | f-string with no placeholders (should be a regular string) | WARNING |
| P05 | Unused import (not caught by ruff for some reason) | WARNING |
| P06 | Hardcoded secret, credential, API key, or password | CRITICAL |
| P07 | `# type: ignore` without specific error code (e.g., should be `# type: ignore[attr-defined]`) | WARNING |
| P08 | `# noqa` without specific rule code (e.g., should be `# noqa: E501`) | WARNING |
| P09 | `assert` used for runtime validation in production code (non-test files) | WARNING |
| P10 | Overly broad exception type (`except Exception`) where a specific exception is appropriate | SUGGESTION |

### Style Checks (S01–S06)

| ID  | Trigger Condition | Severity |
|-----|-------------------|----------|
| S01 | Function or method body exceeds 50 lines | SUGGESTION |
| S02 | Nesting depth exceeds 4 levels (nested if/for/with/try) | SUGGESTION |
| S03 | Magic number or string literal used more than once in the same function | SUGGESTION |
| S04 | 5+ lines of identical code appearing more than once in the diff | SUGGESTION |
| S05 | Public function or class missing a docstring | SUGGESTION |
| S06 | Naming convention violation: non-snake_case function/variable, non-PascalCase class | WARNING |

### General Checks (G01–G02)

| ID  | Trigger Condition | Severity |
|-----|-------------------|----------|
| G01 | Hardcoded secrets, credentials, API keys, or passwords | CRITICAL |
| G02 | Syntax error or lint error (verified in Step 4) | CRITICAL |

## Step 4: Build Verification

Run `uv run ruff check .` and `uv run mypy src/`. Any errors in changed files are reported as **G02 CRITICAL** findings.

## Step 5: Output

### Format

Files sorted alphabetically. Findings within each file sorted by line number, then severity (CRITICAL > WARNING > SUGGESTION). Suggestions listed in a separate section after main findings.

```
## Review Summary

**Files reviewed**: X
**Issues found**: Y critical, Z warnings

---

### filename.py

**[CRITICAL P02]** Line ~XX: Bare except clause
> [code snippet]
[How to fix]

**[WARNING P01]** Line ~XX: Missing return type annotation
> [code snippet]
[How to fix]

---

## Suggestions

### filename.py

**[SUGGESTION S01]** Line ~XX: Function exceeds 50 lines
> [code snippet]
[Suggested improvement]

---

## Verdict: PASS | PASS WITH WARNINGS | FAIL
```

### Verdict Rules

- **FAIL** — 1 or more CRITICAL findings
- **PASS WITH WARNINGS** — 0 critical, 1 or more WARNING findings
- **PASS** — 0 critical, 0 warnings (suggestions don't affect verdict)
