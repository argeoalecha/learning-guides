"""make_dataset.py — generate the Sales 2026 dataset used by every exercise.

Creates three CSVs in ./data:
    products.csv    8 rows   dimension: catalogue, price, stock
    customers.csv  37 rows   dimension: account, region, segment (3 dormant)
    sales.csv     652 rows   fact: one row per order line (646 clean + 6 deliberately bad)

Deterministic: same seed, same files, every time.
    python make_dataset.py                # 646 clean order lines
    python make_dataset.py --rows 412908  # big file for the streaming exercises
"""

from __future__ import annotations

import argparse
import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 2026
START = date(2026, 1, 1)
END = date(2026, 6, 30)

# product_code, product, category, unit_price, stock, reorder_point
PRODUCTS = [
    ("PS-100", "Pump seal",         "Rotating equipment",  1450.00, 240,  60),
    ("BR-500", "Bearing housing",   "Rotating equipment",  6750.00,  48,  20),
    ("IM-600", "Impeller",          "Rotating equipment", 12300.00,   8,  12),
    ("VK-200", "Valve kit",         "Valves & fittings",   8900.00,  62,  25),
    ("GS-300", "Gasket set",        "Valves & fittings",    320.00, 900, 200),
    ("CV-800", "Check valve",       "Valves & fittings",   4150.00,   9,  15),
    ("FM-400", "Flow meter",        "Instrumentation",    24500.00,   5,   8),
    ("PG-700", "Pressure gauge",    "Instrumentation",     1980.00, 130,  40),
]

SEGMENTS = ["Manufacturing", "Utilities", "Marine", "Construction"]

# region -> (number of active accounts, number of clean order lines)
REGIONS = {"NCR": (18, 406), "Cebu": (10, 142), "Davao": (6, 98)}

# Accounts on the books that never placed an order in the period. They exist so
# the anti-join exercises ("which customers bought nothing?") return real rows.
DORMANT = [
    ("C-NCR-019", "NCR Industrial Account 19",   "NCR",   "Construction"),
    ("C-CEB-011", "Cebu Industrial Account 11",  "Cebu",  "Utilities"),
    ("C-DAV-007", "Davao Industrial Account 07", "Davao", "Marine"),
]

# Regional demand mix. NCR skews to rotating equipment, Cebu to valves,
# Davao is mixed — this is what makes the GROUP BY exercises interesting.
MIX = {
    "NCR":   [0.20, 0.14, 0.10, 0.12, 0.18, 0.08, 0.06, 0.12],
    "Cebu":  [0.10, 0.06, 0.04, 0.26, 0.28, 0.14, 0.04, 0.08],
    "Davao": [0.22, 0.10, 0.06, 0.14, 0.20, 0.10, 0.08, 0.10],
}

# Six deliberately broken rows. Module 2.2 logs and skips them;
# Module 2.3 drops the duplicate. Do not "fix" them in the generator.
BAD_ROWS = [
    ("PH-01412", "2026-03-11", "C-NCR-004", "PS-100",  "NCR",   ""),      # blank qty
    ("PH-01488", "2026-03-29", "C-CEB-002", "GS-300",  "Cebu",  "six"),   # qty not numeric
    ("PH-01041", "2026-01-04", "C-NCR-001", "PS-100",  "NCR",   "12"),    # duplicate order_id
    ("PH-01530", "2026-04-14", "C-DAV-003", "ZZ-999",  "Davao", "4"),     # unknown product
    ("PH-01602", "",           "C-NCR-011", "VK-200",  "NCR",   "3"),     # missing date
    ("PH-01655", "2026-05-30", "C-CEB-007", "FM-400",  "Cebu",  "-2"),    # negative qty
]


def build_customers() -> list[dict]:
    rng = random.Random(SEED)
    rows = []
    for region, (n_accounts, _) in REGIONS.items():
        prefix = {"NCR": "NCR", "Cebu": "CEB", "Davao": "DAV"}[region]
        for i in range(1, n_accounts + 1):
            rows.append({
                "customer_id": f"C-{prefix}-{i:03d}",
                "customer": f"{region} Industrial Account {i:02d}",
                "region": region,
                "segment": rng.choice(SEGMENTS),
            })
    fields = ["customer_id", "customer", "region", "segment"]
    rows += [dict(zip(fields, d)) for d in DORMANT]
    return rows


def build_sales(customers: list[dict], scale: int | None) -> list[dict]:
    rng = random.Random(SEED + 1)
    dormant = {d[0] for d in DORMANT}
    by_region: dict[str, list[str]] = {r: [] for r in REGIONS}
    for c in customers:
        if c["customer_id"] not in dormant:
            by_region[c["region"]].append(c["customer_id"])

    codes = [p[0] for p in PRODUCTS]
    span = (END - START).days

    # Scale each region's line count proportionally when --rows is given.
    base_total = sum(n for _, n in REGIONS.values())
    counts = {r: n for r, (_, n) in REGIONS.items()}
    if scale:
        counts = {r: round(n * scale / base_total) for r, n in counts.items()}

    rows, oid = [], 1041
    for region, n_lines in counts.items():
        for _ in range(n_lines):
            code = rng.choices(codes, weights=MIX[region])[0]
            price = dict((p[0], p[3]) for p in PRODUCTS)[code]
            # Cheap consumables move in bulk; capital items move in ones and twos.
            qty = rng.randint(10, 60) if price < 1000 else (
                rng.randint(3, 18) if price < 5000 else rng.randint(1, 5))
            rows.append({
                "order_id": f"PH-{oid:05d}",
                "order_date": (START + timedelta(days=rng.randint(0, span))).isoformat(),
                "customer_id": rng.choice(by_region[region]),
                "product_code": code,
                "region": region,
                "qty": str(qty),
            })
            oid += 1

    rows.sort(key=lambda r: r["order_date"])
    if not scale:  # only pollute the small teaching file
        fields = ["order_id", "order_date", "customer_id", "product_code", "region", "qty"]
        rows += [dict(zip(fields, bad)) for bad in BAD_ROWS]
    return rows


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {path}  ({len(rows)} rows)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", type=int, default=None,
                    help="total clean order lines (default 646)")
    ap.add_argument("--out", type=Path, default=Path("data"))
    args = ap.parse_args()

    products = [dict(zip(
        ["product_code", "product", "category", "unit_price", "stock", "reorder_point"],
        (row[0], row[1], row[2], f"{row[3]:.2f}", row[4], row[5]),
    )) for row in PRODUCTS]
    customers = build_customers()
    sales = build_sales(customers, args.rows)

    write_csv(args.out / "products.csv", products,
              ["product_code", "product", "category", "unit_price", "stock", "reorder_point"])
    write_csv(args.out / "customers.csv", customers,
              ["customer_id", "customer", "region", "segment"])
    write_csv(args.out / "sales.csv", sales,
              ["order_id", "order_date", "customer_id", "product_code", "region", "qty"])


if __name__ == "__main__":
    main()
