CREATE DATABASE ecommerce_db;

USE ecommerce_db;


-- Create Table 

CREATE TABLE customers(
customer_id INT PRIMARY KEY,
name VARCHAR(100),
city VARCHAR(100)
);


CREATE TABLE orders(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE,
amount DECIMAL(10,2),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);


CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- insert Values of tables

INSERT INTO customers (customer_id, name, city) VALUES
(1, 'Krish', 'Delhi'),
(2, 'Yash', 'Mumbai'),
(3, 'Taks', 'Bangalore'),
(4, 'Dhruv', 'Chennai'),
(5, 'Aryan', 'Delhi'),
(6, 'Tirth', 'Pune');

INSERT INTO products (product_id, product_name, price) VALUES
(101, 'Laptop', 55000),
(102, 'Smartphone', 30000),
(103, 'Headphones', 2000),
(104, 'Keyboard', 1500),
(105, 'Mouse', 800);

INSERT INTO orders (order_id, customer_id, order_date, amount) VALUES
(1001, 1, '2024-01-10', 85000),
(1002, 2, '2024-01-15', 30000),
(1003, 1, '2024-02-05', 2000),
(1004, 3, '2024-02-20', 60000),
(1005, 4, '2024-03-01', 1500),
(1006, 5, '2024-03-10', 55000),
(1007, 3, '2024-03-15', 30000);


INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1001, 101, 1),
(1001, 102, 1),

(1002, 102, 1),

(1003, 103, 1),

(1004, 101, 1),
(1004, 105, 2),

(1005, 104, 1),

(1006, 101, 1),

(1007, 102, 1);


-- 1.Total orders per customer

SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;


--2.Customers who never placed an order

SELECT 
    c.customer_id,
    c.name,
    c.city
FROM customers c
LEFT JOIN orders o 
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;


--3.Highest selling product 

SELECT 
    p.product_id,
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold
FROM products p
JOIN order_items oi 
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC


--4.Monthly sales report

SELECT 
    FORMAT(order_date, 'yyyy-MM') AS month,
    SUM(amount) AS total_sales
FROM orders
GROUP BY FORMAT(order_date, 'yyyy-MM')
ORDER BY month;


--5.Customers with total purchase > 50,000

SELECT *
FROM (
    SELECT 
        c.customer_id,
        c.name,
        SUM(o.amount) AS total_purchase
    FROM customers c
    JOIN orders o 
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name
) t
WHERE total_purchase > 50000;


--6.Top 3 cities by revenue

SELECT 
    c.city,
    SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o 
    ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC










