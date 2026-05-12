# Align foundations modules with torch plus reference implementation

## Goal

Update the repository conventions so model-architecture modules use PyTorch for
the main implementation while also shipping a non-framework reference
implementation that produces the same outputs for the same inputs.

## What I already know

- The repo now uses self-contained module directories under `foundations/`,
  `training/`, and `agents/`.
- The user wants architecture modules to stay easy to read, not over-engineered.
- The current `01-linear-layer` module is pure Python only, which is not enough
  for later training reuse.

## Requirements

- Update project specs so future agent work follows the torch-plus-reference rule.
- Update the first `linear-layer` module to demonstrate the new pattern.
- Keep the module directory self-contained: one README, one topic `.py`, one
  topic `.ipynb`.
- Ensure the torch implementation and reference implementation produce matching
  outputs for the same example input.

## Acceptance Criteria

- [ ] Spec files state that foundations architecture modules use torch plus a
      matching non-framework reference path.
- [ ] `foundations/01-linear-layer/linear_layer.py` includes both versions.
- [ ] The notebook and README explain why both implementations exist.
- [ ] Tests cover output parity or skip parity checks gracefully when torch is
      unavailable in the environment.

## Out of Scope

- Refactoring all future modules now
- Building a training loop in this task
- Picking a fully pinned torch version strategy
