# Superstore Sales

Used by: **[Data Analyst guide](../../data-analyst/da_learning_guide_v3_merged.html)** (Modules 1.1–2.4)

Synthetic dataset in the style of the well-known "Sample Superstore" retail dataset. 2,000 orders across 3 years, mirroring the row-shape and column names of the public Kaggle version so any external Superstore tutorial content still lines up.

## Files

| File | Use |
|---|---|
| `superstore_sales.csv` | Flat single-table version — Excel modules (1.1–1.2): PivotTables, formulas, structured Tables |
| `Superstore_Sales.xlsx` | Same data pre-loaded into an `.xlsx` workbook (`Orders` sheet) — open directly in Excel |
| `fact_Sales.csv` | Fact table for the star-schema exercises (Power Pivot / DAX, Module 2.2+) |
| `dim_Product.csv` | Product dimension (Product ID, Name, Category, Sub-Category) |
| `dim_Customer.csv` | Customer dimension (Customer ID, Name, Segment) |
| `dim_Region.csv` | Region dimension (Region, State, City, Country) |
| `dim_Date.csv` | Date dimension spanning the order date range, with Year/Quarter/Month/Day-of-Week columns — mark as a Date Table in Power Pivot |

## Columns (flat version)

`Order ID, Order Date, Ship Date, Ship Mode, Customer ID, Customer Name, Segment, Country, City, State, Postal Code, Region, Product ID, Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit`

## Notes for exercises

- Profit is intentionally negative on a meaningful subset of rows (high-discount Furniture orders skew this way) — supports the `COUNTIFS(Profit<0)` and "which sub-category loses money" exercises.
- Discount values cluster at 0, 10, 15, 20, 30, 40, 50% — realistic for `SUMIFS`/`FILTER` grouping exercises.
- `fact_Sales` joins to all four dimension tables on their respective ID/key columns — build the star schema with `fact_Sales` at the center.
- For the guide's SQL and capstone inventory exercises (reorder alerts, dead-stock detection), see [`../inventory/`](../inventory/) — it shares this dataset's Product ID catalog.
