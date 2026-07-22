# Data Analyst Learning Guide
## Beginner to Intermediate Track
### Tools: Excel · Power Query · Power Pivot · Python · SQL

---

> **How to use this guide — you do NOT have to start at Module 1.1**
> This guide is built to be **non-linear**. Each module is self-contained with its own prerequisites, skip-check, and outcomes. Use the **Placement Quiz** below to find your entry point, or jump straight to any module using the **Module Index**. Each module header tells you what you must already know, how to test out of it, and what it unlocks. All capstone datasets are standard **Sales & Inventory** scenarios — realistic, reusable, and interview-relevant.

---

## Quick Start: Three Ways to Use This Guide

1. **Complete beginner** → Start at Module 1.1 and go sequentially.
2. **Some experience** → Take the **Placement Quiz** (next section) to find your entry point.
3. **Targeting a specific skill or certification** → Jump via the **Module Index** or the **Certification Roadmap**, and use **Learning Tracks** to follow a curated subset.

---

## Placement Quiz — Find Your Starting Point

Answer honestly. Score 1 point per "yes." Your **lowest-scoring** area is where you should start.

### Section A — Excel (Modules 1.2–2.3)
- [ ] I can write VLOOKUP/XLOOKUP and nested IF formulas without looking them up
- [ ] I build Pivot Tables with slicers and calculated fields regularly
- [ ] I use SUMIFS/COUNTIFS and structured Table references (`Table[Column]`)
- [ ] I know dynamic array functions (FILTER, SORT, UNIQUE)

**0–1 yes** → Start **Module 1.2** | **2–3 yes** → Start **Module 2.1** | **4 yes** → Skip to **Module 2.2**

### Section B — Power Query / Power Pivot (Modules 2.1–2.2)
- [ ] I have combined multiple files with Get Data > From Folder
- [ ] I can merge and append queries (joins in Power Query)
- [ ] I have built a star schema with relationships
- [ ] I can write DAX measures using CALCULATE and time intelligence

**0–1 yes** → Start **Module 2.1** | **2–3 yes** → Start **Module 2.2** | **4 yes** → Skip to **Phase 3**

### Section C — Python (Modules 3.1–3.5)
- [ ] I write Python functions, loops, and list comprehensions comfortably
- [ ] I clean data in Pandas (nulls, dtypes, groupby, merge)
- [ ] I run statistical tests (t-test, correlation) and interpret p-values
- [ ] I have trained a scikit-learn model and evaluated it

**0 yes** → Start **Module 3.1** | **1 yes** → Start **Module 3.2** | **2–3 yes** → Start **Module 3.3 or 3.5** | **4 yes** → Skip to **Phase 4**

### Section D — SQL (Modules 4.1–4.2)
- [ ] I write JOINs across 3+ tables and use GROUP BY/HAVING
- [ ] I use CASE WHEN and subqueries
- [ ] I use window functions (ROW_NUMBER, LAG, running totals)
- [ ] I write CTEs and do data profiling in SQL

**0–1 yes** → Start **Module 4.1** | **2–3 yes** → Start **Module 4.2** | **4 yes** → Skip to **Phase 5**

> **Rule of thumb:** If you can already complete a module's **Exercise** without studying it, skip the module. The exercise *is* the test-out.

---

## Module Index (Jump Anywhere)

| Module | Topic | Level | Prereqs | Time |
|---|---|---|---|---|
| 1.1 | Data Analyst Fundamentals | Beginner | None | 3h |
| 1.2 | Excel Fundamentals | Beginner | None | 12h |
| 1.3 | Excel Tables & Structured Data | Beginner | 1.2 | 3h |
| 2.1 | Power Query (ETL) | Beginner–Int | 1.3 | 14h |
| 2.2 | Power Pivot & DAX | Intermediate | 2.1 | 18h |
| 2.3 | Advanced Excel Analytics | Intermediate | 1.2 | 8h |
| 3.1 | Python Basics for Analysts | Beginner | None | 12h |
| 3.2 | Pandas — Cleaning & Manipulation | Beginner–Int | 3.1 | 20h |
| 3.3 | Statistics for Analysts | Intermediate | 3.2 | 14h |
| 3.4 | EDA Framework | Intermediate | 3.2 | 12h |
| 3.5 | Machine Learning & DS Basics | Intermediate | 3.2, 3.3 | 18h |
| 4.1 | SQL Fundamentals | Beginner | None | 14h |
| 4.2 | Intermediate SQL (Windows, CTEs) | Intermediate | 4.1 | 16h |
| 5.1 | Python + SQL Integration | Intermediate | 3.2, 4.1 | 6h |
| 5.2 | End-to-End Pipeline | Intermediate | Phases 2–4 | 6h |
| 5.3 | Portfolio Setup | All | Any capstone | 4h |

> **Note:** The four tool tracks (Excel/Power BI, Python, SQL) are **independent**. You can do Phase 4 (SQL) before Phase 3 (Python), or run them in parallel. Only **Phase 5** requires multiple tracks complete.

---

## Learning Tracks (Curated Paths)

Pick a track based on your goal. Each is a valid subset — you don't need everything.

### Track 1 — Excel/Power BI Analyst (fastest to employable)
`1.1 → 1.2 → 1.3 → 2.1 → 2.2 → 2.3 → Capstone 2`
Target cert: **Microsoft PL-300 (Power BI Data Analyst Associate)**

### Track 2 — Python Data Analyst
`3.1 → 3.2 → 3.3 → 3.4 → 3.5 → Capstone 3`
Target cert: **Microsoft DP-100** (entry) or **DataCamp Data Analyst in Python**

### Track 3 — SQL / Data Analyst (BI focus)
`4.1 → 4.2 → 5.1 → Capstone 4`
Target cert: **Microsoft DP-900** + **Oracle/PostgreSQL** associate

### Track 4 — Full Data Analyst (all tools, most complete)
`All phases → Final Capstone`
Target cert: **Google Data Analytics Certificate** + **PL-300** + **DP-900**

### Track 5 — Career-Switcher Sprint (12 weeks, employable minimum)
`1.1 → 1.2 → 2.1 → 2.2 → 4.1 → 4.2 → 3.2 → 3.4 → Capstone 2 → Capstone 4`
Skips: deep Python ML, integration phase. Add later.

---

## Roadmap Overview

```
Phase 1 — Foundations         (Weeks 1–6)
Phase 2 — Core Tools          (Weeks 7–16)
Phase 3 — Python for DA       (Weeks 17–26)   [independent of Phase 4]
Phase 4 — SQL Mastery         (Weeks 27–32)   [independent of Phase 3]
Phase 5 — Integration         (Weeks 33–36)   [requires Phases 2–4]
Capstone Projects             (Ongoing)
```

**Dependency map:**
```
1.1 ─┬─ 1.2 ── 1.3 ── 2.1 ── 2.2 ── 2.3 ─┐
     │                                    ├─ 5.2 ── 5.3
     ├─ 3.1 ── 3.2 ─┬─ 3.3 ── 3.5        │
     │              └─ 3.4 ──────────────┤
     └─ 4.1 ── 4.2 ───────────── 5.1 ────┘
```

---

## Phase 1: Foundations
### Weeks 1–6 | Goal: Build the data mindset and Excel fundamentals

---

### Module 1.1 — Data Analyst Fundamentals

> **Level:** Beginner · **Prereqs:** None · **Time:** ~3h
> **Skip if:** you can already explain the data analysis lifecycle and the difference between descriptive/diagnostic/predictive analytics.
> **Unlocks:** context for every later module. Safe to skim if you have any analytics exposure.

**What is a Data Analyst?**

A Data Analyst translates raw data into actionable business insights. Core responsibilities:
- Data collection and extraction
- Data cleaning and validation
- Exploratory analysis and summarization
- Visualization and reporting
- Communicating findings to stakeholders

**The Data Analysis Process**

```
Define Question → Collect Data → Clean Data → Analyze → Visualize → Communicate
```

**Key Concepts**
- Structured vs. unstructured data
- Quantitative vs. qualitative data
- Descriptive vs. diagnostic vs. predictive analytics
- Data types: nominal, ordinal, interval, ratio
- The difference between correlation and causation

**Tools Introduction**

| Tool | Primary Use |
|---|---|
| Excel | Data entry, formulas, basic analysis |
| Power Query | ETL — import, transform, clean |
| Power Pivot | Data modeling, DAX calculations |
| Python | Automation, statistics, ML |
| SQL | Database querying and manipulation |

**Resources**
- Google's free Data Analytics Certificate (Coursera) — audit for free
- "Storytelling with Data" by Cole Nussbaumer Knaflic (first 3 chapters)

**Exercise 1.1**
Download the Superstore Sales dataset (available free on Kaggle). Open in Excel. Answer:
1. How many rows and columns are there?
2. What data type is each column?
3. List 3 business questions this dataset could answer.

---

### Module 1.2 — Excel Fundamentals

> **Level:** Beginner · **Prereqs:** None · **Time:** ~12h
> **Skip-check (test-out):** Complete Exercise 1.2 cold. If you can do all 8 tasks, skip to Module 2.1.
> **Skip if:** you fluently use XLOOKUP/INDEX-MATCH, SUMIFS/COUNTIFS, and Pivot Tables with slicers.
> **Unlocks:** 1.3, 2.1, 2.3.

#### 1.2.1 Navigation & Structure
- Workbook vs. worksheet vs. cell
- Named ranges
- Absolute (`$A$1`), relative (`A1`), and mixed (`$A1`, `A$1`) references
- Data entry best practices: one variable per column, no merged cells in data tables

#### 1.2.2 Essential Formulas

**Lookup & Reference**
```excel
=VLOOKUP(lookup_value, table_array, col_index, FALSE)
=XLOOKUP(lookup_value, lookup_array, return_array, [not_found])
=INDEX(array, MATCH(lookup_value, lookup_array, 0))
=INDIRECT("Sheet1!A"&ROW())
```

**Logical**
```excel
=IF(condition, value_if_true, value_if_false)
=IFS(condition1, val1, condition2, val2, ...)
=AND(condition1, condition2)
=OR(condition1, condition2)
=IFERROR(formula, "Error message")
=ISBLANK(cell)
```

**Text**
```excel
=TRIM(text)           -- removes extra spaces
=CLEAN(text)          -- removes non-printable characters
=UPPER/LOWER/PROPER(text)
=LEFT(text, n)
=RIGHT(text, n)
=MID(text, start, n)
=FIND(search_text, within_text)
=SUBSTITUTE(text, old, new)
=CONCATENATE(text1, text2)  -- or =text1&" "&text2
=TEXT(value, "format")      -- e.g., =TEXT(A1,"MM/DD/YYYY")
```

**Math & Statistical**
```excel
=SUM / SUMIF / SUMIFS
=COUNT / COUNTA / COUNTIF / COUNTIFS
=AVERAGE / AVERAGEIF / AVERAGEIFS
=MAX / MIN / LARGE / SMALL
=ROUND / ROUNDUP / ROUNDDOWN
=STDEV / VAR
=PERCENTILE(array, k)
=RANK(number, ref, order)
```

