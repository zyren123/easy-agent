# Implement first foundations module: linear layer

## Goal

Build the first concrete lesson in the curriculum: a linear-layer module that
sets the pattern for future modules in `foundations/` by pairing a torch
implementation with a matching non-framework reference implementation.

## Context

- Parent planning task: `.trellis/tasks/05-11-first-week-trellis-setup/`
- Repository decisions are already frozen around `uv` and module-local docs.
- This is the first implementation slice, so it should stay intentionally small and set a
  strong example for future lessons.

## Requirements

- Fill `foundations/01-linear-layer/README.md` with the actual lesson narrative.
- Implement `foundations/01-linear-layer/linear_layer.py` with both:
  - a torch implementation that later training code can import
  - a non-framework reference implementation that explains the same math
- Implement `foundations/01-linear-layer/linear_layer.ipynb` with the same teaching flow.
- Keep the lesson CPU-friendly and dependency-light beyond torch; do not require GPUs or a training stack.
- Add focused tests for the module implementation, including output parity for a fixed example input.

## Acceptance Criteria

- A learner can understand what a linear layer does from the module README alone.
- The `.py` and `.ipynb` artifacts stay aligned in scope and terminology.
- The same fixed input produces matching outputs from the torch implementation and
  the non-framework reference implementation.
- Lint, type-check, and tests run through `uv` if the toolchain is configured.

## Out of Scope

- Building a full MLP, autograd engine, or optimizer stack
- Covering training loops or agent workflows
