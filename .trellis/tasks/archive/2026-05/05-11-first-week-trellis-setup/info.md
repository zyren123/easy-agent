# First-Week Technical Plan

## Scope

This task defines the repository foundation for the first week of a Python-first AI
education project. It locks the layout, conventions, and first implementation slice
without attempting to build the full curriculum.

## In Scope

- Repository skeleton and package layout
- Trellis backend specs for structure, quality, logging, and error handling
- Notebook and module documentation conventions
- Early testing and validation expectations
- A concrete first implementation task for `foundations/01-linear-layer`

## Out of Scope

- Full multi-month curriculum breakdown
- Choosing every future framework or training library
- Building a standalone documentation site
- Adding persistence, APIs, or deployment infrastructure

## Frozen Decisions

- Package manager and workflow: `uv` with `pyproject.toml`
- Reusable code root: `src/ai_edu`
- Top-level curriculum sections: `foundations`, `training`, `agents`
- Module folder naming: numbered kebab-case such as `01-linear-layer`
- Module-local docs: each module owns `README.md`, `lesson.py`, and `lesson.ipynb`
- No separate docs site in week one

## Repository Layout

```text
src/ai_edu/
foundations/
training/
agents/
tests/
.trellis/tasks/
.trellis/spec/backend/
```

## Module Standards

- `README.md` explains the lesson goal, prerequisites, and artifacts.
- `lesson.py` is the source-of-truth walkthrough that can be reviewed and tested.
- `lesson.ipynb` mirrors the lesson interactively for notebook-first execution.
- Reusable helpers move into `src/ai_edu/` as soon as more than one module could use them.

## Quality Strategy

- Prefer standard-library or dependency-light code in the first slice.
- Run lint, type-check, and tests through `uv run ...` once the toolchain is available.
- Add tests for reusable package code, not for every notebook cell.

## Milestone Breakdown

1. Freeze repo conventions and spec documents.
2. Create the package and curriculum skeleton.
3. Implement `foundations/01-linear-layer` as the first content-bearing slice.
4. Use that slice to validate whether shared abstractions in `src/ai_edu/` are sufficient.

## First Implementation Slice

The next task is `.trellis/tasks/05-11-first-linear-layer/`. It should produce the first
CPU-friendly lesson on linear layers with aligned `README.md`, `lesson.py`, and
`lesson.ipynb`, plus minimal reusable support code in `src/ai_edu/foundations/`.