**Date & Time**
```excel
=TODAY()
=NOW()
=DATE(year, month, day)
=DATEDIF(start, end, "D"/"M"/"Y")
=EOMONTH(date, months)
=WEEKDAY(date, return_type)
=YEAR / MONTH / DAY / WEEKNUM
```

#### 1.2.3 Pivot Tables
- Creating a Pivot Table from a table
- Rows, Columns, Values, Filters
- Value field settings: Sum, Count, Average, % of Total
- Grouping dates (by month, quarter, year)
- Slicers and timelines
- Calculated fields

**Pivot Table Best Practices**
- Always use structured Excel Tables (Ctrl+T) as your source — auto-expands
- Refresh pivot after data updates (Alt+F5)
- Use "Show values as" for % of grand total, running total, difference from

#### 1.2.4 Charts & Visualization
- When to use: bar, column, line, scatter, pie, combo
- Chart formatting: titles, axis labels, data labels, gridlines
- Sparklines for inline trends
- Dynamic charts using named ranges or Tables

#### 1.2.5 Data Validation & Quality in Excel
- Data Validation rules (dropdown lists, number ranges, date limits)
- Conditional Formatting for visual QC
- Remove Duplicates
- Find & Replace with wildcards
- Text to Columns

**Exercise 1.2 — Excel Sales Analysis**

Dataset: Superstore Sales (Excel)

Tasks:
1. Create a structured Table (Ctrl+T)
2. Add a `Profit Margin %` calculated column: `=Profit/Sales`
3. Use SUMIFS to calculate total sales by Region and Category
4. Use COUNTIFS to count orders where Profit < 0
5. Build a Pivot Table: Sales by Category by Year
6. Add a slicer for Region
7. Create a bar chart of top 10 products by sales
8. Use XLOOKUP to pull a customer's total orders by Customer ID

---

### Module 1.3 — Excel Tables & Structured Data

> **Level:** Beginner · **Prereqs:** 1.2 · **Time:** ~3h
> **Skip if:** you already use `Ctrl+T` Tables and structured references (`Table[Column]`) by default.
> **Unlocks:** 2.1 (Power Query ingests Tables cleanly).

- Excel Table (Ctrl+T): why it matters for data work
- Structured references: `=Table1[Sales]` vs. `=$B:$B`
- Auto-expansion behavior
- Table Design tab options
- Converting flat data vs. summary tables
- Preparing data for Power Query ingestion

**Data Layout Rules for Analysis**
```
DO:                              DON'T:
✓ One header row                 ✗ Merged cells in headers
✓ One data point per cell        ✗ Totals row inside the data
✓ Consistent data types          ✗ Mixed text and numbers in one column
✓ No blank rows within data      ✗ Multiple tables on one sheet
✓ ISO date format (YYYY-MM-DD)   ✗ Dates stored as text
```

---

## Phase 2: Core Tools
### Weeks 7–16 | Goal: Power Query, Power Pivot, and intermediate Excel

---

### Module 2.1 — Power Query (ETL in Excel)

> **Level:** Beginner–Intermediate · **Prereqs:** 1.3 · **Time:** ~14h
> **Skip-check (test-out):** Complete Exercise 2.1. If you can combine a folder of CSVs, merge a lookup, and load to the model, skip to 2.2.
> **Skip if:** you build refreshable Power Query pipelines with merge/append and basic M edits.
> **Unlocks:** 2.2, 5.2. Transferable directly to Power BI (same engine).

Power Query is Excel's built-in ETL engine. It handles data import, transformation, and loading — all without formulas, and with a reproducible, step-by-step pipeline.

#### 2.1.1 Data Sources
- Import from: Excel file, CSV, folder (multiple files), SQL Server, Web, SharePoint
- Get Data > From Folder (combine multiple CSVs automatically)
- Refreshing queries after source data updates

#### 2.1.2 The Query Editor Interface
- Applied Steps pane (every transformation is recorded)
- Column headers (data types, rename, reorder, remove)
- Filter rows
- Formula bar (M language expressions)

#### 2.1.3 Core Transformations

**Column Operations**
```
- Change Type (Text, Number, Date, Logical)
- Rename Column
- Remove Column / Keep Column
- Split Column by Delimiter, by Number of Characters
- Merge Columns
- Add Column from Examples
- Extract: First N chars, Last N chars, Text Between Delimiters
```

**Row Operations**
```
- Filter Rows (equals, contains, is null, is not null)
- Remove Duplicates
- Remove Blank Rows
- Keep / Remove Top N Rows
- Sort Ascending / Descending
```

**Transform Operations**
```
- Trim / Clean (removes whitespace and non-printable characters)
- UPPER / LOWER / Capitalize Each Word
- Replace Values
- Replace Errors
- Fill Down / Fill Up (fill null cells with nearest non-null)
- Unpivot Columns (wide → long format)
- Pivot Column (long → wide format)
- Transpose
- Group By (aggregate: sum, count, min, max, average)
```

**Date Operations**
```
- Date > Year / Month / Quarter / Week Number / Day of Week
- Duration > Total Days between dates
```

#### 2.1.4 Combining Queries

**Append Queries** — stack rows (same columns, different time periods)
```
Home > Append Queries > Two tables or More tables
Use case: Monthly sales files from Jan, Feb, Mar → combined full-year table
```

**Merge Queries** — join tables (like SQL JOIN)
```
Home > Merge Queries > Select join column + join type
Join types: Left Outer, Right Outer, Inner, Full Outer, Left Anti, Right Anti
Use case: Add product category from a product lookup table
```

#### 2.1.5 M Language Basics
```m
// Each step creates a new table variable
let
    Source = Excel.Workbook(File.Contents("sales.xlsx"), null, true),
    Sheet1 = Source{[Item="Sheet1",Kind="Sheet"]}[Data],
    PromotedHeaders = Table.PromoteHeaders(Sheet1, [PromoteAllScalars=true]),
    TypedColumns = Table.TransformColumnTypes(PromotedHeaders,{
        {"OrderDate", type date},
        {"Sales", type number},
        {"Region", type text}
    }),
    FilteredRows = Table.SelectRows(TypedColumns, each [Sales] > 0),
    AddedMargin = Table.AddColumn(FilteredRows, "Margin%", 
        each [Profit] / [Sales], Percentage.Type)
in
    AddedMargin
```

**Key M functions to know**
```m
Table.SelectRows(table, each [Column] = "Value")
Table.AddColumn(table, "NewCol", each [A] + [B])
Table.TransformColumns(table, {{"Col", Text.Upper}})
Table.Group(table, {"Category"}, {{"Total", each List.Sum([Sales]), type number}})
Table.NestedJoin(table1, "Key", table2, "Key", "NewCol", JoinKind.LeftOuter)
Text.Trim([Column])
Date.Year([DateColumn])
```

#### 2.1.6 Power Query Best Practices
- Always rename steps to be descriptive ("Remove null rows" not "Filtered Rows3")
- Disable Load for staging queries (right-click > uncheck "Enable Load")
- Use `Table.Buffer()` on frequently referenced tables
- Never hardcode file paths — use parameters instead
- Document transformations in query descriptions

**Exercise 2.1 — Power Query Sales ETL**

Dataset: 12 monthly CSV files of sales data (create or download)

Tasks:
1. Combine all 12 CSVs using Get Data > From Folder
2. Promote headers and set correct data types
3. Remove blank rows and duplicates
4. Add a `Year` and `Month` column from the Order Date
5. Merge with a product lookup table to add Category and Subcategory
6. Add a calculated column: `Revenue = Quantity * Unit Price`
7. Group by Category to get total Revenue per Category
8. Load the final clean table to the Excel data model

---

### Module 2.2 — Power Pivot & Data Modeling

> **Level:** Intermediate · **Prereqs:** 2.1 · **Time:** ~18h
> **Skip-check (test-out):** Complete Exercise 2.2. If you can build a star schema and write CALCULATE + time-intelligence measures, skip to 2.3 or Phase 3.
> **Skip if:** you write DAX measures (CALCULATE, SAMEPERIODLASTYEAR, TOTALYTD) and understand filter context.
> **Unlocks:** Capstone 2, Power BI PL-300 prep. **This is the highest-leverage Excel-track module for certification.**

Power Pivot extends Excel with a columnar in-memory database (xVelocity engine) and the DAX formula language. This is the foundation of modern Excel BI.

#### 2.2.1 The Data Model
- What is a data model: multiple tables connected by relationships
- Star schema vs. snowflake schema
- Fact tables vs. dimension tables

**Star Schema (standard pattern)**
```
                  dim_Product
                      |
dim_Date ── fact_Sales ── dim_Customer
                      |
                  dim_Region
```

- **Fact table**: transactional data — Sales, Orders, Payments
- **Dimension tables**: descriptive context — Products, Customers, Dates, Regions

#### 2.2.2 Relationships
- One-to-many (most common): one Product → many Sales rows
- Cross-filter direction: Single vs. Both
- Creating relationships in Diagram View
- Active vs. inactive relationships
- **Never** use VLOOKUP between tables once you're in the data model — use relationships instead

#### 2.2.3 DAX — Data Analysis Expressions

**DAX Concepts**
- **Calculated Columns**: row-by-row computation, stored in the model
- **Measures**: aggregation computed at query time, respects filter context
- **Filter Context**: the active filters from slicers, pivot rows/columns
- **Row Context**: the current row being evaluated (in calculated columns and iterators)

**DAX Syntax Structure**
```dax
Measure Name = FUNCTION(arguments)
```

**Basic Aggregation Measures**
```dax
Total Sales = SUM(fact_Sales[Revenue])
Total Orders = COUNTROWS(fact_Sales)
Avg Order Value = AVERAGE(fact_Sales[Revenue])
Unique Customers = DISTINCTCOUNT(fact_Sales[CustomerID])
Max Sale = MAX(fact_Sales[Revenue])
```

**Logical Functions**
```dax
Profitable Orders = 
    CALCULATE(
        COUNTROWS(fact_Sales),
        fact_Sales[Profit] > 0
    )
```

**CALCULATE** — the most important DAX function
```dax
-- CALCULATE modifies filter context
Sales in East = CALCULATE([Total Sales], dim_Region[Region] = "East")

Sales Excluding Furniture = 
    CALCULATE([Total Sales], dim_Product[Category] <> "Furniture")

-- ALL() removes all filters
Sales All Time = CALCULATE([Total Sales], ALL(dim_Date))
```

**Time Intelligence**
```dax
-- Requires a proper Date dimension table with contiguous dates
Sales LY = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(dim_Date[Date]))

Sales YTD = TOTALYTD([Total Sales], dim_Date[Date])

Sales MTD = TOTALMTD([Total Sales], dim_Date[Date])

YoY Growth % = 
    DIVIDE([Total Sales] - [Sales LY], [Sales LY], BLANK())

Rolling 3M Sales = 
    CALCULATE([Total Sales], DATESINPERIOD(dim_Date[Date], LASTDATE(dim_Date[Date]), -3, MONTH))
```

