
USE StudentDB


--1> Count total numbers of student
select count (*) total_student from students;

--2> Find avarage marks of student
select avg(marks) as avg_marks from  students;

--3> Find the higest and lowest marks
select max(marks) as higest_marks,min(marks) as lowest_marks from students;

--4> Find department wise average marks
select department, avg(marks) avg_marks from students group by department;

--5> Display depatrment where avg marks>70
SELECT 
    department,
    AVG(marks) AS average_marks
FROM students
GROUP BY department
HAVING AVG(marks) > 70;
