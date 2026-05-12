# Directory Structure

This project teaches AI systems through self-contained curriculum modules.
Repository structure should help a learner find the explanation, implementation,
and notebook in one place without jumping between parallel code trees.

## Scenario: Week-One Repository Foundation

### 1. Scope / Trigger

- Trigger: establish the initial directory contract for a long-lived educational repo
- Applies to: new modules, tests, and planning artifacts

### 2. Signatures

- Curriculum section roots: `foundations/`, `training/`, `agents/`
- Module directory signature: `<section>/<nn>-<kebab-case-topic>/`
- Required module files: `README.md`, topic-named `.py`, topic-named `.ipynb`

### 3. Contracts

- Curriculum folders contain educational, module-scoped material and should stay readable
  without navigating a separate docs site or a second code tree.
- The primary implementation for an early module lives in the module folder itself.
- For `foundations/` architecture modules, the topic `.py` file should contain a
  torch implementation plus a non-framework reference implementation when that
  comparison teaches the mechanism clearly.
- Tests live under `tests/` and target stable module behavior or layout contracts.
- Planning artifacts remain under `.trellis/tasks/<task>/`.

### 4. Validation & Error Matrix

| Condition | Result |
|-----------|--------|
| New important logic added directly inside a notebook | Move the logic into the module's `.py` file |
| New module folder is not numbered kebab-case | Rename before merge |
| Module lacks `README.md`, a topic `.py`, or a topic `.ipynb` | Incomplete module scaffold |
| Foundations architecture module has torch code but no comparable reference path | Incomplete teaching scaffold |
| New top-level docs tree duplicates module-local docs | Reject unless backend spec changes |

### 5. Good / Base / Bad Cases

- Good: `foundations/01-linear-layer/README.md` plus `foundations/01-linear-layer/linear_layer.py`
- Base: section root `training/README.md` exists before individual modules land
- Bad: `docs/linear_layer.md` as the only explanation for a curriculum module

### 6. Tests Required

- Smoke tests should verify curriculum layout and runnable module behavior.
- When scaffolding a new module, add at least one test for the module's public contract.
- For foundations architecture modules, add a parity test or parity helper that
  compares the torch path against the reference path on the same input.
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
    linear_layer.py
    linear_layer.ipynb
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
│       ├── linear_layer.py
│       └── linear_layer.ipynb
├── training/
│   └── README.md
├── agents/
│   └── README.md
└── tests/
```

## Module Organization

- Put the main implementation in the module's topic-named `.py` file.
- Put the beginner-friendly walkthrough in the matching topic-named `.ipynb`.
- Keep the `.py` and `.ipynb` conceptually aligned.
- In `foundations/`, prefer one module file that contains both the torch path and
  the reference path rather than splitting a simple concept across many files.
- Keep section-level `README.md` files short; they index modules and progression.
- Avoid nested packaging complexity in week one.

## Naming Conventions

- Curriculum directories: numbered kebab-case, for example `02-softmax-attention`
- Python modules: snake_case, for example `linear_layer.py`
- Notebook files should mirror the module name, for example `linear_layer.ipynb`
- Readme files: `README.md` at the section level and module level

## Examples

- Repository example: `foundations/01-linear-layer/`
- Module code example: `foundations/01-linear-layer/linear_layer.py`
