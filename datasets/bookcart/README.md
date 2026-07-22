# BookCart

Used by: **[Python guide](../../python/python_learning_guide.html)**

**Not a downloadable dataset.** Exercise 1.1 explicitly has the learner *"download (or create) the three BookCart CSVs"* — generating the data is part of the exercise, so no starter files are provided here. This is a spec so the schema stays consistent across the guide.

## Files the learner builds

`books.csv`, `orders.csv`, `customers.csv`

## Schema (as referenced across the guide's exercises)

**books.csv**
| Column | Notes |
|---|---|
| `book_id` | Join key |
| `title` | |
| `category` | Used for revenue-by-category grouping exercises |
| `price` | |

**orders.csv**
| Column | Notes |
|---|---|
| `order_id` | |
| `book_id` | Foreign key to `books.csv` |
| `order_date` | Parsed with `pd.to_datetime` |
| `quantity` | Used with `price` to compute `revenue = quantity * price` |

**customers.csv**
| Column | Notes |
|---|---|
| `customer_id` | |
| *(name/region fields as needed by later modules)* | |

## Progression across the guide

Phase 1 bootstraps the project (`bookcart/` + `.venv`, `pandas`/`requests`, the three CSVs in `data/`). Later phases (Pandas, FastAPI, SQLAlchemy, pytest, packaging) all operate on this same trio of files, culminating in the **Final Capstone: BookCart Platform**.

## Notes

- If you'd rather not hand-author these, any small public book-sales dataset (e.g. a trimmed Kaggle bookstore dataset) with equivalent columns works — the guide's exercises only depend on the column names above, not a specific source.
