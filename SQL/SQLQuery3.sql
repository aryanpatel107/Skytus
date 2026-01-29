CREATE DATABASE company_db;
USE company_db;

create table employees(
  emp_id INT,
  emp_name VARCHAR(50),
  dept_id INT,
  salary INT
  )

create table departments(
   dept_id INT,
   dept_name VARCHAR(50)
   )

insert into employees values
(101,'Dhruv',1, 50000),
(102,'yash',2,80000),
(103,'Krish',4,75000),
(104,'Aryan',3,48000),
(105,'Ram',3,52000),
(106,'Jay',NULL,40000);

insert into departments values
(1,'HR'),
(2,'IT'),
(3,'Finance'),
(4,'Marketing');

--1> Display employee name with department name
select e.emp_name, d.dept_name from employees e
inner join departments d on e.dept_id = d.dept_id;

--2> employees earning more than 50000
select emp_name,salary from employees where salary > 50000;

--3>depatment-wise total salary
select d.dept_name, Sum(e.salary) as total_salary from employees e inner join departments d on e.dept_id = d.dept_id group by d.dept_name;

--4>department with more than 2 employees
select d.dept_name, count(e.emp_id) as employee_count from employees e inner join departments d on e.dept_id = d.dept_id group by d.dept_name having count(e.emp_id) > 1;

--5> Employees without a department
select emp_name from employees where dept_id is null;