**Iterator Functions (X functions)**
```dax
-- SUMX evaluates an expression per row, then sums
Total Revenue = SUMX(fact_Sales, fact_Sales[Quantity] * fact_Sales[UnitPrice])

-- AVERAGEX
Avg Profit Per Order = AVERAGEX(fact_Sales, fact_Sales[Profit])

-- RANKX
Product Sales Rank = RANKX(ALL(dim_Product), [Total Sales],, DESC, Dense)
```

**Filter Functions**
```dax
-- FILTER returns a table
Top 10 Products = 
    CALCULATE([Total Sales], TOPN(10, dim_Product, [Total Sales], DESC))

-- RELATED pulls from related dimension
Category Sales = CALCULATE([Total Sales], RELATED(dim_Product[Category]))

-- VALUES returns distinct values in current filter context
Categories In View = CONCATENATEX(VALUES(dim_Product[Category]), dim_Product[Category], ", ")
```

#### 2.2.4 Date Dimension Table
A proper date dimension is mandatory for time intelligence.

```dax
-- Create in Power Query (M)
let
    StartDate = #date(2020, 1, 1),
    EndDate = #date(2025, 12, 31),
    DateList = List.Dates(StartDate, Duration.Days(EndDate - StartDate) + 1, #duration(1,0,0,0)),
    DateTable = Table.FromList(DateList, Splitter.SplitByNothing(), {"Date"}),
    TypedDate = Table.TransformColumnTypes(DateTable, {{"Date", type date}}),
    AddYear    = Table.AddColumn(TypedDate, "Year", each Date.Year([Date]), Int64.Type),
    AddMonth   = Table.AddColumn(AddYear, "MonthNo", each Date.Month([Date]), Int64.Type),
    AddMonthName = Table.AddColumn(AddMonth, "MonthName", each Date.ToText([Date], "MMMM"), type text),
    AddQtr     = Table.AddColumn(AddMonthName, "Quarter", each "Q" & Text.From(Date.QuarterOfYear([Date])), type text),
    AddWkNo    = Table.AddColumn(AddQtr, "WeekNo", each Date.WeekOfYear([Date]), Int64.Type),
    AddDayName = Table.AddColumn(AddWkNo, "DayName", each Date.ToText([Date], "dddd"), type text),
    AddIsWeekend = Table.AddColumn(AddDayName, "IsWeekend", 
        each Date.DayOfWeek([Date], Day.Monday) >= 5, type logical)
in
    AddIsWeekend
```

#### 2.2.5 Power Pivot KPI Dashboard — Design Pattern
```
Data Model:
  fact_Sales  ── dim_Product
             ── dim_Customer
             ── dim_Date (mark as Date Table)
             ── dim_Region

Key Measures:
  [Total Sales]        -- base measure
  [Total Cost]         -- base measure
  [Gross Profit]       -- = [Total Sales] - [Total Cost]
  [Profit Margin %]    -- = DIVIDE([Gross Profit], [Total Sales])
  [Sales LY]           -- time intelligence
  [YoY Growth %]       -- = DIVIDE([Total Sales] - [Sales LY], [Sales LY])
  [Sales YTD]          -- running year total
  [Avg Transaction]    -- = DIVIDE([Total Sales], [Total Orders])
```

**Exercise 2.2 — Power Pivot Sales Data Model**

Dataset: Superstore Sales (multi-table version)

Tasks:
1. Load fact_Sales, dim_Product, dim_Customer, dim_Region, dim_Date into Power Pivot
2. Build the star schema with correct relationships
3. Mark dim_Date as Date Table
4. Write these measures: Total Sales, Total Orders, Profit Margin %, Sales LY, YoY Growth %, Sales YTD
5. Build a Pivot Table with: Year on columns, Category on rows, Total Sales as value
6. Add slicers for Region and Category
7. Add a KPI: flag if Profit Margin % is below 15%

---

### Module 2.3 — Advanced Excel Analytics

> **Level:** Intermediate · **Prereqs:** 1.2 · **Time:** ~8h
> **Skip if:** you use dynamic arrays (FILTER/SORT/UNIQUE), statistical functions, and What-If analysis.
> **Unlocks:** Capstone 2. **Optional** — can be done any time after 1.2; not required for Phase 3+.

#### 2.3.1 Dynamic Arrays (Excel 365)
```excel
=UNIQUE(range)              -- unique values from a range
=SORT(range, col, order)    -- sorted array
=FILTER(range, condition)   -- filtered rows
=SORTBY(range, by_range)    -- sort by another column
=SEQUENCE(rows, cols, start, step)
=RANDARRAY(rows, cols)

-- Example: Top 5 products by sales
=TAKE(SORT(product_sales, 2, -1), 5)

-- Example: Filter orders with profit < 0
=FILTER(orders_table, orders_table[Profit] < 0)
```

#### 2.3.2 Statistical Functions for Analysts
```excel
=CORREL(array1, array2)          -- correlation coefficient
=FORECAST.LINEAR(x, known_y, known_x)
=TREND(known_y, known_x, new_x)
=STDEV.S / STDEV.P
=VAR.S / VAR.P
=NORM.DIST(x, mean, stdev, cumulative)
=CONFIDENCE.NORM(alpha, stdev, n)
=QUARTILE(array, quart)          -- Q1, Q2, Q3
=PERCENTRANK.INC(array, x)
```

#### 2.3.3 What-If Analysis
- Goal Seek: reverse-solve for input given desired output
- Scenario Manager: compare multiple input scenarios
- Data Table (1-variable and 2-variable): sensitivity analysis grid

**Exercise 2.3 — Advanced Analysis**

Dataset: Superstore Sales

Tasks:
1. Use FILTER + SORT to build a dynamic "Top 10 Customers by Profit" table
2. Use CORREL to find the correlation between Discount and Profit
3. Use FORECAST.LINEAR to project next 3 months of sales
4. Build a 2-variable Data Table: profit at different Discount rates × Sales volumes

---

### Phase 2 Capstone: Excel + Power Query + Power Pivot Dashboard

**Project: Retail Sales Performance Dashboard**

**Dataset:** Superstore Sales (Kaggle) — multi-year, multi-region, multi-category

**Deliverable:** A single Excel workbook with:
1. A Power Query pipeline that cleans and loads the raw data
2. A star schema data model in Power Pivot (fact + 4 dimensions)
3. A Date dimension created in Power Query
4. The following measures in Power Pivot:
   - Total Sales, Total Profit, Profit Margin %
   - YoY Sales Growth %, Sales YTD, Rolling 12-Month Sales
   - Top Category by Sales (using RANKX)
5. An interactive dashboard sheet with:
   - KPI cards (Total Sales, Profit, Orders, Margin %)
   - Monthly sales trend line chart
   - Sales by Category bar chart
   - Top 10 Products table
   - Regional performance map or filled map chart
   - Slicers: Year, Region, Category
6. A documentation sheet describing your data model and DAX measures

---

## Phase 3: Python for Data Analysis
### Weeks 17–26 | Goal: End-to-end data work in Python

---

### Module 3.1 — Python Basics for Analysts

> **Level:** Beginner · **Prereqs:** None (separate track) · **Time:** ~12h
> **Skip-check (test-out):** Write a function that reads a CSV, filters rows, and returns a summary dict. If trivial, skip to 3.2.
> **Skip if:** you know Python syntax — functions, loops, comprehensions, dicts — and basic file I/O.
> **Unlocks:** 3.2, 3.3, 3.4, 3.5.

This module covers only what's relevant to data work — not general software engineering.

#### 3.1.1 Setup
```bash
# Recommended setup
python -m venv da-env
source da-env/bin/activate  # Windows: da-env\Scripts\activate
pip install pandas numpy matplotlib seaborn scipy scikit-learn jupyter

# Launch Jupyter
jupyter lab
```

#### 3.1.2 Python Fundamentals
```python
# Data types
x = 42          # int
y = 3.14        # float
s = "hello"     # str
b = True        # bool
n = None        # NoneType

# Collections
lst = [1, 2, 3]               # list — mutable, ordered
tpl = (1, 2, 3)               # tuple — immutable
dct = {"key": "value"}        # dict — key-value pairs
st  = {1, 2, 3}               # set — unique values

# Control flow
for item in lst:
    print(item)

if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")

# List comprehension (Pythonic pattern)
squares = [x**2 for x in range(10)]
evens   = [x for x in range(20) if x % 2 == 0]

# Functions
def calculate_margin(sales, cost):
    """Returns gross profit margin as a decimal."""
    if sales == 0:
        return 0
    return (sales - cost) / sales

# Lambda
margin_fn = lambda s, c: (s - c) / s if s != 0 else 0
```

#### 3.1.3 File I/O
```python
import pandas as pd

# Read
df = pd.read_csv("sales.csv")
df = pd.read_excel("sales.xlsx", sheet_name="Sheet1")
df = pd.read_json("sales.json")

# Write
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False, sheet_name="Results")

# Read with options
df = pd.read_csv("sales.csv",
    parse_dates=["OrderDate"],
    dtype={"PostalCode": str},
    encoding="utf-8",
    na_values=["N/A", "null", "-"]
)
```

---

### Module 3.2 — Pandas: Data Cleaning & Manipulation

> **Level:** Beginner–Intermediate · **Prereqs:** 3.1 · **Time:** ~20h
> **Skip-check (test-out):** Complete Exercise 3.2. If you can audit nulls, fix dtypes, engineer features, groupby-aggregate, and merge, skip to 3.3/3.4.
> **Skip if:** Pandas is already your daily driver for tabular work.
> **Unlocks:** 3.3, 3.4, 3.5, 5.1. **Core dependency for the entire Python track.**

Pandas is the primary Python library for tabular data. Master this before anything else.

#### 3.2.1 DataFrame Fundamentals
```python
import pandas as pd
import numpy as np

df = pd.read_csv("sales.csv", parse_dates=["OrderDate"])

# Inspection
df.shape           # (rows, cols)
df.dtypes          # column data types
df.info()          # full summary: dtypes + null counts
df.describe()      # statistical summary of numeric columns
df.head(5)         # first 5 rows
df.tail(5)         # last 5 rows
df.sample(5)       # random 5 rows
df.columns.tolist()
df["Category"].unique()
df["Category"].value_counts()
df["Category"].nunique()
```

