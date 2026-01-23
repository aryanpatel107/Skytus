CREATE DATABASE StudentDB;

USE StudentDB;

CREATE TABLE students(
  student_id INT PRIMARY KEY,
  name VARCHAR(50),
  department VARCHAR(30),
  year INT,
  marks INT
  );

INSERT INTO students VALUES
(1, 'Amit', 'CSE', 3, 85),
(2, 'Neha', 'ECE', 2, 78),
(3, 'Rahul', 'CSE', 4, 92),
(4, 'Priya', 'MECH', 1, 69),
(5, 'Suman', 'CSE', 3, 88),
(6, 'Karan', 'EEE', 2, 74);


SELECT*FROM students;

SELECT*FROM students
WHERE marks > 75;

SELECT*FROM students
WHERE department = 'CSE';

SELECT * FROM students
ORDER BY marks DESC;

SELECT TOP 3 * FROM students
ORDER BY marks DESC;






