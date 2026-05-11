# Implement first foundations module: linear layer

## Goal

Build the first concrete lesson in the curriculum: a CPU-friendly linear-layer module that
sets the pattern for future modules in `foundations/`.

## Context

- Parent planning task: `.trellis/tasks/05-11-first-week-trellis-setup/`
- Repository decisions are already frozen around `uv`, `src/ai_edu`, and module-local docs.
- This is the first implementation slice, so it should stay intentionally small and set a
  strong example for future lessons.

## Requirements

- Fill `foundations/01-linear-layer/README.md` with the actual lesson narrative.
- Implement `foundations/01-linear-layer/lesson.py` as a readable walkthrough.
- Implement `foundations/01-linear-layer/lesson.ipynb` with the same teaching flow.
- Add reusable support code to `src/ai_edu/foundations/` only if it removes duplication.
- Keep the lesson CPU-friendly and dependency-light; do not require GPUs or a training stack.
- Add focused tests for any reusable package code introduced.

## Acceptance Criteria

- A learner can understand what a linear layer does from the module README alone.
- The `.py` and `.ipynb` artifacts stay aligned in scope and terminology.
- Reusable code lives in `src/ai_edu/` rather than being copied between files.
- Lint, type-check, and tests run through `uv` if the toolchain is configured.

## Out of Scope

- Building a full MLP, autograd engine, or optimizer stack
- Introducing PyTorch as a hard dependency
- Covering training loops or agent workflows
