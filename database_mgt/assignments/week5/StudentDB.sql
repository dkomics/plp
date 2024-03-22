CREATE DATABASE StudentDB;
USE StudentDB;
CREATE TABLE Students (
studentID INT PRIMARY KEY,
first_name VARCHAR(150),
last_name VARCHAR(150),
date_of_birth DATE,
email VARCHAR(150),
major VARCHAR(50)
);

-- Entering students information into the database using the Students Table

INSERT INTO Students (studentID, first_name, last_name, date_of_birth, email, major)
VALUES
(1001, 'Jay', 'Patrick', '1990-09-28', 'pjay@powerlearnproject.org', 'Database design and programming with SQL'),
(1002, 'Shakul', 'Kingston', '1999-02-23', 'kshakul@powerlearnproject.org', 'Dart - Flutter programming'),
(1003, 'Joyce', 'Mangi', '2000-05-12', 'mjoyce@powerlearnproject.org', 'Web development'),
(1004, 'Christine', 'Melkzedeck', '1995-01-21', 'mchristine@powerlearnproject.org', 'Python programming');