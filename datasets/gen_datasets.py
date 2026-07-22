import numpy as np
import pandas as pd
from datetime import datetime, timedelta

rng = np.random.default_rng(42)
BASE = "/Volumes/1TB_SSD/projects-mvp-ext/learning-guides/datasets"

# ============================================================
# 1. SUPERSTORE SALES  (data-analyst guide)
# ============================================================
n = 2000
regions = ["East", "West", "Central", "South"]
states_by_region = {
    "East": ["New York", "Pennsylvania", "New Jersey", "Massachusetts"],
    "West": ["California", "Washington", "Oregon", "Arizona"],
    "Central": ["Texas", "Illinois", "Ohio", "Michigan"],
    "South": ["Florida", "Georgia", "North Carolina", "Tennessee"],
}
cities_by_state = {
    "New York": ["New York City", "Buffalo"], "Pennsylvania": ["Philadelphia", "Pittsburgh"],
    "New Jersey": ["Newark", "Jersey City"], "Massachusetts": ["Boston", "Worcester"],
    "California": ["Los Angeles", "San Francisco", "San Diego"], "Washington": ["Seattle", "Spokane"],
    "Oregon": ["Portland", "Eugene"], "Arizona": ["Phoenix", "Tucson"],
    "Texas": ["Houston", "Dallas", "Austin"], "Illinois": ["Chicago", "Springfield"],
    "Ohio": ["Columbus", "Cleveland"], "Michigan": ["Detroit", "Ann Arbor"],
    "Florida": ["Miami", "Orlando", "Tampa"], "Georgia": ["Atlanta", "Savannah"],
    "North Carolina": ["Charlotte", "Raleigh"], "Tennessee": ["Nashville", "Memphis"],
}
segments = ["Consumer", "Corporate", "Home Office"]
ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]
categories = {
    "Furniture": ["Bookcases", "Chairs", "Tables", "Furnishings"],
    "Office Supplies": ["Binders", "Paper", "Storage", "Art", "Labels"],
    "Technology": ["Phones", "Machines", "Accessories", "Copiers"],
}
product_names = {
    "Bookcases": ["Sauder Bookcase", "Bush Cubix Bookcase", "O'Sullivan Bookcase"],
    "Chairs": ["Global Task Chair", "HON Executive Chair", "Hbada Office Chair"],
    "Tables": ["Bretford Conference Table", "Chromcraft Round Table", "Bush Somerset Table"],
    "Furnishings": ["Eldon Desk Lamp", "Tenex Chairmat", "Advantus Task Lamp"],
    "Binders": ["Avery Binder", "GBC Binding System", "Wilson Jones Binder"],
    "Paper": ["Xerox Paper Ream", "HP Paper Ream", "Boise Paper"],
    "Storage": ["Fellowes Storage Box", "SimpleHouseware Bin", "Iris File Box"],
    "Art": ["Newell Highlighters", "Bic Pens", "Sharpie Markers"],
    "Labels": ["Avery Labels", "Hon Label Maker Tape"],
    "Phones": ["Apple iPhone", "Samsung Galaxy", "Cisco IP Phone"],
    "Machines": ["Zebra Label Printer", "Cubify 3D Printer", "Lexmark Printer"],
    "Accessories": ["Logitech Mouse", "Kensington Keyboard", "SanDisk Flash Drive"],
    "Copiers": ["Canon Copier", "Hewlett Packard Copier"],
}
customer_first = ["Aaron","Alice","Brian","Carla","Derek","Elena","Frank","Grace","Henry","Ivy",
                  "Jack","Karen","Leo","Maria","Nathan","Olivia","Paul","Quinn","Rita","Sam"]
customer_last = ["Bennett","Chavez","Diaz","Evans","Foster","Garcia","Hughes","Irwin","Johnson",
                  "Kim","Lopez","Moore","Nguyen","Ortiz","Parker","Quintana","Reed","Silva","Turner","Ward"]

order_dates = pd.date_range("2023-01-01", "2025-12-31", freq="D")
rows = []
n_customers = 120
cust_ids = [f"CU-{10000+i}" for i in range(n_customers)]
cust_names = [f"{rng.choice(customer_first)} {rng.choice(customer_last)}" for _ in range(n_customers)]
cust_segment = {cid: rng.choice(segments) for cid in cust_ids}
cust_region = {cid: rng.choice(regions) for cid in cust_ids}

