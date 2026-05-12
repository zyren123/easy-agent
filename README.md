# AI Education Repository

This repository is the week-one foundation for a Python-first AI education project.
It uses Trellis for planning and execution and `uv` for environment management,
but the teaching structure stays intentionally simple: each module should be
understandable from its own folder.

## Repository shape

```text
foundations/                 Early model-internals curriculum
training/                    Training-pipeline curriculum
agents/                      Agent-systems curriculum
tests/                       Project tests
.trellis/tasks/              Planning and execution artifacts
```

Curriculum modules live in their own numbered folders, for example:

```text
foundations/
  01-linear-layer/
    README.md
    linear_layer.py
    linear_layer.ipynb
```

The intent is straightforward:

- `README.md` explains the concept and intuition
- `linear_layer.py` shows the implementation and can include small
  `if __name__ == "__main__"` checks
- `linear_layer.ipynb` walks beginners through the same ideas interactively

For `foundations/` architecture modules, the `.py` file should usually contain:

- a torch implementation that later training code can import directly
- a small non-framework reference implementation used to explain the math and
  verify the same input produces the same output

Torch is optional in the local environment. The reference path should still run
without it, and parity tests may skip when the dependency is unavailable.

## Week-one decisions

- Package and commands route through `uv` and `pyproject.toml`.
- Curriculum content is organized into `foundations`, `training`, and `agents`.
- No separate docs site is introduced in week one; docs stay inside module folders.
- The first implementation slice is `foundations/01-linear-layer`.
- Architecture modules should prefer torch for the main path and keep a matching
  non-framework reference path for educational comparison.

## Common commands

```bash
uv sync --dev
uv run ruff check .
uv run mypy foundations tests
uv run pytest
```

If tooling is not installed yet, the Trellis task docs under
`.trellis/tasks/05-11-first-week-trellis-setup/` define the expected setup.
