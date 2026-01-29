--1. Add index to improve search on orderrs.customer_id

CREATE INDEX idx_orders_customer_id
ON orders(customer_id);


--2. Use SET STATISTICS PROFILE ON instad off EXPLAIN to anaiyze query Optimize a slow join query

SET STATISTICS PROFILE ON;

SELECT 
    c.customer_id,
    c.name,
    o.order_id,
    o.amount
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
WHERE o.customer_id = 3;

SET STATISTICS PROFILE OFF;


--3.Optimize a slow join query

CREATE INDEX idx_customers_city
ON customers(city);

SELECT c.name,o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.city ='Delhi';


--4.When index shouid not be used select

SELECT*
FROM orders
WHERE order_date between '2024-01-01'
and '2024-12-31'

SELECT*
FROM customers 
WHERE city in('Delhi','Pune');