for i in range(n):
    order_id = f"US-{2023 + i // 700}-{100000 + i}"
    order_date = pd.Timestamp(rng.choice(order_dates))
    ship_delay = rng.integers(1, 8)
    ship_date = pd.Timestamp(order_date) + timedelta(days=int(ship_delay))
    cust_idx = rng.integers(0, n_customers)
    customer_id = cust_ids[cust_idx]
    customer_name = cust_names[cust_idx]
    segment = cust_segment[customer_id]
    region = cust_region[customer_id]
    state = rng.choice(states_by_region[region])
    city = rng.choice(cities_by_state[state])
    category = rng.choice(list(categories.keys()), p=[0.22, 0.5, 0.28])
    sub_category = rng.choice(categories[category])
    product_name = rng.choice(product_names[sub_category])
    product_id = f"{category[:3].upper()}-{sub_category[:2].upper()}-{1000+i%400}"
    quantity = int(rng.integers(1, 14))
    base_price = {"Furniture": 250, "Office Supplies": 25, "Technology": 400}[category]
    unit_price = round(base_price * rng.uniform(0.5, 2.2), 2)
    discount = rng.choice([0, 0, 0, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5], p=[0.35,0.1,0.1,0.15,0.1,0.08,0.06,0.04,0.02])
    sales = round(unit_price * quantity * (1 - discount), 2)
    margin_rate = {"Furniture": 0.05, "Office Supplies": 0.22, "Technology": 0.12}[category]
    profit = round(sales * (margin_rate + rng.uniform(-0.15, 0.15)), 2)
    rows.append({
        "Order ID": order_id, "Order Date": order_date.strftime("%Y-%m-%d"),
        "Ship Date": ship_date.strftime("%Y-%m-%d"), "Ship Mode": rng.choice(ship_modes),
        "Customer ID": customer_id, "Customer Name": customer_name, "Segment": segment,
        "Country": "United States", "City": city, "State": state,
        "Postal Code": int(rng.integers(10000, 99999)), "Region": region,
        "Product ID": product_id, "Category": category, "Sub-Category": sub_category,
        "Product Name": product_name, "Sales": sales, "Quantity": quantity,
        "Discount": discount, "Profit": profit,
    })

superstore = pd.DataFrame(rows)
superstore.to_csv(f"{BASE}/superstore-sales/superstore_sales.csv", index=False)

# Star-schema version for Power Pivot / DAX exercises
fact_sales = superstore[["Order ID", "Order Date", "Customer ID", "Product ID", "Sales", "Quantity", "Discount", "Profit"]].copy()
fact_sales.insert(0, "Sales Key", range(1, len(fact_sales) + 1))

dim_product = superstore[["Product ID", "Product Name", "Category", "Sub-Category"]].drop_duplicates(subset=["Product ID"]).reset_index(drop=True)
dim_customer = superstore[["Customer ID", "Customer Name", "Segment"]].drop_duplicates(subset=["Customer ID"]).reset_index(drop=True)
dim_region = superstore[["Region", "State", "City", "Country"]].drop_duplicates().reset_index(drop=True)
dim_region.insert(0, "Region Key", range(1, len(dim_region) + 1))

date_min, date_max = pd.to_datetime(superstore["Order Date"]).min(), pd.to_datetime(superstore["Order Date"]).max()
dim_date = pd.DataFrame({"Date": pd.date_range(date_min, date_max, freq="D")})
dim_date["Year"] = dim_date["Date"].dt.year
dim_date["Quarter"] = "Q" + dim_date["Date"].dt.quarter.astype(str)
dim_date["Month"] = dim_date["Date"].dt.strftime("%B")
dim_date["Month Number"] = dim_date["Date"].dt.month
dim_date["Day of Week"] = dim_date["Date"].dt.strftime("%A")
dim_date["Date"] = dim_date["Date"].dt.strftime("%Y-%m-%d")

fact_sales.to_csv(f"{BASE}/superstore-sales/fact_Sales.csv", index=False)
dim_product.to_csv(f"{BASE}/superstore-sales/dim_Product.csv", index=False)
dim_customer.to_csv(f"{BASE}/superstore-sales/dim_Customer.csv", index=False)
dim_region.to_csv(f"{BASE}/superstore-sales/dim_Region.csv", index=False)
dim_date.to_csv(f"{BASE}/superstore-sales/dim_Date.csv", index=False)

# Also ship an .xlsx workbook: single flat sheet (matches "Dataset: Superstore Sales (Excel)")
with pd.ExcelWriter(f"{BASE}/superstore-sales/Superstore_Sales.xlsx", engine="openpyxl") as xw:
    superstore.to_excel(xw, sheet_name="Orders", index=False)

