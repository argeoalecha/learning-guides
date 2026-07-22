-- TindaHub seed data — run after schema.sql (which starts identities at 1).
-- 4 categories, 8 customers, 15 products, 20 orders, 60 order items, payments.

INSERT INTO categories (name) VALUES
  ('Electronics'), ('Home & Living'), ('Groceries'), ('Fashion')
ON CONFLICT (name) DO NOTHING;

INSERT INTO customers (full_name, email, city, province, region) VALUES
  ('Maria Santos',     'maria@example.com',  'Cebu City',      'Cebu',              'Central Visayas'),
  ('Jose Reyes',       'jose@example.com',   'Davao City',     'Davao del Sur',     'Davao Region'),
  ('Andrea Cruz',      'andrea@example.com', 'Quezon City',    'Metro Manila',      'NCR'),
  ('Mark Villanueva',  'mark@example.com',   'Iloilo City',    'Iloilo',            'Western Visayas'),
  ('Liza Aquino',      'liza@example.com',   'Baguio City',    'Benguet',           'CAR'),
  ('Paolo Mendoza',    'paolo@example.com',  'Cagayan de Oro', 'Misamis Oriental',  'Northern Mindanao'),
  ('Grace Tan',        'grace@example.com',  'Makati City',    'Metro Manila',      'NCR'),
  ('Ramon Bautista',   'ramon@example.com',  'Bacolod City',   'Negros Occidental', 'Western Visayas');

INSERT INTO products (category_id, name, price, attributes) VALUES
  (1, 'USB-C Charger 30W',      499.00, '{"watts":30,"ports":["usb-c","usb-a"]}'),
  (1, 'Wireless Mouse',         350.00, '{"dpi":1600,"wireless":true}'),
  (1, 'HDMI Cable 2m',          199.00, '{"length_m":2}'),
  (1, 'Power Bank 10000mAh',    899.00, '{"capacity_mah":10000,"ports":["usb-c","usb-a"]}'),
  (1, 'Bluetooth Earbuds',     1299.00, '{"wireless":true,"anc":false}'),
  (2, 'Ceramic Mug',            149.00, '{"color":"white","ml":350}'),
  (2, 'LED Desk Lamp',          749.00, '{"watts":9,"dimmable":true}'),
  (2, 'Throw Pillow',           299.00, '{"size":"45x45"}'),
  (3, 'Brewed Coffee 250g',     320.00, '{"roast":"medium"}'),
  (3, 'Coconut Oil 500ml',      180.00, '{"organic":true}'),
  (3, 'Rice 5kg',               290.00, '{"variety":"jasmine"}'),
  (4, 'Cotton T-Shirt',         399.00, '{"size":"M","color":"black"}'),
  (4, 'Tsinelas (Flip-flops)',  129.00, '{"size":"9"}'),
  (4, 'Canvas Tote Bag',        249.00, '{"color":"natural"}'),
  (4, 'Baseball Cap',           279.00, '{"adjustable":true}');

INSERT INTO orders (customer_id, status, ordered_at) VALUES
  (1, 'delivered', '2026-01-05 10:15+08'),
  (2, 'delivered', '2026-01-12 14:30+08'),
  (3, 'shipped',   '2026-01-20 09:05+08'),
  (1, 'delivered', '2026-02-03 16:45+08'),
  (4, 'cancelled', '2026-02-09 11:20+08'),
  (5, 'delivered', '2026-02-15 08:50+08'),
  (3, 'delivered', '2026-02-22 19:10+08'),
  (6, 'delivered', '2026-03-01 13:00+08'),
  (7, 'shipped',   '2026-03-10 10:40+08'),
  (2, 'delivered', '2026-03-18 15:25+08'),
  (8, 'delivered', '2026-03-25 12:05+08'),
  (1, 'delivered', '2026-04-02 09:30+08'),
  (4, 'delivered', '2026-04-11 17:15+08'),
  (5, 'cancelled', '2026-04-19 14:00+08'),
  (7, 'delivered', '2026-04-27 11:55+08'),
  (3, 'delivered', '2026-05-06 10:10+08'),
  (6, 'shipped',   '2026-05-14 16:20+08'),
  (8, 'delivered', '2026-05-23 13:45+08'),
  (2, 'delivered', '2026-06-04 09:00+08'),
  (7, 'pending',   '2026-06-12 18:30+08');

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
  (1, 1, 1, 499.00), (1, 3, 2, 199.00),
  (2, 5, 1, 1299.00), (2, 6, 2, 149.00),
  (3, 9, 3, 320.00), (3, 11, 1, 290.00), (3, 10, 2, 180.00),
  (4, 2, 1, 350.00), (4, 7, 1, 749.00),
  (5, 12, 2, 399.00), (5, 13, 1, 129.00),
  (6, 4, 1, 899.00), (6, 1, 1, 499.00), (6, 3, 1, 199.00),
  (7, 6, 4, 149.00), (7, 8, 2, 299.00),
  (8, 11, 2, 290.00), (8, 9, 1, 320.00), (8, 10, 1, 180.00),
  (9, 5, 2, 1299.00),
  (10, 12, 3, 399.00), (10, 15, 1, 279.00), (10, 14, 2, 249.00),
  (11, 7, 1, 749.00), (11, 6, 2, 149.00),
  (12, 1, 2, 499.00), (12, 2, 1, 350.00), (12, 4, 1, 899.00),
  (13, 9, 2, 320.00), (13, 11, 3, 290.00),
  (14, 13, 2, 129.00),
  (15, 5, 1, 1299.00), (15, 8, 1, 299.00),
  (16, 12, 1, 399.00), (16, 13, 1, 129.00), (16, 15, 2, 279.00), (16, 14, 1, 249.00),
  (17, 3, 3, 199.00), (17, 1, 1, 499.00),
  (18, 11, 4, 290.00), (18, 10, 2, 180.00),
  (19, 2, 2, 350.00), (19, 7, 1, 749.00),
  (20, 6, 1, 149.00), (20, 9, 1, 320.00);

-- Payments derived from line totals: one per non-cancelled order, mostly COD.
INSERT INTO payments (order_id, method, amount, paid_at)
SELECT o.order_id,
       CASE WHEN o.order_id % 5 = 0 THEN 'gcash'
            WHEN o.order_id % 7 = 0 THEN 'card'
            ELSE 'cod' END,
       SUM(oi.quantity * oi.unit_price),
       CASE WHEN o.status = 'delivered' THEN o.ordered_at + interval '2 days' END
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.status <> 'cancelled'
GROUP BY o.order_id, o.status, o.ordered_at;
