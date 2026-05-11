# Backend Development Guidelines

This repository is a Python-first AI education codebase. These backend specs define the
week-one contracts that keep future curriculum modules aligned with the chosen
repository layout and tooling.

## Overview

The backend layer in this project covers:

- Reusable Python code under `src/ai_edu/`
- Curriculum-facing module code under `foundations/`, `training/`, and `agents/`
- Tests, command-line workflows, and development tooling configured via `pyproject.toml`

## Pre-Development Checklist

Read these files before creating or changing backend code:

1. [Directory Structure](./directory-structure.md)
2. [Quality Guidelines](./quality-guidelines.md)
3. [Error Handling](./error-handling.md)
4. [Logging Guidelines](./logging-guidelines.md)
5. [Database Guidelines](./database-guidelines.md) if the task introduces persistence

## Guidelines Index

| Guide | Description | Status |
|-------|-------------|--------|
| [Directory Structure](./directory-structure.md) | Repository layout, curriculum module shape, naming rules | Active |
| [Database Guidelines](./database-guidelines.md) | Explicit week-one stance on persistence | Deferred until storage exists |
| [Error Handling](./error-handling.md) | Validation, notebook-safe failures, and boundary behavior | Active |
| [Quality Guidelines](./quality-guidelines.md) | Commands, tests, review rules, and forbidden shortcuts | Active |
| [Logging Guidelines](./logging-guidelines.md) | Lightweight logging rules for package code and scripts | Active |

## Quality Check

Reviewers and implementation agents must verify:

1. The repo still follows the `uv + pyproject.toml + src/ai_edu` decision.
2. New curriculum modules use numbered kebab-case folder names and module-local docs.
3. Shared logic is placed in `src/ai_edu/` instead of duplicated across notebooks.
4. Lint, type-check, and tests are run through `uv run ...` when configured.
5. New storage or external-service integrations extend the relevant spec before code lands.

## Design Decisions Frozen In Week One

- Single Python package: `src/ai_edu`
- Top-level curriculum sections: `foundations`, `training`, `agents`
- Module-local documentation instead of a separate docs site
- Numbered kebab-case curriculum module directories
- Educational notebooks must be paired with a `.py` source file, not replace it