print("superstore-sales:", superstore.shape)

# ============================================================
# 2. SHOPSPHERE  (data-science-ml guide)
# ============================================================
n_cust = 6000
plan_types = ["basic", "standard", "premium"]
regions2 = ["NCR", "Region III", "Region IV-A", "Region VII", "Region XI"]

tenure = rng.integers(1, 60, n_cust)
plan = rng.choice(plan_types, n_cust, p=[0.5, 0.35, 0.15])
region = rng.choice(regions2, n_cust)
avg_order_value = np.round(rng.gamma(shape=3.0, scale=350, size=n_cust) + {"basic":0,"standard":200,"premium":500}[plan_types[0]], 2)
# make premium/standard skew higher AOV
plan_bonus = pd.Series(plan).map({"basic": 0, "standard": 250, "premium": 600}).to_numpy()
avg_order_value = np.round(rng.gamma(shape=3.0, scale=300, size=n_cust) + plan_bonus, 2)
orders_last_90d = rng.poisson(lam=np.clip(tenure / 12, 0.3, None))
days_since_last_order = rng.integers(0, 200, n_cust)
support_tickets = rng.poisson(lam=1.2, size=n_cust)

# churn probability: higher with low tenure, high days_since_last_order, low orders, many tickets
# Calibrated for a realistic ~5-7% base churn rate (the guide's imbalanced-classification teaching point)
logit = (
    -4.4
    - 0.03 * tenure
    + 0.018 * days_since_last_order
    - 0.30 * orders_last_90d
    + 0.30 * support_tickets
    + np.where(pd.Series(plan) == "basic", 0.5, 0.0)
    + rng.normal(0, 0.5, n_cust)
)
churn_prob = 1 / (1 + np.exp(-logit))
churned = (rng.uniform(0, 1, n_cust) < churn_prob).astype(int)

cancellation_reason = np.where(
    churned == 1,
    rng.choice(["too_expensive", "found_alternative", "no_longer_needed", "poor_support", "unknown"], n_cust),
    None,
)
refund_after_churn = np.where(churned == 1, rng.choice([0, 1], n_cust, p=[0.85, 0.15]), 0)

customer_ids = [f"CUST-{100000+i}" for i in range(n_cust)]

shopsphere = pd.DataFrame({
    "customer_id": customer_ids,
    "tenure_months": tenure,
    "avg_order_value": avg_order_value,
    "orders_last_90d": orders_last_90d,
    "days_since_last_order": days_since_last_order,
    "support_tickets": support_tickets,
    "plan_type": plan,
    "region": region,
    "churned_next_30d": churned,
    "cancellation_reason": cancellation_reason,
    "refund_after_churn": refund_after_churn,
})
shopsphere.to_csv(f"{BASE}/shopsphere/shopsphere_customers.csv", index=False)

# Reviews table for the NLP exercise (5.2 — TF-IDF + logistic regression sentiment)
positive_templates = [
    "Fast delivery and the {item} works great, very happy with this purchase.",
    "Excellent quality {item}, exceeded my expectations. Will buy again!",
    "The {item} arrived on time and packaging was perfect. Five stars.",
    "Great customer support when my {item} had an issue, resolved quickly.",
    "Love the {item}, exactly as described. Highly recommend to others.",
]
negative_templates = [
    "The {item} broke after one week, very disappointed with the quality.",
    "Delivery took way too long and the {item} arrived damaged.",
    "Customer support never responded about my {item} refund request.",
    "Overpriced for what you get, the {item} feels cheap and flimsy.",
    "Would not recommend, the {item} did not match the description at all.",
]
items = ["blender", "phone case", "backpack", "office chair", "wireless earbuds", "coffee maker", "desk lamp", "sneakers"]
n_reviews = 4000
review_rows = []
for i in range(n_reviews):
    sentiment = rng.choice(["positive", "negative"], p=[0.6, 0.4])
    template = rng.choice(positive_templates if sentiment == "positive" else negative_templates)
    text = template.format(item=rng.choice(items))
    review_rows.append({
        "review_id": f"REV-{i+1}",
        "customer_id": rng.choice(customer_ids),
        "review_text": text,
        "sentiment": sentiment,
    })
reviews = pd.DataFrame(review_rows)
reviews.to_csv(f"{BASE}/shopsphere/shopsphere_reviews.csv", index=False)

