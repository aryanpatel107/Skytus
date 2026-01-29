USE company_db;
SELECT name FROM sys.tables;

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'employees';

--1> find employees earning more than average salary
select emp_name, salary from employees where salary > (select avg(salary) from employees);

--2> find department with higest total salary
select d.dept_name, sum(e.salary) as total_salary from employees e join departments d on e.dept_id = d.dept_id
group by d.dept_name order by total_salary desc ;

--3> Display employee with second higest salary
select emp_name, salary from employees where salary = (select max(salary) from employees where salary < (select max(salary) from employees));

--4>Display employees working in same department 
SELECT emp_name
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Krish'
)
AND emp_name <> 'Krish';