#### 3.2.2 Selecting Data
```python
# Column selection
df["Sales"]              # single column → Series
df[["Sales", "Profit"]]  # multiple columns → DataFrame

# Row selection by index
df.iloc[0]               # first row
df.iloc[0:5]             # first 5 rows
df.iloc[0:5, 2:4]        # rows 0–4, columns 2–3

# Row selection by label
df.loc[0, "Sales"]
df.loc[0:5, ["Sales", "Profit"]]

# Boolean filtering
df[df["Profit"] < 0]
df[(df["Category"] == "Furniture") & (df["Profit"] < 0)]
df[df["Region"].isin(["East", "West"])]
df[df["ProductName"].str.contains("Chair", case=False)]

# query() method (readable alternative)
df.query("Profit < 0 and Category == 'Furniture'")
df.query("Sales > @threshold")  # use @ to reference Python variables
```

#### 3.2.3 Data Cleaning
```python
# ── Null Handling ──────────────────────────────────────────────────────────
df.isnull().sum()               # null count per column
df.isnull().sum() / len(df)     # null % per column

df.dropna()                     # drop rows with any null
df.dropna(subset=["Sales"])     # drop rows where Sales is null
df.dropna(how="all")            # drop rows that are entirely null
df.dropna(thresh=5)             # keep rows with at least 5 non-null values

df["PostalCode"].fillna("Unknown", inplace=True)
df["Sales"].fillna(df["Sales"].median(), inplace=True)
df["Sales"].fillna(method="ffill", inplace=True)    # forward fill

# ── Duplicates ────────────────────────────────────────────────────────────
df.duplicated().sum()
df.duplicated(subset=["OrderID"]).sum()
df.drop_duplicates(inplace=True)
df.drop_duplicates(subset=["OrderID"], keep="first", inplace=True)

# ── Data Types ────────────────────────────────────────────────────────────
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Category"] = df["Category"].astype("category")
df["OrderID"] = df["OrderID"].astype(str)

# ── String Cleaning ───────────────────────────────────────────────────────
df["CustomerName"] = df["CustomerName"].str.strip()
df["CustomerName"] = df["CustomerName"].str.title()
df["City"] = df["City"].str.upper()
df["ProductName"] = df["ProductName"].str.replace(r"\s+", " ", regex=True)

# Extract parts of strings
df["FirstName"] = df["CustomerName"].str.split(" ").str[0]
df["Domain"] = df["Email"].str.extract(r"@(.+)$")

# ── Outlier Detection ─────────────────────────────────────────────────────
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df["Sales"] < lower) | (df["Sales"] > upper)]
df_clean = df[(df["Sales"] >= lower) & (df["Sales"] <= upper)]

# ── Renaming & Reordering ─────────────────────────────────────────────────
df.rename(columns={"Row ID": "row_id", "Order ID": "order_id"}, inplace=True)
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Reorder columns
cols = ["order_id", "order_date", "customer_name", "sales", "profit"]
df = df[cols]
```

#### 3.2.4 Feature Engineering
```python
# ── Date Features ─────────────────────────────────────────────────────────
df["year"]     = df["order_date"].dt.year
df["month"]    = df["order_date"].dt.month
df["month_name"] = df["order_date"].dt.strftime("%B")
df["quarter"]  = df["order_date"].dt.quarter
df["day_name"] = df["order_date"].dt.day_name()
df["week_no"]  = df["order_date"].dt.isocalendar().week
df["days_to_ship"] = (df["ship_date"] - df["order_date"]).dt.days

# ── Derived Metrics ───────────────────────────────────────────────────────
df["profit_margin"] = df["profit"] / df["sales"]
df["revenue"]       = df["quantity"] * df["unit_price"]
df["discount_amount"] = df["sales"] * df["discount"]

# ── Binning / Categorization ──────────────────────────────────────────────
df["sales_tier"] = pd.cut(df["sales"],
    bins=[0, 100, 500, 1000, float("inf")],
    labels=["Low", "Medium", "High", "Premium"]
)

df["profit_flag"] = np.where(df["profit"] >= 0, "Profitable", "Loss")

# ── Encoding Categorical Variables ───────────────────────────────────────
df_dummies = pd.get_dummies(df, columns=["region", "category"], drop_first=True)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["region_encoded"] = le.fit_transform(df["region"])
```

#### 3.2.5 GroupBy & Aggregation
```python
# Basic groupby
df.groupby("category")["sales"].sum()
df.groupby(["category", "region"])["sales"].sum()

# Multiple aggregations
summary = df.groupby("category").agg(
    total_sales=("sales", "sum"),
    total_profit=("profit", "sum"),
    avg_margin=("profit_margin", "mean"),
    order_count=("order_id", "count"),
    unique_customers=("customer_id", "nunique")
).reset_index()

# Named aggregation with custom functions
df.groupby("category").agg(
    sales_q3=("sales", lambda x: x.quantile(0.75))
)

# Transform: add group-level aggregate back to row level
df["category_total_sales"] = df.groupby("category")["sales"].transform("sum")
df["pct_of_category"]      = df["sales"] / df["category_total_sales"]

# Pivot table equivalent
df.pivot_table(
    values="sales",
    index="category",
    columns="region",
    aggfunc="sum",
    fill_value=0,
    margins=True
)
```

#### 3.2.6 Merging & Joining
```python
# Merge (SQL JOIN equivalent)
merged = pd.merge(df_orders, df_products, on="product_id", how="left")
merged = pd.merge(df_orders, df_customers, left_on="customer_id", right_on="cust_id", how="inner")

# Merge validation
pd.merge(df1, df2, on="id", how="left", validate="m:1")  # catches bad joins

# Concatenate (stack rows)
df_all = pd.concat([df_2022, df_2023, df_2024], ignore_index=True)
df_all = pd.concat([df_2022, df_2023], axis=0, ignore_index=True)

# Check for unmatched keys after left join
merged[merged["product_name"].isnull()]  # rows from left with no match
```

**Exercise 3.2 — Python Data Cleaning**

Dataset: Superstore Sales CSV (with intentional dirty data)

Tasks:
1. Load the CSV and run a full null/dtype audit
2. Fix all date columns to datetime type
3. Standardize all text columns: strip, titlecase, remove extra spaces
4. Remove duplicate orders (by OrderID)
5. Add calculated columns: `profit_margin`, `days_to_ship`, `quarter`, `sales_tier`
6. Detect and flag outliers in `sales` using IQR method
7. Create a summary table: total sales, profit, order count, avg margin by category
8. Export clean dataset to CSV and Excel

---

### Module 3.3 — Statistics for Data Analysts

> **Level:** Intermediate · **Prereqs:** 3.2 · **Time:** ~14h
> **Skip if:** you confidently run and interpret t-tests, ANOVA, chi-square, and correlation, and know Type I/II error.
> **Unlocks:** 3.5 (ML rests on these foundations). Can be studied alongside 3.4.

#### 3.3.1 Descriptive Statistics
```python
import numpy as np
from scipy import stats
import pandas as pd

sales = df["sales"]

# Central tendency
mean   = sales.mean()
median = sales.median()
mode   = sales.mode()[0]

# Spread
std    = sales.std()
var    = sales.var()
rng    = sales.max() - sales.min()
iqr    = sales.quantile(0.75) - sales.quantile(0.25)

# Shape
skewness = sales.skew()      # >0 right-skewed, <0 left-skewed
kurtosis = sales.kurtosis()  # >0 heavy tails, <0 light tails

# Percentiles
p25, p50, p75, p90, p95 = np.percentile(sales.dropna(), [25, 50, 75, 90, 95])

print(f"Mean: {mean:.2f} | Median: {median:.2f} | Std: {std:.2f}")
print(f"Skewness: {skewness:.3f} | Kurtosis: {kurtosis:.3f}")
```

#### 3.3.2 Distributions
```python
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Visualize distribution
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].hist(df["sales"], bins=50, edgecolor="black")
axes[0].set_title("Histogram")

stats.probplot(df["sales"], dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot")

axes[2].boxplot(df["sales"])
axes[2].set_title("Box Plot")
plt.tight_layout()
plt.show()

# Test for normality
stat, p = stats.shapiro(df["sales"].sample(50))
print(f"Shapiro-Wilk: stat={stat:.4f}, p={p:.4f}")
# p < 0.05 → reject H0 (not normally distributed)
```

#### 3.3.3 Correlation & Relationships
```python
# Pearson correlation (linear, continuous)
r, p = stats.pearsonr(df["discount"], df["profit"])
print(f"Pearson r: {r:.3f}, p-value: {p:.4f}")

# Spearman correlation (monotonic, robust to outliers)
rho, p = stats.spearmanr(df["discount"], df["profit"])

# Full correlation matrix
corr_matrix = df[["sales", "profit", "discount", "quantity"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()
```

#### 3.3.4 Hypothesis Testing
```python
from scipy import stats

# Two-sample t-test: Is sales different between East and West?
east  = df[df["region"] == "East"]["sales"]
west  = df[df["region"] == "West"]["sales"]
t_stat, p_value = stats.ttest_ind(east, west)
print(f"t={t_stat:.3f}, p={p_value:.4f}")
print("Significant difference" if p_value < 0.05 else "No significant difference")

# ANOVA: Is profit different across all 4 regions?
groups = [df[df["region"] == r]["profit"] for r in df["region"].unique()]
f_stat, p_value = stats.f_oneway(*groups)
print(f"ANOVA: F={f_stat:.3f}, p={p_value:.4f}")

# Chi-square: Is there an association between Category and Region?
contingency = pd.crosstab(df["category"], df["region"])
chi2, p, dof, expected = stats.chi2_contingency(contingency)
print(f"Chi2={chi2:.3f}, p={p:.4f}, dof={dof}")
```

#### 3.3.5 Key Statistical Concepts