print("shopsphere_customers:", shopsphere.shape, " churn rate:", churned.mean().round(3))
print("shopsphere_reviews:", reviews.shape)

# ============================================================
# 3. ECOMMERCE ORDERS  (pydantic guide)
# ============================================================
n_orders = 1500
ph_regions = ["NCR", "Region III", "Region IV-A", "Region VII", "Region XI", "CAR"]
skus = [f"SKU-{1000+i}" for i in range(60)]
statuses = ["pending", "processing", "shipped", "delivered", "cancelled"]

order_rows = []
for i in range(n_orders):
    order_id = f"ORD-{20000+i}"
    email_ok = rng.uniform() > 0.06
    email = f"user{i}@example.com" if email_ok else rng.choice(["not-an-email", "user_at_example.com", ""])
    sku = rng.choice(skus)
    qty_ok = rng.uniform() > 0.04
    quantity = int(rng.integers(1, 10)) if qty_ok else rng.choice(["five", "-2", ""])
    unit_price_ok = rng.uniform() > 0.03
    unit_price = round(float(rng.uniform(50, 3000)), 2) if unit_price_ok else rng.choice([-99.0, 0])
    discount_ok = rng.uniform() > 0.05
    discount_pct = round(float(rng.uniform(0, 0.4)), 2) if discount_ok else round(float(rng.uniform(1.1, 2.0)), 2)
    order_date = pd.Timestamp("2025-01-01") + timedelta(days=int(rng.integers(0, 365)))
    ship_ok = rng.uniform() > 0.05
    if rng.uniform() < 0.15:
        ship_date = ""
    elif ship_ok:
        ship_date = (order_date + timedelta(days=int(rng.integers(1, 10)))).strftime("%Y-%m-%d")
    else:
        ship_date = (order_date - timedelta(days=int(rng.integers(1, 5)))).strftime("%Y-%m-%d")  # ship before order — bug
    status = rng.choice(statuses)
    if rng.uniform() < 0.08:
        status = status.upper()  # inconsistent casing
    order_id_dirty = f"  {order_id}" if rng.uniform() < 0.05 else order_id  # stray whitespace
    order_rows.append({
        "order_id": order_id_dirty,
        "customer_email": email,
        "product_sku": sku,
        "quantity": quantity,
        "unit_price": unit_price,
        "discount_pct": discount_pct if rng.uniform() > 0.1 else "",
        "order_date": order_date.strftime("%Y-%m-%d"),
        "ship_date": ship_date,
        "region": rng.choice(ph_regions) if rng.uniform() > 0.03 else "",
        "status": status,
    })

ecommerce_orders = pd.DataFrame(order_rows)
ecommerce_orders.to_csv(f"{BASE}/ecommerce-orders/ecommerce_orders.csv", index=False)
print("ecommerce_orders:", ecommerce_orders.shape)

# ============================================================
# 4. SHOPFLOW  (statistics-with-python guide)
# ============================================================
n_shop = 80000
ph_regions2 = ["NCR", "Region III", "Region IV-A", "Region VII", "Region XI", "CAR", "Region I", "Visayas", "Mindanao"]
categories2 = ["Electronics", "Fashion", "Home & Living", "Groceries", "Beauty", "Sports", "Toys"]
delivery_tiers = ["standard", "express", "same_day"]
delivery_statuses = ["delivered", "in_transit", "returned", "cancelled"]

order_id = np.arange(1, n_shop + 1)
customer_id = rng.integers(1, 25000, n_shop)
order_date = pd.Timestamp("2024-01-01") + pd.to_timedelta(rng.integers(0, 730, n_shop), unit="D")
delivery_lag = rng.integers(1, 15, n_shop)
delivery_date = order_date + pd.to_timedelta(delivery_lag, unit="D")
product_category = rng.choice(categories2, n_shop, p=[0.2,0.18,0.15,0.22,0.1,0.08,0.07])
region = rng.choice(ph_regions2, n_shop)
quantity = rng.integers(1, 12, n_shop)
# right-skewed order values with a modest outlier tail, matches guide's skewness/kurtosis exercise
# (calibrated for skew ~3-5, realistic for e-commerce order values — not an absurd long tail)
order_value = np.round(rng.lognormal(mean=6.3, sigma=0.55, size=n_shop), 2)
outlier_mask = rng.uniform(0, 1, n_shop) < 0.005
order_value[outlier_mask] = order_value[outlier_mask] * rng.uniform(3, 6, outlier_mask.sum())
discount_pct = np.round(rng.choice([0, 0, 0, 5, 10, 15, 20, 30], n_shop) / 100, 2)
shipping_fee = np.round(rng.uniform(0, 250, n_shop), 2)
weight_kg = np.round(rng.gamma(2, 0.8, n_shop), 2)
delivery_tier = rng.choice(delivery_tiers, n_shop, p=[0.6, 0.3, 0.1])
delivery_status = rng.choice(delivery_statuses, n_shop, p=[0.82, 0.08, 0.07, 0.03])
customer_phone = [f"09{rng.integers(100000000,999999999)}" for _ in range(n_shop)]

shopflow = pd.DataFrame({
    "order_id": order_id,
    "customer_id": customer_id,
    "order_date": order_date.strftime("%Y-%m-%d"),
    "delivery_date": delivery_date.strftime("%Y-%m-%d"),
    "product_category": product_category,
    "region": region,
    "quantity": quantity,
    "order_value": order_value,
    "discount_pct": discount_pct,
    "shipping_fee": shipping_fee,
    "weight_kg": weight_kg,
    "delivery_tier": delivery_tier,
    "delivery_status": delivery_status,
    "customer_phone": customer_phone,
})

# inject real-world messiness: nulls, duplicates, inconsistent phone formats
null_frac = 0.02
for col in ["delivery_date", "shipping_fee", "weight_kg", "customer_phone"]:
    mask = rng.uniform(0, 1, n_shop) < null_frac
    shopflow.loc[mask, col] = np.nan

# inconsistent phone formatting for a subset
alt_phone_mask = rng.uniform(0, 1, n_shop) < 0.1
shopflow.loc[alt_phone_mask, "customer_phone"] = shopflow.loc[alt_phone_mask, "customer_phone"].apply(
    lambda p: f"+63{str(p)[1:]}" if pd.notna(p) else p
)

# duplicate ~0.5% of rows (common real-world data quality issue)
dup_idx = rng.choice(shopflow.index, size=int(n_shop * 0.005), replace=False)
shopflow = pd.concat([shopflow, shopflow.loc[dup_idx]], ignore_index=True)

shopflow.to_csv(f"{BASE}/shopflow/shopflow_orders.csv", index=False)
print("shopflow_orders:", shopflow.shape)

# ============================================================
# 5. INVENTORY  (data-analyst guide — pairs with superstore-sales
#    via Product ID; feeds Phase 3/4 capstones + Final Capstone)
# ============================================================
inv_products = dim_product.copy().reset_index(drop=True)
n_products = len(inv_products)

supplier_names = ["Metro Supply Co.", "Pacific Wholesale", "Global Sourcing Partners", "Northbridge Distribution",
                   "Everstock Trading", "Union Freight Supply", "Continental Goods", "Harborline Logistics",
                   "Summit Vendor Group", "Coastal Import Co.", "Vantage Supply Chain", "Ridgeway Distributors",
                   "Anchor Wholesale", "Keystone Sourcing", "Trailhead Supply Co."]
supplier_countries = ["United States", "Mexico", "China", "Vietnam", "Canada"]
n_suppliers = len(supplier_names)
supplier_ids = [f"SUP-{100+i}" for i in range(n_suppliers)]
supplier_lead_time = rng.integers(3, 21, n_suppliers)
supplier_reliability = np.round(rng.uniform(0.82, 0.99, n_suppliers), 2)

suppliers = pd.DataFrame({
    "Supplier ID": supplier_ids,
    "Supplier Name": supplier_names,
    "Country": rng.choice(supplier_countries, n_suppliers),
    "Avg Lead Time Days": supplier_lead_time,
    "Reliability Rating": supplier_reliability,
})
suppliers.to_csv(f"{BASE}/inventory/inventory_suppliers.csv", index=False)

cost_basis = {"Furniture": 160, "Office Supplies": 14, "Technology": 260}
order_dates_dt = pd.to_datetime(superstore["Order Date"])
span_start, span_end = order_dates_dt.min(), order_dates_dt.max()
span_days = (span_end - span_start).days
warehouses = ["East DC", "West DC", "Central DC", "South DC"]

# Demand is modeled independently of the (deliberately sparse, ~1 order/product)
# superstore sample — this is the guide's own "synthetic Inventory dataset", sized
# like a real warehouse catalog: Office Supplies moves fastest, Furniture slowest.
demand_scale = {"Furniture": 1.2, "Office Supplies": 9.0, "Technology": 3.5}
avg_daily_demand = np.round(
    np.array([rng.gamma(shape=2.0, scale=demand_scale[c]) for c in inv_products["Category"]]) + 0.2,
    2,
)
inv_products["Avg Daily Demand"] = avg_daily_demand

