CREATE TABLE bronze_orders (
    order_id INT,
    customer_id VARCHAR(20),
    amount INT
);

INSERT INTO bronze_orders
    (order_id, customer_id, amount)
VALUES
    (101, 'C01', 200),
    (102, 'C02', 300),
    (102, 'C02', 300),
    (103, 'C01', NULL),
    (104, 'C03', 500);


SELECT *
FROM bronze_orders;