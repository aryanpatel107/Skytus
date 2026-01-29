CREATE DATABASE company_orders_db;

USE company_orders_db;

--1.Create users table with:Primary key Unique email Not null password 

CREATE TABLE users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,  
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,              
    password VARCHAR(100) NOT NULL           
);


--2.Create orders table and add foreign key to users

CREATE TABLE orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    CONSTRAINT FK_orders_users FOREIGN KEY (user_id) REFERENCES users(user_id)
);


--3.Create index on email column

CREATE INDEX idx_users_email
ON users(email);



--4.Create view to display user order summary


CREATE VIEW user_order_summary 
AS
SELECT 
    u.user_id,
    u.name,
    u.email,
    COUNT(o.order_id) AS total_orders,
    ISNULL(SUM(o.amount), 0) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY u.user_id, u.name, u.email;



INSERT INTO users (name, email, password) VALUES
('Amit', 'amit@example.com', 'pass123'),
('Sara', 'sara@example.com', 'pass456'),
('John', 'john@example.com', 'pass789');

INSERT INTO orders (user_id, order_date, amount) VALUES
(1, '2026-01-20', 100.50),
(1, '2026-01-22', 250.00),
(2, '2026-01-21', 300.75);



SELECT * FROM user_order_summary;