supplier_idx = rng.integers(0, n_suppliers, n_products)
inv_products["Supplier ID"] = [supplier_ids[i] for i in supplier_idx]
inv_products["Warehouse"] = rng.choice(warehouses, n_products)
lead_time_days = np.array([int(np.clip(supplier_lead_time[i] + rng.integers(-2, 3), 2, 30)) for i in supplier_idx])
inv_products["Lead Time Days"] = lead_time_days
inv_products["Unit Cost"] = [round(cost_basis[c] * rng.uniform(0.5, 2.2), 2) for c in inv_products["Category"]]

safety_days = rng.integers(5, 15, n_products)
safety_stock = np.round(avg_daily_demand * safety_days).astype(int)
inv_products["Safety Stock"] = safety_stock
reorder_point = np.round(avg_daily_demand * lead_time_days).astype(int) + safety_stock
inv_products["Reorder Point"] = reorder_point

order_qty = np.maximum(5, np.round(avg_daily_demand * rng.integers(30, 90, n_products)).astype(int))
order_up_to = reorder_point + order_qty
beginning_stock = np.round(avg_daily_demand * rng.integers(45, 75, n_products)).astype(int) + 5
inv_products["Beginning Stock"] = beginning_stock

# Simulate a simple (s, S) reorder policy week-by-week across the order-date span:
# consume Poisson demand, and once stock dips to/below the reorder point, place a
# PO for (order-up-to - stock) that arrives after that product's lead time. This is
# what makes some products land below their reorder point "today" (the alert
# exercise) and slow movers accumulate untouched stock (the dead-stock exercise).
n_weeks = max(span_days // 7, 1)
receipt_rows = []
receipt_counter = 1
current_stock = np.zeros(n_products, dtype=int)
last_restock_date = [None] * n_products

for idx in range(n_products):
    pid = inv_products.loc[idx, "Product ID"]
    sup = inv_products.loc[idx, "Supplier ID"]
    cost = inv_products.loc[idx, "Unit Cost"]
    lam = max(avg_daily_demand[idx] * 7, 0.01)
    lead_weeks = max(int(round(lead_time_days[idx] / 7)), 1)
    s, S = reorder_point[idx], order_up_to[idx]
    stock = int(beginning_stock[idx])
    pending = {}  # arrival_week -> qty
    last_arrive_date = None
    for week in range(n_weeks):
        if week in pending:
            arrived_qty = pending.pop(week)
            stock += arrived_qty
            arrive_date = span_start + timedelta(days=week * 7)
            last_arrive_date = arrive_date
            receipt_rows.append({
                "Receipt ID": f"RC-{receipt_counter:06d}", "Product ID": pid, "Supplier ID": sup,
                "Receipt Date": arrive_date.strftime("%Y-%m-%d"),
                "Quantity Received": int(arrived_qty),
                "Unit Cost": cost,
            })
            receipt_counter += 1
        weekly_demand = rng.poisson(lam)
        stock = max(stock - weekly_demand, 0)
        if stock <= s and not pending:
            arrival_week = week + lead_weeks
            pending[arrival_week] = int(S - stock)
    current_stock[idx] = stock
    last_restock_date[idx] = last_arrive_date.strftime("%Y-%m-%d") if last_arrive_date else ""

inv_products["Current Stock"] = current_stock
inv_products["Last Restock Date"] = last_restock_date

receipts = pd.DataFrame(receipt_rows)
receipts.to_csv(f"{BASE}/inventory/inventory_receipts.csv", index=False)

inv_products = inv_products[[
    "Product ID", "Product Name", "Category", "Sub-Category", "Warehouse", "Supplier ID",
    "Unit Cost", "Lead Time Days", "Avg Daily Demand", "Safety Stock", "Reorder Point",
    "Beginning Stock", "Current Stock", "Last Restock Date",
]]
inv_products.to_csv(f"{BASE}/inventory/inventory_stock.csv", index=False)

print("inventory_stock:", inv_products.shape)
print("inventory_receipts:", receipts.shape)
print("inventory_suppliers:", suppliers.shape)
below_reorder = (inv_products["Current Stock"] < inv_products["Reorder Point"]).mean().round(3)
print("  share below reorder point:", below_reorder)
