# ShopSphere

Used by: **[Data Science & ML guide](../../data-science-ml/data-science-ml_learning_guide.html)** (Modules 1.1–5.2)

An online retailer's customer table (demographics, behavior, transactions) plus a free-text reviews table, used across the guide to predict churn, estimate lifetime value, segment customers, and classify review sentiment.

## Files

| File | Rows | Use |
|---|---|---|
| `shopsphere_customers.csv` | 6,000 | Churn prediction, baselines, feature engineering, segmentation (Modules 1.1–4.x) |
| `shopsphere_reviews.csv` | 4,000 | Sentiment classification — TF-IDF + logistic regression (Exercise 5.2) |

## `shopsphere_customers.csv` columns

| Column | Notes |
|---|---|
| `customer_id` | Unique customer identifier |
| `tenure_months` | Months since signup |
| `avg_order_value` | Mean order value, correlates with `plan_type` |
| `orders_last_90d` | Recency/frequency signal |
| `days_since_last_order` | Higher values correlate with churn |
| `support_tickets` | Count of support tickets filed |
| `plan_type` | `basic` / `standard` / `premium` |
| `region` | Philippine region code |
| `churned_next_30d` | **Target.** 1 if no purchase in the next 30 days. Base rate ≈ 6% — deliberately imbalanced to support the guide's DummyClassifier-baseline and imbalanced-metric teaching points (Module 1.2's "if only 5% of ShopSphere customers churn…" callout). |
| `cancellation_reason` | **Leakage column** — only populated for churned rows, unavailable at prediction time. Exclude it in Exercise 1.1's leakage-identification task. |
| `refund_after_churn` | **Leakage column** — same reasoning; a post-churn event, not a predictor. |

## `shopsphere_reviews.csv` columns

`review_id, customer_id, review_text, sentiment` (`sentiment` is `positive`/`negative`, ~60/40 split — use as the label for Exercise 5.2, or drop it and predict it to test your pipeline).

## Notes for exercises

- `cancellation_reason` and `refund_after_churn` are included **on purpose** as leakage traps — Module 1.1's exercise explicitly asks you to identify features that wouldn't be available at prediction time. Training a model that includes them will look implausibly good and fail in production, which is the point.
- The ~6% churn base rate makes accuracy a misleading metric on its own — the guide's baseline exercise (1.2) uses this to motivate precision/recall and a `DummyClassifier` comparison.