| Concept | Definition | Practical Use |
|---|---|---|
| Central Limit Theorem | Sample means are normally distributed for large n | Justifies using t-tests even on non-normal data |
| p-value | Probability of results given null hypothesis is true | p < 0.05 = statistically significant |
| Confidence Interval | Range likely to contain true population parameter | 95% CI: "we're 95% confident the mean falls here" |
| Effect Size | Magnitude of difference (Cohen's d) | Statistical significance ≠ practical importance |
| Type I Error | False positive (rejecting true H0) | alpha = 0.05 means 5% chance of false positive |
| Type II Error | False negative (failing to reject false H0) | Controlled by statistical power |

---

### Module 3.4 — EDA: Exploratory Data Analysis

> **Level:** Intermediate · **Prereqs:** 3.2 · **Time:** ~12h
> **Skip-check (test-out):** Complete Exercise 3.4 — full 6-step EDA with 5 documented findings.
> **Skip if:** you have a repeatable EDA workflow and produce univariate/bivariate/multivariate visuals fluently.
> **Unlocks:** Capstone 3. Pairs naturally with 3.3.

EDA is a systematic approach to understanding a new dataset before modeling. The goal is to generate hypotheses, not prove them.

#### 3.4.1 EDA Framework
```
1. Understand the data structure (shape, types, source)
2. Check data quality (nulls, duplicates, outliers, format issues)
3. Univariate analysis (each column independently)
4. Bivariate analysis (column pairs, relationships)
5. Multivariate analysis (3+ variables together)
6. Business insight extraction (summarize what you found)
```

#### 3.4.2 Automated EDA
```python
# ydata-profiling generates a full HTML report
from ydata_profiling import ProfileReport

profile = ProfileReport(df, title="Sales EDA Report", explorative=True)
profile.to_file("eda_report.html")
```

#### 3.4.3 Manual EDA with Matplotlib & Seaborn

**Univariate Plots**
```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("Sales Data — Univariate Analysis", fontsize=16)

# Histogram
axes[0,0].hist(df["sales"], bins=40, color="steelblue", edgecolor="white")
axes[0,0].set_title("Sales Distribution")

# Box plot
sns.boxplot(y=df["profit"], ax=axes[0,1], color="salmon")
axes[0,1].set_title("Profit Distribution")

# Count plot (categorical)
sns.countplot(data=df, x="category", ax=axes[0,2], palette="Set2")
axes[0,2].set_title("Orders by Category")

# KDE plot
df["profit_margin"].plot.kde(ax=axes[1,0], color="green")
axes[1,0].set_title("Profit Margin Density")

# Pie chart (use sparingly)
df["category"].value_counts().plot.pie(ax=axes[1,1], autopct="%1.1f%%")
axes[1,1].set_title("Category Share")

plt.tight_layout()
plt.savefig("univariate_eda.png", dpi=150, bbox_inches="tight")
plt.show()
```

**Bivariate Plots**
```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Scatter: Sales vs. Profit
sns.scatterplot(data=df, x="sales", y="profit", hue="category", ax=axes[0,0], alpha=0.6)
axes[0,0].set_title("Sales vs. Profit by Category")

# Box by group: Sales by Region
sns.boxplot(data=df, x="region", y="sales", ax=axes[0,1], palette="Set3")
axes[0,1].set_title("Sales Distribution by Region")

# Line: Sales trend over time
monthly = df.groupby(df["order_date"].dt.to_period("M"))["sales"].sum()
monthly.plot(ax=axes[1,0], color="navy", linewidth=2)
axes[1,0].set_title("Monthly Sales Trend")

# Heatmap: Avg Sales by Category x Region
pivot = df.pivot_table(values="sales", index="category", columns="region", aggfunc="mean")
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="Blues", ax=axes[1,1])
axes[1,1].set_title("Avg Sales: Category × Region")

plt.tight_layout()
plt.show()
```

**Multivariate: Pair Plot**
```python
numeric_cols = ["sales", "profit", "discount", "quantity"]
sns.pairplot(df[numeric_cols + ["category"]], hue="category", diag_kind="kde")
plt.suptitle("Pairplot — Numeric Features", y=1.02)
plt.show()
```

#### 3.4.4 EDA Findings Template
```markdown
## EDA Summary: [Dataset Name]

### Dataset Overview
- Rows: X | Columns: Y
- Date range: YYYY-MM to YYYY-MM
- Key entities: [list]

### Data Quality Issues Found
- [Issue 1]: [Count affected rows] — [Action taken]
- [Issue 2]: ...

### Key Findings

**Finding 1:** [Category] drives [X%] of revenue but only [Y%] of orders
- Evidence: [chart / stat]
- Business implication: [...]

**Finding 2:** Discount rate above [X%] is associated with negative profit
- Evidence: Pearson r = [X], p = [Y]
- Business implication: [...]

**Finding 3:** [Region] shows declining sales over the last 6 months
- Evidence: [MoM trend]
- Business implication: [...]

### Hypotheses for Further Testing
1. ...
2. ...
```

**Exercise 3.4 — Full EDA**

Dataset: Superstore Sales

Tasks:
1. Conduct full EDA following the 6-step framework
2. Produce all univariate and bivariate plots
3. Identify and document at least 5 data quality issues
4. Write 5 business findings with evidence
5. State 3 hypotheses you would test with more data or modeling

---

### Module 3.5 — Machine Learning & Data Science Basics

> **Level:** Intermediate · **Prereqs:** 3.2, 3.3 · **Time:** ~18h
> **Skip-check (test-out):** Complete Exercise 3.5 — train+evaluate a regressor, a classifier, run K-Means, and forecast.
> **Skip if:** you build and evaluate scikit-learn models and know the regression/classification metric families.
> **Unlocks:** Capstone 3, DP-100 prep. **Optional for pure BI/analyst roles; required for DS-leaning roles.**

This module focuses on the techniques most relevant to business data analysts — not deep learning or research ML.

#### 3.5.1 ML Concepts

**Types of ML**

| Type | Goal | Examples |
|---|---|---|
| Supervised — Regression | Predict a number | Sales forecasting, price prediction |
| Supervised — Classification | Predict a category | Churn prediction, fraud detection |
| Unsupervised — Clustering | Find natural groups | Customer segmentation |
| Time Series | Forecast over time | Inventory demand forecasting |

**The ML Workflow**
```
1. Define problem and target variable
2. Prepare data (clean, encode, scale)
3. Split: train / test (typically 80/20)
4. Train model
5. Evaluate performance
6. Interpret and communicate results
```

#### 3.5.2 ML Setup with Scikit-learn
```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import (mean_absolute_error, mean_squared_error,
                              r2_score, classification_report,
                              confusion_matrix, accuracy_score)
import numpy as np
```

#### 3.5.3 Regression: Predicting Sales

**Linear Regression**
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd

# Feature engineering
features = ["quantity", "discount", "region_encoded", "category_encoded"]
target   = "sales"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"R²:  {r2_score(y_test, y_pred):.4f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")

# Coefficients
coef_df = pd.DataFrame({
    "feature": features,
    "coefficient": model.coef_
}).sort_values("coefficient", key=abs, ascending=False)
print(coef_df)
```

**Random Forest Regressor**
```python
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print(f"RF R²:  {r2_score(y_test, y_pred_rf):.4f}")
print(f"RF MAE: {mean_absolute_error(y_test, y_pred_rf):.2f}")

# Feature importance
feat_importance = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=False)
feat_importance.plot.bar(title="Feature Importance", figsize=(8, 4))
```

#### 3.5.4 Classification: Predicting Profitable Orders

```python
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

# Target: 1 = profitable, 0 = loss
df["is_profitable"] = (df["profit"] > 0).astype(int)

features = ["sales", "quantity", "discount", "region_encoded", "category_encoded"]
target   = "is_profitable"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
    random_state=42, stratify=y)

# Logistic Regression
lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
print(classification_report(y_test, y_pred_lr))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred_lr)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Loss", "Profit"], yticklabels=["Loss", "Profit"])
plt.title("Confusion Matrix")
plt.show()

# Gradient Boosting (better performance)
gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
gb.fit(X_train, y_train)
print(f"GB Accuracy: {accuracy_score(y_test, gb.predict(X_test)):.4f}")
```

**Classification Metrics Explained**

| Metric | Formula | When to Prioritize |
|---|---|---|
| Accuracy | Correct / Total | Balanced classes |
| Precision | TP / (TP+FP) | Cost of false positives is high |
| Recall | TP / (TP+FN) | Cost of false negatives is high |
| F1-Score | 2*(P*R)/(P+R) | Imbalanced classes |
| AUC-ROC | Area under ROC curve | Probabilistic ranking quality |

#### 3.5.5 Clustering: Customer Segmentation

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Build customer-level features
customer_summary = df.groupby("customer_id").agg(
    total_sales   = ("sales", "sum"),
    order_count   = ("order_id", "count"),
    avg_order_val = ("sales", "mean"),
    profit_total  = ("profit", "sum"),
    avg_discount  = ("discount", "mean")
).reset_index()

features = ["total_sales", "order_count", "avg_order_val", "avg_discount"]
X = customer_summary[features]

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow method to find optimal k
inertias = []
k_range = range(2, 11)
for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.plot(k_range, inertias, "bo-")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()

# Fit with optimal k (e.g., k=4)
km = KMeans(n_clusters=4, random_state=42, n_init=10)
customer_summary["segment"] = km.fit_predict(X_scaled)

# Profile segments
segment_profile = customer_summary.groupby("segment")[features].mean().round(2)
print(segment_profile)
```

#### 3.5.6 Time Series Forecasting (Basic)

```python
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

# Aggregate to monthly
monthly = (df.groupby(df["order_date"].dt.to_period("M"))["sales"]
             .sum()
             .reset_index()
             .rename(columns={"order_date": "period", "sales": "total_sales"}))
monthly["period_int"] = range(len(monthly))

# Features: time index, seasonal indicators
monthly["month"] = monthly["period"].dt.month
monthly["sin_month"] = np.sin(2 * np.pi * monthly["month"] / 12)
monthly["cos_month"] = np.cos(2 * np.pi * monthly["month"] / 12)

features = ["period_int", "sin_month", "cos_month"]
X = monthly[features]
y = monthly["total_sales"]

# Train on all history, forecast next 6 months
model = LinearRegression()
model.fit(X, y)

future_periods = range(len(monthly), len(monthly) + 6)
future_df = pd.DataFrame({
    "period_int": future_periods,
    "month": [(p % 12) + 1 for p in future_periods],
})
future_df["sin_month"] = np.sin(2 * np.pi * future_df["month"] / 12)
future_df["cos_month"] = np.cos(2 * np.pi * future_df["month"] / 12)

forecast = model.predict(future_df[features])
print("6-Month Forecast:", forecast.round(0))
```

**Exercise 3.5 — ML Workflow**

Dataset: Superstore Sales

Tasks:
1. Train a Linear Regression model to predict `Sales` from order features
2. Train a Gradient Boosting Classifier to predict `is_profitable`
3. Evaluate both models with appropriate metrics
4. Segment customers into 4 groups using K-Means
5. Profile each customer segment with business labels (e.g., "High Value", "At Risk")
6. Produce a monthly sales forecast for the next 6 months

---

### Phase 3 Capstone: Python EDA + ML Report

**Project: Sales & Inventory Analytics in Python**

**Dataset:** Superstore Sales + a synthetic Inventory dataset (stock levels, reorder points, supplier lead times)

**Deliverables:**
1. Jupyter Notebook with full EDA (all 6 steps)
2. Data quality report (null analysis, outlier flags, DQ issues)
3. Regression model: predict `Sales` — compare Linear Regression vs. Random Forest
4. Classification model: predict `is_profitable` — compare Logistic Regression vs. Gradient Boosting
5. Clustering: 4-segment customer analysis with business labels
6. 6-month sales forecast per product category
7. Inventory reorder alert: flag products where current stock < reorder point + lead-time demand
8. Final summary: 5 business recommendations backed by data

---

## Phase 4: SQL Mastery
### Weeks 27–32 | Goal: Production-grade querying, ETL support, and data modeling

---

### Module 4.1 — SQL Fundamentals

