# Error Handling

Week-one code is local Python and notebooks, not a networked service. Error handling should
stay simple, explicit, and educational.

## Scenario: Curriculum Module Boundary Validation

### 1. Scope / Trigger

- Trigger: adding module functions, module scripts, or notebook-backed examples
- Applies to: module-local `.py` files under `foundations/`, `training/`, and `agents/`

### 2. Signatures

- Validation failure: raise `ValueError` with a message that names the violated assumption
- Unsupported future work: raise `NotImplementedError` only for clearly marked extension points
- Internal impossible state: raise `RuntimeError` with actionable context

### 3. Contracts

- Error messages must tell the learner what input or invariant was wrong.
- Notebook examples should fail fast rather than silently clipping or coercing data.
- Module code should not swallow exceptions just to keep notebooks running.
- `print()` is not error handling; use exceptions for failures and logging for diagnostics.
- If a module offers both torch and reference paths, missing torch should raise a
  clear runtime error at the torch boundary rather than breaking the reference path.

### 4. Validation & Error Matrix

| Condition | Error |
|-----------|-------|
| Empty or invalid shape/config data passed into shared helpers | `ValueError` |
| Placeholder function intentionally left for a later milestone | `NotImplementedError` with TODO context |
| Unexpected state after validation already passed | `RuntimeError` |

### 5. Good / Base / Bad Cases

- Good: `raise ValueError("input_dim must be positive")`
- Base: validate public function inputs at the top of the function
- Bad: returning `None` on invalid input and letting the notebook continue silently

### 6. Tests Required

- Add unit tests for each public validation branch introduced in a module `.py` file.
- If a module file grows too large, refactor within the module directory before adding another top-level abstraction layer.
- Regression tests should assert the exception type and the key message fragment.

### 7. Wrong vs Correct

#### Wrong

```python
def build_layer(input_dim: int) -> dict[str, int] | None:
    if input_dim <= 0:
        return None
    return {"input_dim": input_dim}
```

#### Correct

```python
def build_layer(input_dim: int) -> dict[str, int]:
    if input_dim <= 0:
        raise ValueError("input_dim must be positive")
    return {"input_dim": input_dim}
```

## API Error Responses

No API layer exists in week one. If the project later introduces services or CLIs with
stable machine-readable output, this spec must be extended before implementation.

## Common Mistakes

- Hiding invalid inputs inside notebooks to avoid interrupting a demo
- Leaving broad `except Exception:` blocks in lesson scaffolds
- Using `assert` for user-facing validation in library code
