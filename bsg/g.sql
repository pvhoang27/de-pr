CREATE TABLE gold_customer_revenue AS
SELECT
    customer_id,
    SUM(amount) AS total_amount
FROM silver_orders
GROUP BY customer_id;