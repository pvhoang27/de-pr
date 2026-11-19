CREATE TABLE silver_orders AS
WITH ranked_orders AS (
    SELECT
        order_id,
        customer_id,
        amount,
        ROW_NUMBER() OVER (
            PARTITION BY order_id
            ORDER BY amount DESC NULLS LAST
        ) AS rn
    FROM bronze_orders
)
SELECT
    order_id,
    customer_id,
    amount
FROM ranked_orders
WHERE rn = 1
  AND amount IS NOT NULL;