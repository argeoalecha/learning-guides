-- TindaHub schema — Philippine online marketplace (COD, peso-priced)
-- Matches the PostgreSQL & Metabase Learning Guide, Module 1.2.
-- Idempotent: safe to re-run.

DROP TABLE IF EXISTS payments      CASCADE;
DROP TABLE IF EXISTS order_items   CASCADE;
DROP TABLE IF EXISTS orders        CASCADE;
DROP TABLE IF EXISTS products      CASCADE;
DROP TABLE IF EXISTS customers     CASCADE;
DROP TABLE IF EXISTS categories    CASCADE;

CREATE TABLE categories (
  category_id  bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  name         text NOT NULL UNIQUE
);

CREATE TABLE customers (
  customer_id  bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  full_name    text NOT NULL,
  email        text NOT NULL UNIQUE,
  city         text NOT NULL,
  province     text NOT NULL,
  region       text NOT NULL,
  created_at   timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE products (
  product_id   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  category_id  bigint NOT NULL REFERENCES categories(category_id),
  name         text NOT NULL,
  price        numeric(12,2) NOT NULL CHECK (price >= 0),
  is_active    boolean NOT NULL DEFAULT true,
  attributes   jsonb NOT NULL DEFAULT '{}'::jsonb
);

CREATE TABLE orders (
  order_id     bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  customer_id  bigint NOT NULL REFERENCES customers(customer_id),
  status       text NOT NULL DEFAULT 'pending'
               CHECK (status IN ('pending','shipped','delivered','cancelled')),
  ordered_at   timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE order_items (
  order_item_id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  order_id      bigint NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
  product_id    bigint NOT NULL REFERENCES products(product_id),
  quantity      integer NOT NULL CHECK (quantity > 0),
  unit_price    numeric(12,2) NOT NULL CHECK (unit_price >= 0)
);

CREATE TABLE payments (
  payment_id   bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  order_id     bigint NOT NULL UNIQUE REFERENCES orders(order_id),
  method       text NOT NULL CHECK (method IN ('cod','gcash','card','bank')),
  amount       numeric(12,2) NOT NULL CHECK (amount >= 0),
  paid_at      timestamptz
);
