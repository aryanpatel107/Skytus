--1.Tasks count total number of student

SELECT COUNT(*) AS total_students 
FROM Students;


--2.Find average marks of students

SELECT AVG(marks) AS average_marks
FROM students;


--3.Find highest and lowest marks

SELECT MAX(marks) AS highest_marks,
MIN(marks) AS lowest_marks
FROM students;


--4.Find department-wise average marks 

SELECT department,
Avg(marks) AS avg_marks
FROM Students
GROUP BY department;


--5.Display department where average marks > 70

SELECT department,
AVG(marks) As avg_marks
FROM Students
GROUP BY department
HAVING AVG(marks) > 70;


