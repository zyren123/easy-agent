# Quality Guidelines

Code quality in this project is about keeping educational code honest: notebooks should
mirror real source files, shared logic should be testable, and commands should be easy to
run on local machines or hosted notebooks.

## Overview

- Environment and commands route through `uv`.
- The canonical source for reusable logic is `.py` files, not notebooks.
- New repository conventions must be recorded in `.trellis/spec/` during the task that introduces them.

## Forbidden Patterns

- Duplicating the same implementation in multiple notebooks
- Adding top-level curriculum folders outside `foundations`, `training`, or `agents`
- Using ad-hoc commands that bypass `uv` when a project command exists
- Treating notebooks as the only source of truth for a lesson
- Committing placeholder TODO code without documenting the next task in Trellis

## Required Patterns

- Add or update a `README.md` for every curriculum module
- Keep reusable code under `src/ai_edu/`
- Run lint and type-check through `uv run ruff check .` and `uv run mypy src` once configured
- Add at least one focused test when introducing reusable Python code
- Update task artifacts (`prd.md`, `info.md`, research, or child task PRDs) when decisions change

## Testing Requirements

- Package-level helpers in `src/ai_edu/` require unit tests under `tests/`.
- Pure scaffolding docs do not require tests, but the first reusable code added in a task does.
- Notebooks are reviewed for structure and readability; they are not the only validation layer.
- Keep early lessons CPU-friendly and dependency-light unless the task explicitly expands scope.

## Code Review Checklist

- Does the change preserve the week-one layout contract?
- Can a future module reuse the code without copying notebook cells?
- Are lint, type-check, and tests either run or explicitly reported as unavailable?
- Do task docs explain why this change exists and what comes next?
- If a new tool or integration appears, was the spec updated before merge?