> **Level:** Beginner · **Prereqs:** None (separate track) · **Time:** ~14h
> **Skip-check (test-out):** Write a 3-table JOIN with GROUP BY, HAVING, and a CASE expression. If easy, skip to 4.2.
> **Skip if:** you write multi-table JOINs, aggregations, and subqueries comfortably.
> **Unlocks:** 4.2, 5.1. **Highest ROI for analyst job interviews** — most live tests are SQL.

#### 4.1.1 Setup
```bash
# PostgreSQL (recommended)
# Install: postgresql.org or via Docker
docker run --name pg-da -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres

# GUI: DBeaver (free), pgAdmin, TablePlus
# Online practice: sqlfiddle.com, db-fiddle.com, PostgreSQL on Supabase (free tier)
```

#### 4.1.2 Core SQL — SELECT
```sql
-- Basic SELECT
SELECT order_id, customer_name, sales, profit
FROM   orders
WHERE  profit < 0
ORDER  BY sales DESC
LIMIT  10;

-- Aliases
SELECT
    o.order_id,
    c.customer_name,
    o.sales,
    o.profit,
    o.profit / o.sales AS profit_margin
FROM   orders  o
JOIN   customers c ON o.customer_id = c.customer_id
WHERE  o.order_date >= '2023-01-01';

-- DISTINCT
SELECT DISTINCT region, category FROM orders;

-- Wildcards
SELECT * FROM products WHERE product_name LIKE '%Chair%';
SELECT * FROM customers WHERE email LIKE '%@gmail.com';

-- NULL handling
SELECT * FROM orders WHERE ship_date IS NULL;
SELECT order_id, COALESCE(discount, 0) AS discount FROM orders;
```

#### 4.1.3 Filtering & Conditions
```sql
-- Comparison operators
WHERE sales > 500
WHERE profit BETWEEN -100 AND 0
WHERE order_date BETWEEN '2023-01-01' AND '2023-12-31'
WHERE region IN ('East', 'West')
WHERE region NOT IN ('Central')

-- Compound conditions
WHERE profit < 0 AND category = 'Furniture'
WHERE region = 'East' OR region = 'West'
WHERE NOT (category = 'Technology')

-- CASE WHEN
SELECT
    order_id,
    sales,
    CASE
        WHEN sales >= 1000 THEN 'Premium'
        WHEN sales >= 500  THEN 'High'
        WHEN sales >= 100  THEN 'Medium'
        ELSE 'Low'
    END AS sales_tier
FROM orders;
```

#### 4.1.4 Aggregation & GROUP BY
```sql
-- Basic aggregation
SELECT
    category,
    COUNT(*)                        AS total_orders,
    SUM(sales)                      AS total_sales,
    SUM(profit)                     AS total_profit,
    AVG(profit / NULLIF(sales, 0))  AS avg_margin,
    MIN(sales)                      AS min_sale,
    MAX(sales)                      AS max_sale
FROM   orders
GROUP  BY category
ORDER  BY total_sales DESC;

-- HAVING (filter after aggregation)
SELECT
    customer_id,
    COUNT(*)     AS order_count,
    SUM(sales)   AS lifetime_value
FROM   orders
GROUP  BY customer_id
HAVING SUM(sales) > 5000
ORDER  BY lifetime_value DESC;

-- GROUP BY ROLLUP (subtotals + grand total)
SELECT
    COALESCE(region, 'ALL REGIONS')     AS region,
    COALESCE(category, 'ALL CATEGORIES') AS category,
    SUM(sales)                           AS total_sales
FROM   orders
GROUP  BY ROLLUP(region, category)
ORDER  BY region, category;
```

#### 4.1.5 JOINs
```sql
-- INNER JOIN: only matching rows
SELECT o.order_id, o.sales, p.product_name, p.category
FROM   orders o
INNER JOIN products p ON o.product_id = p.product_id;

-- LEFT JOIN: all left rows, nulls where no match
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS order_count
FROM   customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY order_count DESC NULLS LAST;

-- Multiple joins
SELECT
    o.order_id,
    o.order_date,
    c.customer_name,
    p.product_name,
    p.category,
    r.region_name,
    o.sales,
    o.profit
FROM   orders       o
JOIN   customers    c ON o.customer_id   = c.customer_id
JOIN   products     p ON o.product_id    = p.product_id
JOIN   regions      r ON o.region_id     = r.region_id;

-- Self join: compare rows within same table
SELECT
    a.order_id,
    a.customer_id,
    a.order_date,
    b.order_date AS prev_order_date
FROM   orders a
JOIN   orders b
    ON  a.customer_id = b.customer_id
    AND b.order_date  = (
        SELECT MAX(order_date)
        FROM orders
        WHERE customer_id = a.customer_id
          AND order_date   < a.order_date
    );
```

---

### Module 4.2 — Intermediate SQL

> **Level:** Intermediate · **Prereqs:** 4.1 · **Time:** ~16h
> **Skip-check (test-out):** Complete Exercise 4.2. If you can write window functions, CTEs, and SQL profiling queries, skip to Phase 5.
> **Skip if:** window functions (ROW_NUMBER, LAG, running totals) and chained CTEs are second nature.
> **Unlocks:** Capstone 4, 5.1. **Window functions are the #1 SQL interview differentiator.**

#### 4.2.1 Window Functions

Window functions are the single most powerful tool in analytical SQL. They compute aggregates over a "window" of rows without collapsing the result set.

```sql
-- Syntax
function() OVER (
    PARTITION BY column    -- reset per group (optional)
    ORDER BY column        -- order within window (required for running calcs)
    ROWS/RANGE BETWEEN ... -- frame (optional)
)

-- ROW_NUMBER, RANK, DENSE_RANK
SELECT
    order_id,
    customer_id,
    sales,
    ROW_NUMBER()  OVER (PARTITION BY customer_id ORDER BY sales DESC) AS row_num,
    RANK()        OVER (PARTITION BY customer_id ORDER BY sales DESC) AS rnk,
    DENSE_RANK()  OVER (PARTITION BY customer_id ORDER BY sales DESC) AS dense_rnk
FROM orders;

-- Running totals and moving averages
SELECT
    order_date,
    sales,
    SUM(sales)  OVER (ORDER BY order_date) AS running_total,
    AVG(sales)  OVER (ORDER BY order_date
                      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_7d_avg
FROM orders;

-- LAG / LEAD: compare to previous or next row
SELECT
    order_date,
    sales,
    LAG(sales, 1, 0)  OVER (ORDER BY order_date) AS prev_sales,
    sales - LAG(sales, 1, 0) OVER (ORDER BY order_date) AS sales_change,
    LEAD(sales, 1, 0) OVER (ORDER BY order_date) AS next_sales
FROM (
    SELECT DATE_TRUNC('month', order_date) AS order_date,
           SUM(sales) AS sales
    FROM orders
    GROUP BY 1
) monthly;

-- FIRST_VALUE / LAST_VALUE / NTH_VALUE
SELECT
    customer_id,
    order_id,
    order_date,
    sales,
    FIRST_VALUE(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS first_order,
    LAST_VALUE(sales)       OVER (PARTITION BY customer_id ORDER BY order_date
                                  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_sale
FROM orders;

-- NTILE: divide into quartiles
SELECT
    customer_id,
    SUM(sales) AS total_sales,
    NTILE(4) OVER (ORDER BY SUM(sales) DESC) AS sales_quartile
FROM orders
GROUP BY customer_id;

-- PERCENT_RANK and CUME_DIST
SELECT
    product_id,
    SUM(sales)                                 AS product_sales,
    PERCENT_RANK() OVER (ORDER BY SUM(sales))  AS pct_rank,
    CUME_DIST()    OVER (ORDER BY SUM(sales))  AS cumulative_dist
FROM orders
GROUP BY product_id;
```

#### 4.2.2 CTEs (Common Table Expressions)
```sql
-- Basic CTE
WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', order_date) AS month,
        SUM(sales)   AS total_sales,
        SUM(profit)  AS total_profit
    FROM   orders
    GROUP  BY 1
)
SELECT
    month,
    total_sales,
    total_profit,
    total_sales - LAG(total_sales) OVER (ORDER BY month) AS mom_change
FROM monthly_sales
ORDER BY month;

-- Chained CTEs
WITH
customer_orders AS (
    SELECT
        customer_id,
        COUNT(*)    AS order_count,
        SUM(sales)  AS lifetime_value
    FROM   orders
    GROUP  BY customer_id
),
customer_segments AS (
    SELECT
        customer_id,
        order_count,
        lifetime_value,
        NTILE(4) OVER (ORDER BY lifetime_value DESC) AS value_quartile
    FROM customer_orders
)
SELECT
    value_quartile,
    COUNT(*)             AS customer_count,
    AVG(lifetime_value)  AS avg_ltv,
    SUM(lifetime_value)  AS total_revenue
FROM customer_segments
GROUP BY value_quartile
ORDER BY value_quartile;
```

#### 4.2.3 Subqueries
```sql
-- Scalar subquery
SELECT
    order_id,
    sales,
    (SELECT AVG(sales) FROM orders) AS overall_avg,
    sales - (SELECT AVG(sales) FROM orders) AS diff_from_avg
FROM orders;

-- Correlated subquery (references outer query)
SELECT
    customer_id,
    customer_name,
    (SELECT SUM(sales)
     FROM orders o
     WHERE o.customer_id = c.customer_id) AS total_spent
FROM customers c;

-- EXISTS
SELECT customer_id, customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
      AND o.profit < 0
);

-- IN with subquery
SELECT * FROM products
WHERE product_id IN (
    SELECT product_id
    FROM orders
    WHERE sales > 1000
);
```

#### 4.2.4 Date Functions (PostgreSQL)
```sql
-- Date truncation and extraction
SELECT
    order_date,
    DATE_TRUNC('month',   order_date) AS month_start,
    DATE_TRUNC('quarter', order_date) AS quarter_start,
    DATE_TRUNC('year',    order_date) AS year_start,
    EXTRACT(YEAR    FROM order_date)  AS year,
    EXTRACT(MONTH   FROM order_date)  AS month,
    EXTRACT(QUARTER FROM order_date)  AS quarter,
    EXTRACT(DOW     FROM order_date)  AS day_of_week,  -- 0=Sunday
    TO_CHAR(order_date, 'Mon YYYY')   AS month_label
FROM orders;

-- Date arithmetic
SELECT
    order_id,
    order_date,
    ship_date,
    ship_date - order_date               AS days_to_ship,
    order_date + INTERVAL '30 days'      AS due_date,
    CURRENT_DATE - order_date            AS days_since_order
FROM orders;

-- Date filtering
WHERE order_date >= DATE_TRUNC('year', CURRENT_DATE)         -- YTD
WHERE order_date >= DATE_TRUNC('month', CURRENT_DATE)        -- MTD
WHERE order_date >= CURRENT_DATE - INTERVAL '90 days'        -- last 90 days
WHERE EXTRACT(MONTH FROM order_date) = EXTRACT(MONTH FROM CURRENT_DATE)  -- this month
```

