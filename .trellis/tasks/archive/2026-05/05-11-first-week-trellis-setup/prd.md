# First week Trellis setup for AI education project

## Goal

Set up Trellis and define the first-week foundation for a long-term AI education repository that teaches model internals, training pipelines, and agent systems through a production-style but progressively educational codebase.

## What I already know

* The project goal is a cohesive educational codebase, not a collection of disconnected demos.
* The curriculum has three major sections: model architecture fundamentals, model training pipeline, and agent systems.
* Each important module should include production-style Python code plus aligned educational Jupyter notebooks.
* Early lessons must stay CPU-friendly and easy to run on Kaggle, Colab, and local Jupyter.
* Later lessons should adopt more realistic tooling for finetuning and agent systems.
* The user only wants the first week of work scoped now.
* The first-week deliverables should include repository structure, conventions, documentation standards, notebook standards, testing strategy, boundaries, milestone breakdown, and a small first-task PRD.
* Current repo state is still bootstrap-level Trellis scaffolding; backend spec files are templates and there is no established curriculum code layout yet.
* The user selected `Python-first curriculum repo` as the primary first-month delivery mode.
* The user selected `uv + pyproject.toml` as the package and environment management standard.
* The user selected `single Python package` as the initial repository organization model.
* The user wants module-local documentation rather than a separate docs site in week one: each module folder should contain Python files, notebooks, and `README.md`.
* The user selected numbered kebab-case module directories such as `01-linear-layer`.
* The user selected semantic top-level curriculum sections: `foundations`, `training`, and `agents`.
* The user selected `ai_edu` as the Python package name under `src/`.

## Assumptions (temporary)

* Week one should freeze repository-level conventions before any substantial curriculum content is implemented.
* The first implementation slice will likely live in Section 1 because it has the strongest dependency on shared tensor/model conventions.
* The project will initially stay Python-first, with optional frontend/docs tooling added only if it has a clear educational or operational role.
* Project commands, local setup, and CI should all route through `uv`.
* Shared educational infrastructure should live inside one package rather than separate publishable packages in week one.
* Documentation should live next to each teaching module by default.
* Section-level directories can contain many module folders, while reusable code should live under `src/ai_edu/`.

## Open Questions

* None blocking for week-one foundation planning.

## Requirements (evolving)

* Define the repository structure for the first week only.
* Freeze a minimal set of early architectural decisions that prevent drift across future curriculum modules.
* Establish shared standards for docs, notebooks, tests, naming, error handling, and module boundaries.
* Create a small first-task PRD that is implementation-ready.
* Keep the plan maintainable for a long-term educational open-source project.
* Generate initial Trellis spec content so later implementation/check tasks inherit the same conventions.

## Acceptance Criteria (evolving)

* [ ] First-week scope is documented with explicit in-scope and out-of-scope boundaries.
* [ ] Early architectural decisions are identified and either frozen or marked for follow-up.
* [ ] Initial repository layout is defined consistently with the educational progression.
* [ ] Shared conventions are documented clearly enough for future Trellis implementation tasks.
* [ ] A concrete first implementation task exists after planning.
* [ ] Trellis spec files are no longer placeholder-only for the relevant week-one decisions.

## Definition of Done (team quality bar)

* Tests added/updated where code is introduced
* Lint / typecheck / CI expectations defined
* Docs/notes updated if behavior changes
* Rollout/rollback considered if risky

## Out of Scope (explicit)

* Designing the full multi-month curriculum in implementation detail
* Building all three sections now
* Choosing every future library/tool in advance
* Shipping polished course content beyond the first-week foundation
* Building a separate documentation website

## Technical Notes

* Active task: `.trellis/tasks/05-11-first-week-trellis-setup/`
* Existing spec index: `.trellis/spec/backend/index.md` is still template-level and should be filled based on real decisions made during this task.
* Existing bootstrap task: `.trellis/tasks/00-bootstrap-guidelines/prd.md`
* Expected week-one outputs include repository layout, spec conventions, and a first implementation task for the initial curriculum slice.
