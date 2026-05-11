# Logging Guidelines

Week-one logging is intentionally lightweight. The project does not need a custom logging
stack yet, but it does need consistent rules so notebook output and reusable package code
do not drift.

## Overview

- Use the Python standard library `logging` module for reusable package code and scripts.
- Use `print()` only for deliberate notebook pedagogy or very small CLI examples.
- Prefer module-level loggers: `logger = logging.getLogger(__name__)`.

## Log Levels

- `DEBUG`: tensor shapes, step-by-step internals, or temporary diagnostics that are useful
  while building a lesson but safe to disable by default
- `INFO`: major milestones such as loading a dataset or starting a training stage
- `WARNING`: recoverable states where the code falls back to a safer option
- `ERROR`: failures that abort the current action and then raise or propagate an exception

## Structured Logging

Week one does not require JSON logs. Keep messages plain text but make them specific:

- Include the module or lesson stage in the message
- Include counts, dimensions, or config values when they help debugging
- Do not log full notebook cell outputs or large tensors unless explicitly debugging

## What to Log

- Entrypoint configuration summaries
- Major state transitions in longer-running scripts
- Recovery paths that might explain surprising results to a learner

## What NOT to Log

- Secrets or tokens if later integrations are added
- Entire datasets or large tensor contents by default
- Duplicate exception messages immediately before re-raising the same error

## Common Mistakes

- Using `print()` inside reusable library code
- Logging an exception and then swallowing it
- Leaving noisy debug logs in lessons after the educational goal is clear
