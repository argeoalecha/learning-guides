# E-commerce Orders Dataset

Used by: **[Pydantic guide](../../pydantic/pydantic_learning_guide.html)** (Modules 1.1–2.2)

1,500 order records, **deliberately messy** — this is a validation-library teaching dataset, so a meaningful fraction of rows fail one or more constraints on purpose. That messiness is the exercise, not a bug in the data.

## File

`ecommerce_orders.csv` — 1,500 rows, 10 columns.

## Columns

`order_id, customer_email, product_sku, quantity, unit_price, discount_pct, order_date, ship_date, region, status`

## Seeded data-quality issues (by design)

| Issue | Approx. rate | Exercise it supports |
|---|---|---|
| Malformed `customer_email` (missing `@`, blank, wrong format) | ~6.5% | Exercise 1.3 — `EmailStr` validation |
| Non-numeric or negative `quantity` (`"five"`, `"-2"`, blank) | ~4% | Exercise 1.1 — "Spot the Bug", `ValidationError` |
| Invalid `unit_price` (negative or zero) | ~3% | Exercise 1.3 — `Field(gt=0)` |
| `discount_pct` outside 0.0–1.0, or blank | ~15% | Exercise 1.3 — `Field(ge=0.0, le=1.0)`; Exercise 1.4 — custom validator |
| `ship_date` earlier than `order_date` | ~5% | Exercise 1.4 / Phase 1 Capstone — `@model_validator` cross-field check |
| Blank `ship_date` (order not yet shipped) | ~15% | Optional-field handling |
| Inconsistent `status` casing (`SHIPPED` vs `shipped`) | ~8% | Exercise 1.4 — `@field_validator(mode="before")` lowercasing |
| Leading/trailing whitespace on `order_id` | ~5% | Exercise 1.4 — `@field_validator(mode="before")` strip/uppercase |
| Blank `region` | ~3% | Optional-field / normalization handling |

## Notes for exercises

- Run `load_orders_from_csv()` (Exercise 2.2) on the **full** file — expect roughly **22–23% of rows** to fail at least one validator once all constraints from Modules 1.3–1.4 are implemented (verified empirically against the seeded issue rates above; a handful of rows stack more than one problem, which is why it's a bit below the sum of the individual rates).
- The dataset is regenerated deterministically (seeded RNG) — row counts and error rates above are stable across re-generations from `datasets/gen_datasets.py` if you ever need to reproduce or extend it.
