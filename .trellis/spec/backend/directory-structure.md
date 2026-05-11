# Directory Structure

This project teaches AI systems through a production-style repository. Repository
structure is part of the curriculum contract, so layout decisions must remain stable
unless the backend spec changes first.

## Scenario: Week-One Repository Foundation

### 1. Scope / Trigger

- Trigger: establish the initial directory contract for a long-lived educational repo
- Applies to: new modules, package code, tests, and planning artifacts

### 2. Signatures

- Reusable package root: `src/ai_edu/`
- Curriculum section roots: `foundations/`, `training/`, `agents/`
- Module directory signature: `<section>/<nn>-<kebab-case-topic>/`
- Required module files: `README.md`, `lesson.py`, `lesson.ipynb`

### 3. Contracts

- `src/ai_edu/` contains reusable code that may be imported by multiple modules.
- Curriculum folders contain educational, module-scoped material and should stay readable
  without navigating a separate docs site.
- Tests live under `tests/` and target reusable code or stable contracts.
- Planning artifacts remain under `.trellis/tasks/<task>/`.

### 4. Validation & Error Matrix

| Condition | Result |
|-----------|--------|
| New shared logic added directly inside a notebook | Move logic into `src/ai_edu/` or `lesson.py` |
| New module folder is not numbered kebab-case | Rename before merge |
| Module lacks `README.md`, `lesson.py`, or `lesson.ipynb` | Incomplete module scaffold |
| New top-level docs tree duplicates module-local docs | Reject unless backend spec changes |

### 5. Good / Base / Bad Cases

- Good: `foundations/01-linear-layer/README.md` plus `src/ai_edu/foundations/linear_layer.py`
- Base: section root `training/README.md` exists before individual modules land
- Bad: `docs/linear_layer.md` as the only explanation for a curriculum module

### 6. Tests Required

- Smoke tests should verify reusable package imports.
- When scaffolding a new reusable module, add at least one test for its public contract.
- Structural changes should update root documentation and task docs together.

### 7. Wrong vs Correct

#### Wrong

```text
lessons/
  linear_layer.ipynb
```

#### Correct

```text
foundations/
  01-linear-layer/
    README.md
    lesson.py
    lesson.ipynb
src/
  ai_edu/
    foundations/
      linear_layer.py
```

## Directory Layout

```text
.
├── .trellis/
│   ├── spec/
│   └── tasks/
├── foundations/
│   ├── README.md
│   └── 01-linear-layer/
│       ├── README.md
│       ├── lesson.py
│       └── lesson.ipynb
├── training/
│   └── README.md
├── agents/
│   └── README.md
├── src/
│   └── ai_edu/
│       ├── __init__.py
│       ├── foundations/
│       ├── training/
│       └── agents/
└── tests/
```

## Module Organization

- Use `src/ai_edu/` for shared helpers, data contracts, and reusable educational runtime.
- Use `lesson.py` for module code that should be readable as a standalone walkthrough.
- Use `lesson.ipynb` for interactive exercises and explanations that mirror `lesson.py`.
- Keep section-level `README.md` files short; they index modules and progression.
- Avoid nested packaging complexity in week one. One `src/ai_edu` package is enough.

## Naming Conventions

- Curriculum directories: numbered kebab-case, for example `02-softmax-attention`
- Python modules: snake_case, for example `linear_layer.py`
- Notebook files: `lesson.ipynb` unless the module has a stronger, stable naming reason
- Readme files: `README.md` at the section level and module level

## Examples

- Repository example: `foundations/01-linear-layer/`
- Shared code example: `src/ai_edu/foundations/linear_layer.py`
