WITH ranked_orders AS (
    SELECT
        order_id,
        amount,
        updated_at,
        ROW_NUMBER() OVER (
            PARTITION BY order_id
            ORDER BY updated_at DESC
        ) AS rn
    FROM orders
)
SELECT order_id, amount, updated_at
FROM ranked_orders
WHERE rn = 1;