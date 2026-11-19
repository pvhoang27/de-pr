INSERT INTO warehouse_orders (
    order_id, amount, updated_at
)
VALUES
    (103, 400, '2026-11-17 08:00:00'),
    (104, 500, '2026-11-17 10:00:00'),
    (105, 600, '2026-11-17 15:00:00')
ON CONFLICT (order_id)
DO UPDATE SET
    amount = EXCLUDED.amount,
    updated_at = EXCLUDED.updated_at
WHERE warehouse_orders.updated_at
      < EXCLUDED.updated_at;