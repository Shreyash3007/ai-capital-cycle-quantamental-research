# Data directory

This directory will hold immutable learning fixtures and later versioned research snapshots.

Planned subdirectories will be added only when needed:

- `synthetic/` for small teaching fixtures;
- `raw/` for immutable provider snapshots;
- `normalized/` for stable schemas;
- `features/` for point-in-time model tables.

Every real dataset must document source, `as_of`, `available_from`, fetch time, units, transformations, missingness, licensing limits, and content hash.

ML-G01-T01 starts with a small in-script NumPy matrix, so no data file exists yet.
