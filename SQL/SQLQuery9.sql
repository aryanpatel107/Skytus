
CREATE DATABASE interview_db;

USE interview_db;


CREATE TABLE employees(
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    hire_date DATE
);

INSERT INTO employees VALUES
(1,'Krish',50000,'2025-01-10'),
(2, 'Yash', 40000, '2025-01-10'),
(3, 'Taksh', 60000, '2025-05-15'),
(4, 'Dhruv', 70000, '2025-08-01'),
(5, 'Aryan', 65000, '2025-09-12'),
(6, 'Krish', 50000, '2025-11-20'),
(7, 'Trith', 80000, '2025-01-10');


--1.Find Nth highest salary

SELECT salary

FROM employees e1
WHERE  3 - 1 =(
SELECT COUNT(DISTINCT salary)
FROM employees e2
WHERE e2.salary > e1.salary 
);

SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC


--2.Remove duplicate records

DELETE FROM employees 
WHERE emp_id IN (
SELECT emp_id
FROM (

   SELECT emp_id,
      ROW_NUMBER() OVER(
        PARTITION BY name, salary, hire_date
        ORDER BY emp_id
       )AS rn
    FROM employees
   )t
   WHERE rn > 1
);



CREATE TABLE table_a (
   id INT,
   name VARCHAR(50)
   );

INSERT INTO table_a VALUES
(1,'Krish'),
(2,'Yash'),
(3,'Taksh'),
(4,'Dhruv');


CREATE TABLE table_b (
    id INT,
    name VARCHAR(50)
);

INSERT INTO table_b VALUES
(3, 'Aryan'),
(4, 'Meet'),
(1, 'Krish'),
(6, 'Nisarg');


--3.Find common records in two tables

SELECT t1.*
FROM table_a t1
 INNER JOIN table_b t2
ON t1.id = t2.id;

SELECT * FROM table_a
INTERSECT
SELECT * FROM table_b;

--4.Employees hired in last 6 months

SELECT *
FROM employees
WHERE hire_date >= CAST(DATEADD(MONTH, -6, GETDATE()) AS DATE);


--5.Continuous duplicate values


CREATE TABLE logs1 (
    id INT,
    value VARCHAR(10)
);


INSERT INTO logs1 VALUES
(1, 'A'),
(2, 'A'),
(3, 'A'),
(4, 'B'),
(5, 'B'),
(6, 'C');

SELECT*
FROM(
   SELECT*,
     LAG(value)OVER(ORDER BY id)
AS prev_value 
  FROM logs1
  )t
  WHERE value = prev_value;





     








