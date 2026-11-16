
-- Tạo bảng orders
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    updated_at TEXT,
    amount INTEGER
);

-- Thêm 4 bản ghi
INSERT INTO orders (order_id, updated_at, amount)
VALUES
(101, '2026-11-15 09:00:00', 200),
(102, '2026-11-15 11:00:00', 300),
(103, '2026-11-16 08:00:00', 400),
(104, '2026-11-16 09:00:00', 500);
