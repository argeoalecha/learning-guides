# TindaHub Orders

Used by: **[Excel guide](../../excel/excel_learning_guide.html)** (every module and capstone), **[Python Excel Libraries guide](../../python-excel-libraries/python-excel-libraries_learning_guide.html)**, **[Python Scientific Computing guide](../../python-scientific-computing/python-scientific-computing_learning_guide.html)**, **[Python GIS & Mapping guide](../../python-gis-mapping/python-gis-mapping_learning_guide.html)** (with its bundled `tindahub_city_coords.csv`), **[R GIS & Mapping guide](../../r-gis-mapping/r-gis-mapping_learning_guide.html)**

The flat, 5,000-row order register the Excel guide calls the "TindaHub Orders workbook" throughout — a Philippine sari-sari store distribution business. Distinct from [`tindahub/`](../tindahub/) (the normalized 6-table SQL schema used by the postgresql-metabase guide) — same fictional business, different shape: this one is a deliberately flat, single-table-per-sheet register because the Excel guide teaches Tables, lookups, and PivotTables, not joins.

Every sheet ships as a **plain range**, not a pre-built Excel Table — Module 1.3's first exercise is converting `Orders`/`Products`/`Customers` to named Tables with Ctrl+T, so pre-Tabling them would rob the exercise.

**Date columns are real Excel dates** (true serial values), displayed in the deliberately ambiguous US-style `mm/dd/yyyy`. Real dates are required for PivotTable date grouping, Timeline slicers, `EOMONTH`, `NETWORKDAYS.INTL`, and date-bounded `SUMIFS`; the ambiguous *display* is what gives Module 1.4's "reformat to `yyyy-mm-dd` for unambiguous sorting" exercise something to do. The one exception is `ImportedDates`, which is intentionally text — see below.

## Files

| File | Use |
|---|---|
| `TindaHub_Orders.xlsx` | The workbook itself — one sheet per table below. Open this and start at Module 1.1. |
| `tindahub_orders.csv` | Same data as the `Orders` sheet, as CSV |
| `tindahub_products.csv` | Same data as the `Products` sheet, as CSV |
| `tindahub_customers.csv` | Same data as the `Customers` sheet, as CSV |
| `tindahub_raw_contacts.csv` | Same data as the `RawContacts` sheet, as CSV |
| `tindahub_messy_import.csv` | Same data as the `MessyImport` sheet, as CSV |
| `tindahub_2026-04.csv`, `tindahub_2026-05.csv`, `tindahub_2026-06.csv` | Three monthly raw extracts for Module 4.2's Power Query capstone (Get Data → From Folder) |

## Sheets in `TindaHub_Orders.xlsx`

**`Orders`** (5,000 rows) — `OrderID, OrderDate, CustomerID, Customer, Barangay, City, Province, Region, Product, Category, Qty, UnitPrice, Amount, PaymentMethod, Status, DeliveredDate, ImportedDates`. Jan–Jun 2026, 6 regions (NCR, Central Luzon, CALABARZON, Central Visayas, Davao Region, Western Visayas), 26 products across 6 categories (Noodles & Canned Goods includes "Lucky Me..." and "...Corned Beef" products for the guide's wildcard-criteria examples). `DeliveredDate` is blank for Pending/Cancelled orders. `ImportedDates` is the same calendar date as `OrderDate` but stored as **text** in `dd/mm/yyyy` format — Module 2.2's exercise is converting the whole column to real dates.

**`Products`** (26 rows) — `Product, Category, UnitPrice`. Master price list; the source Module 4.2's Power Query merge pulls `Category` from.

**`Customers`** (200 rows) — `CustomerID, Name, Mobile, Barangay, City, Province, Region, JoinDate`. All 200 `Name` values are **unique**, and every `Orders` row carries the matching `CustomerID`, so joining `Orders` → `Customers` on `CustomerID` (or on `Name`) reproduces that row's `Barangay/City/Province/Region` exactly — verified 0 mismatches across all 5,000 rows. Module 2.1's exercise joins on `CustomerID`, the reliable key.

**`RawContacts`** (60 rows) — `RawEntry, Mobile`. `RawEntry` jams `"Surname, FirstName | City"` into one column, mixed-case, with stray spaces — Module 2.2's TEXTSPLIT/TRIM/PROPER exercise. `Mobile` is seeded at an 80/20 valid/invalid rate, landing at **52 of 60 valid** PH format (`09XXXXXXXXX`) with **8 invalid** (missing digit, `+63` prefix, letters) for the REGEXTEST exercise.

**`MessyImport`** (500 rows) — `OrderID, OrderDate, Customer, City, Region, Product, Qty, UnitPrice, Amount, Mobile, PaymentMethod, Status`. Seeded for Module 4.1: 15 duplicate `OrderID`s (known ground truth — audit with `COUNTIF` before removing, and confirm the count matches), **76 of 500** `Amount` values stored as text-numbers (15.2%), **106** `Customer` values padded with stray spaces and upper-cased (21.2%), city-name variants (`"Quezon City"` / `"QC"` / `"quezon city"`, similarly for Manila and Cebu City), **12** `OrderDate` values seeded in the future (2.4%, spanning Dec 2026 – Jan 2027) to trip the no-future-dates validation rule, and a handful of malformed `Mobile` values. `OrderDate` here is a **real date**, so both the Data Validation rule and an `=OrderDate>TODAY()` audit can actually catch those 12 rows.

## Monthly CSV extracts (`tindahub_2026-04/05/06.csv`)

Raw shape as they'd arrive from a POS export — **no `Category` column** (Module 4.2 merges it in from `Products`), `OrderDate` as `dd/mm/yyyy` text (PH locale — the "Changed Type with Locale" teaching point), a few `Status = "Test"` rows to filter out, and 4 duplicate `OrderID`s seeded within each file (the "Removed Duplicates" applied step). Row counts: 320 / 345 / 360 — verify Power Query's appended total equals the sum after building the From Folder query.

## Seeded ground truth (for grading / self-check)

- `Orders`: exactly **3** rows where `Amount ≠ Qty × UnitPrice` (Module 1.3's `LineCheck` exercise), exactly **8** duplicate `OrderID`s (conditional-formatting exercise).
- `MessyImport`: exactly **15** duplicate `OrderID`s, **76** text-number `Amount`s, **12** future-dated `OrderDate`s.
- Each monthly CSV: exactly **4** duplicate `OrderID`s within the file. Raw append total is **1,025** (320 + 345 + 360); after the guide's Filtered-Rows (`Status = "Test"`) and Removed-Duplicates steps it is **989** — the 36-row gap is 24 Test rows plus 12 duplicates, and reconciling it is part of Module 4.2's exercise.
- `Orders` column letters (for the guide's formula-based conditional formatting): **A** OrderID, **B** OrderDate, **C** CustomerID, **D** Customer, **M** Amount, **O** Status.

## Regenerating

Generated by the same script as `superstore-sales`, `shopsphere`, `ecommerce-orders`, `shopflow`, and `inventory` — see the root [`datasets/README.md`](../README.md). Deterministic (seeded RNG, `np.random.default_rng(42)`); re-running `gen_datasets.py` reproduces this data byte-for-byte.
