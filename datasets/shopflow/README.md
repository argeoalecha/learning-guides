# ShopFlow

Used by: **[Statistics with Python guide](../../statistics-with-python/statistics-with-python_learning_guide.html)** (Modules 1.1–4.x)

An 80,400-row Philippine e-commerce transaction log with intentional real-world data-quality issues — nulls, a small duplicate-row tail, right-skewed order values with an outlier tail, and inconsistent phone-number formatting.

## File

`shopflow_orders.csv` — 80,400 rows (80,000 unique + 400 injected duplicates), 14 columns.

## Columns

`order_id, customer_id, order_date, delivery_date, product_category, region, quantity, order_value, discount_pct, shipping_fee, weight_kg, delivery_tier, delivery_status, customer_phone`

## Seeded data-quality issues (by design)

| Issue | Where | Notes |
|---|---|---|
| Nulls (~2% each) | `delivery_date`, `shipping_fee`, `weight_kg`, `customer_phone` | For missing-value handling exercises (Module 2.x) |
| Duplicate rows (~0.5%) | Whole rows | For dedup exercises — `df.duplicated()` should find exactly 400 |
| Right-skewed distribution | `order_value` | Skewness ≈ 4.5, a handful of high-value outliers (~0.5% of rows) — supports the skewness/kurtosis and log-transform exercises (1.2–1.3) |
| Inconsistent formatting | `customer_phone` | ~10% of non-null phones use `+63…` instead of `09…` — for string-normalization/regex exercises |

## Notes for exercises

- `pd.read_csv("shopflow_orders.csv", parse_dates=["order_date", "delivery_date"])` matches the guide's loading example exactly.
- The duplicate rows are **exact** row duplicates (not near-duplicates) — `df.duplicated().sum()` should return 400.
- Order value is generated via a log-normal distribution plus a small high-value tail, so a log transform (Exercise 1.3) should visibly reduce skewness and improve a normality test's p-value — that's the intended before/after.
