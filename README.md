# AI Education Repository

This repository is the week-one foundation for a Python-first AI education project.
It uses Trellis for planning and execution, `uv` for environment management, and a
single `src/ai_edu` package for reusable code shared by curriculum modules.

## Repository shape

```text
src/ai_edu/                  Reusable Python package code
foundations/                 Early model-internals curriculum
training/                    Training-pipeline curriculum
agents/                      Agent-systems curriculum
tests/                       Project tests
.trellis/tasks/              Planning and execution artifacts
```

Curriculum modules live next to their own `README.md`, `lesson.py`, and `lesson.ipynb`.
Module directories use numbered kebab-case slugs such as
`foundations/01-linear-layer/`.

## Week-one decisions

- Package and commands route through `uv` and `pyproject.toml`.
- Shared reusable code lives in `src/ai_edu/`.
- Curriculum content is organized into `foundations`, `training`, and `agents`.
- No separate docs site is introduced in week one; docs stay inside module folders.
- The first implementation slice is `foundations/01-linear-layer`.

## Common commands

```bash
uv sync --dev
uv run ruff check .
uv run mypy src
uv run pytest
```

If tooling is not installed yet, the Trellis task docs under
`.trellis/tasks/05-11-first-week-trellis-setup/` define the expected setup.
