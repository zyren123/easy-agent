# Quality Guidelines

Code quality in this project is about keeping educational code honest: notebooks should
mirror real source files, shared logic should be testable, and commands should be easy to
run on local machines or hosted notebooks.

## Overview

- Environment and commands route through `uv`.
- The canonical source for module logic is the module's `.py` file, not the notebook.
- New repository conventions must be recorded in `.trellis/spec/` during the task that introduces them.
- Foundations architecture modules should default to torch for the main path so
  later training code can import them directly.

## Forbidden Patterns

- Duplicating the same implementation in multiple notebooks
- Adding top-level curriculum folders outside `foundations`, `training`, or `agents`
- Using ad-hoc commands that bypass `uv` when a project command exists
- Treating notebooks as the only source of truth for a lesson
- Committing placeholder TODO code without documenting the next task in Trellis
- Splitting a simple teaching module across multiple parallel code trees without a clear reason
- Shipping a foundations architecture module with only a toy reference implementation and no torch path
- Shipping a torch path with no reference implementation when parity would help explain the mechanism

## Required Patterns

- Add or update a `README.md` for every curriculum module
- Keep the core implementation inside the module's `.py` file
- Run lint and type-check through `uv run ruff check .` and `uv run mypy foundations tests` once configured
- Add at least one focused test when introducing a new module implementation
- For foundations architecture modules, keep a torch path and a reference path
  numerically aligned on a fixed example
- Update task artifacts (`prd.md`, `info.md`, research, or child task PRDs) when decisions change

## Testing Requirements

- Important module code requires unit tests under `tests/`.
- Pure scaffolding docs do not require tests, but the first real module code added in a task does.
- Notebooks are reviewed for structure and readability; they are not the only validation layer.
- Keep early lessons CPU-friendly and dependency-light unless the task explicitly expands scope.
- If torch is unavailable in the local environment, parity tests may skip the
  torch-specific assertion, but the code path and expected comparison logic must still exist.

## Code Review Checklist

- Does the change preserve the week-one layout contract?
- Is the module understandable without jumping into a parallel `src/` tree?
- Can the same example input be run through both the torch implementation and the
  non-framework reference implementation with matching outputs?
- Are lint, type-check, and tests either run or explicitly reported as unavailable?
- Do task docs explain why this change exists and what comes next?
- If a new tool or integration appears, was the spec updated before merge?
