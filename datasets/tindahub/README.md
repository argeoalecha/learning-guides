# TindaHub

Used by: **[PostgreSQL & Metabase guide](../../postgresql-metabase/postgresql-metabase_learning_guide.html)** (Module 1.2 onward)

A Philippine online marketplace schema (COD, peso-priced) — six normalized tables covering categories, customers, products, orders, order items, and payments.

Same fictional business as [`tindahub-orders/`](../tindahub-orders/) (used by the Excel guide), flattened differently — that one is a single 5,000-row order register for Tables/lookups/PivotTables, not a normalized schema for joins.

## Files

| File | Use |
|---|---|
| `schema.sql` | Creates all six tables with correct types, primary/foreign keys, and `CHECK` constraints. Idempotent — safe to re-run (drops tables first). |
| `seed.sql` | Idempotent seed data (`ON CONFLICT DO NOTHING`) — 4 categories, 8 customers, 15 products, 20 orders, ~60 order items, and payments. Run **after** `schema.sql`. |

## Usage

```bash
psql -d tindahub -f schema.sql -f seed.sql
```

Originally lived alongside the guide at `postgresql-metabase/schema.sql` / `seed.sql`; moved here so every guide's benchmark data lives in one shared location. The guide's Module 1.2 references this path directly.

## Schema overview

```
categories ──< products ──< order_items >── orders ──< payments
                                              orders >── customers
```

- `orders.status` is constrained to `pending | shipped | delivered | cancelled`
- `payments.method` is constrained to `cod | gcash | card | bank` — reflecting real Philippine payment mix
- `products.attributes` is a `jsonb` column (variable product specs like wattage, size, color) — used in the guide's JSONB query modules

Note: the guide's own capstone exercise asks the learner to **build** an equivalent schema.sql/seed.sql from scratch as a deliverable — treat these files as the reference/starter version to seed the database before that point, not a substitute for doing the exercise.