#### 4.2.5 Data Profiling in SQL
```sql
-- Null audit
SELECT
    COUNT(*)                                                   AS total_rows,
    SUM(CASE WHEN customer_id IS NULL THEN 1 ELSE 0 END)      AS null_customer_id,
    SUM(CASE WHEN order_date IS NULL THEN 1 ELSE 0 END)       AS null_order_date,
    SUM(CASE WHEN sales IS NULL THEN 1 ELSE 0 END)            AS null_sales,
    SUM(CASE WHEN profit IS NULL THEN 1 ELSE 0 END)           AS null_profit
FROM orders;

-- Duplicate check
SELECT order_id, COUNT(*) AS dup_count
FROM   orders
GROUP  BY order_id
HAVING COUNT(*) > 1;

-- Value distribution
SELECT
    category,
    COUNT(*)                   AS row_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS pct_of_total
FROM orders
GROUP BY category
ORDER BY row_count DESC;

-- Outlier detection using IQR
WITH stats AS (
    SELECT
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY sales) AS q1,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY sales) AS q3
    FROM orders
),
bounds AS (
    SELECT
        q1 - 1.5 * (q3 - q1) AS lower_bound,
        q3 + 1.5 * (q3 - q1) AS upper_bound
    FROM stats
)
SELECT o.*
FROM orders o, bounds b
WHERE o.sales < b.lower_bound OR o.sales > b.upper_bound;
```

**Exercise 4.2 — SQL Analytics Queries**

Dataset: Load Superstore Sales into PostgreSQL

Write queries to answer:
1. Monthly sales trend with MoM growth % (use LAG + window function)
2. Top 5 customers by lifetime value, with their order count and avg order value
3. Products where profit margin < 0, ranked by total loss amount
4. Customer cohort: first purchase month and total orders per cohort (CTE + window)
5. Running inventory balance by product (start stock + receipts - shipments)
6. Find customers who placed orders in 2023 but not in 2024 (EXISTS / EXCEPT)
7. Sales YTD vs same period last year by category (date functions + CASE)
8. Identify orders shipped more than 5 days after order date (date arithmetic)

---

### Phase 4 Capstone: SQL Business Intelligence Queries

**Project: SQL-Driven Sales & Inventory Intelligence**

**Setup:** Load Superstore Sales + Inventory dataset into PostgreSQL

**Deliverables (all in SQL):**

1. **Data Quality Audit Query** — null counts, duplicate checks, outlier flags for all key tables
2. **Sales Performance Dashboard Queries:**
   - Monthly sales with MoM and YoY growth
   - Sales by Category × Region (pivot using CASE WHEN)
   - Top 10 products by revenue and profit
   - Bottom 10 products by profit margin
3. **Customer Analytics Queries:**
   - Customer lifetime value segmentation (NTILE quartiles)
   - Customer retention: active vs. churned (no orders in last 90 days)
   - Average days between orders per customer
4. **Inventory Intelligence Queries:**
   - Current stock vs. reorder point per product
   - Estimated days of stock remaining (stock / avg daily sales)
   - Products with no orders in the last 60 days (dead stock)
5. **Views:** Create 3 reusable SQL views for reporting
6. **Documentation:** SQL comments explaining each query's business purpose

---

## Phase 5: Integration
### Weeks 33–36 | Goal: Connect all tools into an end-to-end workflow

---

### Module 5.1 — Python + SQL Integration

> **Level:** Intermediate · **Prereqs:** 3.2, 4.1 · **Time:** ~6h
> **Skip if:** you already read/write between Pandas and a SQL database via SQLAlchemy.
> **Unlocks:** 5.2, Final Capstone.

```python
import pandas as pd
from sqlalchemy import create_engine, text

# Connect to PostgreSQL
engine = create_engine("postgresql://user:password@localhost:5432/sales_db")

# Read SQL into DataFrame
df = pd.read_sql("SELECT * FROM orders WHERE order_date >= '2023-01-01'", engine)

# Write DataFrame to database
df_clean.to_sql("orders_clean", engine, if_exists="replace", index=False, chunksize=1000)

# Parameterized query
region = "East"
df = pd.read_sql(
    text("SELECT * FROM orders WHERE region = :region"),
    engine,
    params={"region": region}
)
```

### Module 5.2 — End-to-End Pipeline Pattern

> **Level:** Intermediate · **Prereqs:** Phases 2–4 · **Time:** ~6h
> **Skip if:** you have shipped a raw-to-dashboard pipeline end to end.
> **Unlocks:** Final Capstone, portfolio.

```
Raw CSV Files
    ↓ Power Query (clean, standardize, combine)
Excel Data Model
    ↓ Export to PostgreSQL via Python
SQL Database
    ↓ Python EDA & ML analysis
Jupyter Notebook (findings + models)
    ↓ Power BI / Excel Dashboard
Business Dashboard (stakeholder-ready)
```

### Module 5.3 — Analyst Portfolio Setup

> **Level:** All · **Prereqs:** Any completed capstone · **Time:** ~4h
> **Do this once you have ≥1 capstone done — regardless of which track.** Portfolio matters more than certificates to most employers.

**Essential portfolio components:**
- GitHub repository with at least 3 projects
- Each project: README with business context, methods, findings
- Jupyter notebooks with clean markdown explanations
- SQL scripts with comments
- Power BI or Excel dashboard screenshots

**README Template for DA Projects**
```markdown
## Project: [Title]

**Business Question:** [One sentence]

**Dataset:** [Name, source, size, date range]

**Tools Used:** Python (Pandas, Scikit-learn), SQL (PostgreSQL), Excel/Power BI

**Key Findings:**
1. [Finding with metric]
2. [Finding with metric]
3. [Finding with metric]

**Methods:** EDA → Data Cleaning → [Analysis type] → [Model/Dashboard]

**Files:**
- `notebook.ipynb` — full analysis
- `queries.sql` — SQL analytics queries
- `dashboard.pbix` — Power BI dashboard

**How to Run:** [brief instructions]
```

---

## Final Capstone: End-to-End Sales & Inventory Analytics Project

### Project Brief

**Business Context:**
You are a Data Analyst at a mid-size retail company. Management needs a complete analysis of sales performance and inventory health to make decisions for the upcoming quarter.

**Datasets:**
- Superstore Sales (orders, customers, products, regions)
- Inventory data (stock levels, reorder points, supplier lead times, receipts)

---

### Deliverable 1: Data Pipeline (Power Query + Python)

- Ingest raw CSVs via Power Query and Python
- Document all transformation steps
- Load clean data into PostgreSQL

### Deliverable 2: SQL Analytics Layer

Write and document SQL for:
- Sales performance: revenue, profit, YoY growth, top/bottom performers
- Customer analytics: LTV segmentation, retention, cohort analysis
- Inventory health: stock levels, reorder alerts, dead stock identification

### Deliverable 3: Python EDA & ML

- Full 6-step EDA with all visualizations
- Profit prediction model (regression — Gradient Boosting)
- Profitability classification model (Logistic Regression vs. GBM)
- Customer segmentation (K-Means, 4 segments with business labels)
- Demand forecast: 3-month forecast per category

### Deliverable 4: Excel + Power Pivot Dashboard

- Star schema data model: fact_Sales + 4 dimensions
- 8 DAX measures including time intelligence (YoY, YTD, Rolling 12M)
- Interactive dashboard with slicers for Year, Region, Category

### Deliverable 5: Insights Presentation

A 10-slide summary covering:
1. Executive summary (3 key findings)
2. Sales performance overview
3. Top/bottom product analysis
4. Customer segmentation findings
5. Inventory risk summary
6. Demand forecast
7. Business recommendations (min 5, each backed by data)
8. Methodology and data quality notes

---

## Quick Reference: Tool-Task Matrix

| Task | Excel | Power Query | Power Pivot (DAX) | Python | SQL |
|---|:---:|:---:|:---:|:---:|:---:|
| Import CSV files | ✓ | ✓✓ | | ✓✓ | ✓ |
| Clean & standardize data | ✓ | ✓✓ | | ✓✓ | ✓✓ |
| Combine multiple files | | ✓✓ | | ✓✓ | ✓✓ |
| Pivot / aggregate | ✓✓ | ✓ | ✓✓ | ✓✓ | ✓✓ |
| Time intelligence (YTD, YoY) | ✓ | | ✓✓ | ✓ | ✓✓ |
| Statistical analysis | ✓ | | | ✓✓ | ✓ |
| Machine learning | | | | ✓✓ | |
| Interactive dashboards | ✓✓ | | ✓✓ | | |
| Large datasets (1M+ rows) | | ✓ | ✓✓ | ✓✓ | ✓✓ |
| Ad hoc querying | | | | ✓ | ✓✓ |
| Data profiling / DQ audit | ✓ | ✓ | | ✓✓ | ✓✓ |
| Reproducible pipeline | | ✓✓ | | ✓✓ | ✓✓ |

---

## Certification Roadmap

Certifications are **optional** — a strong portfolio (Module 5.3) usually outweighs them — but recognized credentials help with ATS screening, career switches, and markets/employers that filter on them. Below is what each major certification covers, which modules prepare you, and the official exam requirements.

> **Honest guidance:** For most analyst roles, prioritize in this order: (1) portfolio projects, (2) SQL fluency, (3) one BI tool cert (PL-300 or Tableau), (4) a foundations cert (DP-900) for résumé signaling. Don't collect certificates for their own sake.

---

### Tier 1 — Entry / Foundational

#### Google Data Analytics Professional Certificate
- **Provider:** Google (via Coursera) · **Cost:** Coursera subscription (~$49/mo, ~3–6 months) · **Prerequisites:** None
- **Format:** 8 self-paced courses + hands-on labs; no proctored exam — completion-based
- **Covers:** Data lifecycle, spreadsheets, SQL basics, R, Tableau, data cleaning, basic analysis
- **This guide prepares you via:** 1.1, 1.2, 4.1, 3.4 (note: Google cert uses **R**, not Python — this guide uses Python; the concepts transfer)
- **Best for:** Complete beginners and career switchers who want a structured, recognized starting credential
- **Recognition:** High brand recognition; entry-level. Not a deep technical filter.

#### Microsoft Certified: Azure Data Fundamentals (DP-900)
- **Provider:** Microsoft · **Cost:** ~$99 USD exam fee · **Prerequisites:** None
- **Format:** Proctored exam, ~40–60 questions, ~45–60 min, pass mark 700/1000
- **Covers:** Core data concepts, relational vs. non-relational data, analytics workloads on Azure
- **This guide prepares you via:** 1.1, 4.1 (relational concepts), 2.2 (analytics/modeling concepts)
- **Best for:** Résumé signaling, foundation before PL-300 or DP-100
- **Recognition:** Strong in Microsoft-shop employers; widely recognized globally

---

### Tier 2 — Core Analyst (the ones that matter most)

