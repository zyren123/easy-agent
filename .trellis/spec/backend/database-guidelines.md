# Database Guidelines

Week one does not introduce a database. Persistence decisions are intentionally deferred so
the early curriculum can stay CPU-friendly and easy to run in local notebooks or hosted
environments.

## Overview

- No ORM, query layer, or migration system is approved in week one.
- Do not add a database dependency as part of a curriculum module without updating this spec.

## Query Patterns

Not applicable yet. Use local files or in-memory examples for week-one and first-slice work.

## Migrations

Not applicable until the project has a storage-backed feature.

## Naming Conventions

When storage is eventually introduced, add naming rules here before code lands.

## Common Mistakes

- Pulling in a database just to store temporary lesson state
- Hiding storage decisions inside notebooks without spec updates