#### Microsoft Certified: Power BI Data Analyst Associate (PL-300)
- **Provider:** Microsoft · **Cost:** ~$165 USD exam fee · **Prerequisites:** None official; DP-900 recommended
- **Format:** Proctored, ~40–60 questions incl. case studies, ~100 min, pass mark 700/1000
- **Exam domains:**
  - Prepare the data (~25–30%) — **this guide: Module 2.1 Power Query**
  - Model the data (~25–30%) — **this guide: Module 2.2 Power Pivot/DAX, star schema, date dimension**
  - Visualize & analyze (~25–30%) — **this guide: Capstone 2 dashboard work** (supplement with Power BI Desktop practice)
  - Deploy & maintain (~15–20%) — **supplement:** Power BI Service (workspaces, refresh, RLS) — not fully covered here
- **This guide prepares you via:** 2.1, 2.2, 2.3, Capstone 2 (covers ~70–80%)
- **Gap to close independently:** Power BI Desktop visuals + Power BI Service deployment. The Power Query and DAX skills transfer **directly** — they are the same engine.
- **Best for:** The single most employable analyst cert in Microsoft-heavy markets (incl. Philippines/SEA)
- **Official prep:** Microsoft Learn PL-300 learning path (free)

#### Tableau Desktop Specialist
- **Provider:** Tableau (Salesforce) · **Cost:** ~$100 USD · **Prerequisites:** None · **No expiration** (Specialist tier)
- **Format:** ~45 questions, ~60 min, pass mark ~750/1000
- **Covers:** Connecting to data, building visualizations, calculations, dashboards, Tableau-specific functions
- **This guide prepares you via:** Visualization concepts in 3.4 and Capstone 2 transfer; **Tableau tool itself is not taught here** — pair with Tableau Public (free)
- **Best for:** Markets/employers standardized on Tableau rather than Power BI
- **Recognition:** Industry standard for the Tableau ecosystem

---

### Tier 3 — Specialist / Advanced

#### Microsoft Certified: Azure Data Scientist Associate (DP-100)
- **Provider:** Microsoft · **Cost:** ~$165 USD · **Prerequisites:** DP-900 recommended; Python + ML fundamentals expected
- **Format:** Proctored, case studies + questions, ~100–120 min
- **Covers:** ML experiment design, model training/tuning, deployment on Azure ML
- **This guide prepares you via:** 3.2, 3.3, 3.5 (ML foundations + scikit-learn). **Gap:** Azure ML Studio platform specifics — study independently
- **Best for:** Analysts moving toward data science / ML engineering roles
- **Recognition:** Strong, but more than most analyst roles require

#### Databricks / Snowflake / dbt Certifications
- **Databricks Certified Data Analyst Associate** — SQL + Lakehouse analytics; ~$200; for modern data-stack roles
- **SnowPro Core (Snowflake)** — cloud data warehouse; ~$175; high demand in data-engineering-adjacent analyst roles
- **dbt Analytics Engineering Certification** — SQL-based transformation; ~$200; for analytics engineering track
- **This guide prepares you via:** Module 4.1, 4.2 (SQL is the foundation for all three). Platform-specific features studied separately.
- **Best for:** Analysts targeting modern data-stack companies; pursue **after** core SQL mastery

#### Oracle Database SQL Certified Associate (1Z0-071)
- **Provider:** Oracle · **Cost:** ~$245 USD · **Format:** ~78 questions, proctored
- **Covers:** SQL querying, DDL/DML, joins, subqueries, functions (Oracle SQL dialect)
- **This guide prepares you via:** 4.1, 4.2 (this guide uses PostgreSQL; ~90% of SQL transfers; Oracle dialect differences are minor)
- **Best for:** Enterprises running Oracle databases

---

### Certification-to-Module Map

| Certification | Tier | Modules That Prepare You | Coverage | Independent Study Needed |
|---|---|---|---|---|
| Google Data Analytics | 1 | 1.1, 1.2, 4.1, 3.4 | ~70% | R language, Tableau basics |
| DP-900 (Data Fundamentals) | 1 | 1.1, 2.2, 4.1 | ~75% | Azure-specific services |
| PL-300 (Power BI) | 2 | 2.1, 2.2, 2.3, Capstone 2 | ~75% | Power BI Service, RLS, visuals |
| Tableau Desktop Specialist | 2 | 3.4, Capstone 2 (concepts) | ~40% | Tableau tool (use Tableau Public) |
| DP-100 (Data Scientist) | 3 | 3.2, 3.3, 3.5 | ~60% | Azure ML platform |
| SnowPro / Databricks / dbt | 3 | 4.1, 4.2 | ~50% | Platform-specific features |
| Oracle SQL Associate | 3 | 4.1, 4.2 | ~85% | Oracle dialect specifics |

---

### Recommended Certification Sequence by Track

```
EXCEL/BI TRACK:     DP-900 → PL-300                (foundation → flagship)
PYTHON/DS TRACK:    DP-900 → DP-100                (foundation → specialist)
SQL/DATA TRACK:     DP-900 → Oracle SQL or SnowPro (foundation → platform)
GENERALIST:         Google Cert → PL-300 → DP-900  (recognized starter → BI → signaling)
```

> **Cost-conscious path:** Microsoft Learn provides **free** official prep for all Microsoft exams. Tableau Public and PostgreSQL are free. You can prepare for every certification above using free official materials + this guide; only the exam fees are unavoidable. Watch for Microsoft's periodic **free exam vouchers** (via Microsoft events, Virtual Training Days).

---

## Learning Resources Master List

### Free Resources

| Resource | Tool | URL |
|---|---|---|
| ExcelJet | Excel | exceljet.net |
| Microsoft Learn | Power Query / Power BI | learn.microsoft.com |
| SQLBI — DAX Guide | DAX / Power Pivot | dax.guide |
| SQLZoo | SQL | sqlzoo.net |
| Mode SQL Tutorial | SQL | mode.com/sql-tutorial |
| LeetCode SQL | SQL | leetcode.com/problemset/database |
| Python for Everybody | Python | coursera.org (audit free) |
| Kaggle Learn | Python / Pandas / ML | kaggle.com/learn |
| ydata-profiling docs | Python EDA | docs.profiling.ydata.ai |
| Pandas documentation | Python | pandas.pydata.org/docs |
| Scikit-learn User Guide | Python ML | scikit-learn.org/stable/user_guide |
| Real Python | Python | realpython.com |

### Free Certification Prep Resources

| Resource | Certification | URL |
|---|---|---|
| Microsoft Learn — PL-300 path | PL-300 (Power BI) | learn.microsoft.com/training |
| Microsoft Learn — DP-900 path | DP-900 (Fundamentals) | learn.microsoft.com/training |
| Microsoft Learn — DP-100 path | DP-100 (Data Scientist) | learn.microsoft.com/training |
| Tableau Public | Tableau Desktop Specialist | public.tableau.com |
| Tableau eLearning (free tier) | Tableau Desktop Specialist | tableau.com/learn/training |
| Google Data Analytics (audit) | Google DA Certificate | coursera.org |
| Oracle SQL practice (Live SQL) | Oracle 1Z0-071 | livesql.oracle.com |
| Microsoft Virtual Training Days | Free exam vouchers | microsoft.com/en-us/trainingdays |

### Recommended Datasets (All Free on Kaggle)

| Dataset | Primary Use |
|---|---|
| Superstore Sales | Sales analytics, EDA, ML |
| Brazilian E-Commerce (Olist) | SQL joins, customer analytics |
| Online Retail II (UCI) | RFM analysis, cohort analysis |
| AdventureWorks | SQL server, full business schema |
| Northwind (SQLite) | Classic OLTP schema practice |

### Books (Optional but High-Impact)

| Book | Focus |
|---|---|
| *Storytelling with Data* — Knaflic | Data visualization |
| *Python for Data Analysis* — McKinney | Pandas deep dive |
| *Practical Statistics for Data Scientists* — Bruce | Applied statistics |
| *The Data Warehouse Toolkit* — Kimball | Dimensional modeling |
| *SQL for Data Analysis* — Cathy Tanimura | Advanced SQL patterns |

---

## Progress Tracker

> Mark each module: `[ ]` not started · `[~]` in progress · `[x]` done · `[S]` skipped (tested out). Skipping is success when you can pass the exercise — track it, don't hide it.

```
PHASE 1 — FOUNDATIONS
[ ] Module 1.1  Data Analyst Fundamentals
[ ] Module 1.2  Excel Fundamentals
[ ] Module 1.3  Excel Tables & Structured Data
[ ] Exercise 1.1  Dataset exploration
[ ] Exercise 1.2  Excel Sales Analysis

PHASE 2 — CORE TOOLS
[ ] Module 2.1  Power Query
[ ] Module 2.2  Power Pivot & DAX
[ ] Module 2.3  Advanced Excel Analytics
[ ] Exercise 2.1  Power Query ETL
[ ] Exercise 2.2  Power Pivot Data Model
[ ] Exercise 2.3  Advanced Analysis
[ ] CAPSTONE 2   Retail Sales Performance Dashboard

PHASE 3 — PYTHON  [independent track — can start any time]
[ ] Module 3.1  Python Basics
[ ] Module 3.2  Pandas — Cleaning & Manipulation
[ ] Module 3.3  Statistics for Analysts
[ ] Module 3.4  EDA Framework
[ ] Module 3.5  ML & Data Science Basics
[ ] Exercise 3.2  Python Data Cleaning
[ ] Exercise 3.4  Full EDA
[ ] Exercise 3.5  ML Workflow
[ ] CAPSTONE 3   Python EDA + ML Report

PHASE 4 — SQL  [independent track — can start any time]
[ ] Module 4.1  SQL Fundamentals
[ ] Module 4.2  Intermediate SQL (Window Functions, CTEs)
[ ] Exercise 4.2  SQL Analytics Queries
[ ] CAPSTONE 4   SQL BI Queries

PHASE 5 — INTEGRATION  [requires Phases 2–4]
[ ] Module 5.1  Python + SQL Integration
[ ] Module 5.2  End-to-End Pipeline
[ ] Module 5.3  Portfolio Setup
[ ] FINAL CAPSTONE  End-to-End Sales & Inventory Project
```

### Certification Tracker (Optional)

```
[ ] DP-900   Azure Data Fundamentals       — after 1.1, 2.2, 4.1
[ ] PL-300   Power BI Data Analyst          — after Phase 2 + Capstone 2
[ ] Tableau  Desktop Specialist             — after 3.4 + Tableau Public practice
[ ] DP-100   Azure Data Scientist           — after 3.2, 3.3, 3.5
[ ] Google   Data Analytics Certificate     — parallel, any time
[ ] SQL Cert Oracle 1Z0-071 / SnowPro Core  — after Phase 4
```

---

*Guide Version 2.0 — Data Analyst Track: Beginner to Intermediate*
*Non-linear modular design · Placement quiz · Certification roadmap*
*Target: 36 weeks part-time (8–12 hrs/week) or 18 weeks full-time — or any subset via Learning Tracks*
