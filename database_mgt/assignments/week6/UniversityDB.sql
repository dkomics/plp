-- Create a new MySQL database named "UniversityDB" using any appropriate MySQL client or command-line tool.
CREATE DATABASE UniversityDB;
-- Design a table named "Students" with the following attributes:
USE UniversityDB;
-- StudentID (Integer, Primary Key)
-- FirstName (VARCHAR, Maximum length 50)
-- LastName (VARCHAR, Maximum length 50)
-- Age (Integer)
-- Major (VARCHAR, Maximum length 50)
CREATE TABLE Students(
StudentID INT PRIMARY KEY,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Age INT,
Major VARCHAR(50)
);

-- Insert at least 5 records into the "Students" table with sample data.
INSERT INTO Students(StudentID, FirstName, LastName, Age, Major)
VALUES
(1001, 'Davids', 'Johnson', 27, 'Bioinfomatics'),
(1002, 'Maxwell', 'Hallway', 26, 'Genomics'),
(1003, 'Annie', 'Clinton', 27, 'Molecular Biology'),
(1004, 'Howard', 'Meshack', 22, 'Microbiology'),
(1005, 'Aaron', 'Davis', 25, 'Bioinfomatics');

-- Alter the "Students" table to add a new column named "GPA" with a data type appropriate for storing decimal values.
ALTER TABLE Students
ADD GPA DECIMAL(4, 2);
-- Insert GPA values for the existing records in the "Students" table.
UPDATE Students
SET GPA = 3.5
WHERE StudentID = 1001;

UPDATE Students
SET GPA = 3.8
WHERE StudentID = 1002;

UPDATE Students
SET GPA = 3.5
WHERE StudentID = 1003;

UPDATE Students
SET GPA = 3.0
WHERE StudentID = 1004;

UPDATE Students
SET GPA = 4.5
WHERE StudentID = 1005;

-- Rename the table from "Students" to "EnrolledStudents."
RENAME TABLE Students TO EnrolledStudents;

-- Create a new table named "Courses" with the following attributes:
-- CourseID (Integer, Primary Key)
-- CourseName (VARCHAR, Maximum length 100)
-- Instructor (VARCHAR, Maximum length 100)
-- Credits (Integer)

CREATE TABLE Courses(
CourseID INT PRIMARY KEY,
CourseName VARCHAR(100),
Instructor VARCHAR(100),
Credits INT
);

-- Insert at least 3 records into the "Courses" table with sample data.
INSERT INTO Courses(CourseID, CourseName, Instructor, Credits)
VALUES
(101, 'Bioinformatics', 'Davis John', 4),
(103, 'Microbiology', 'Mariam Ismail', 3),
(104, 'Genomics', 'Harris Jackson', 3);

-- Drop the "EnrolledStudents" table from the database.
DROP TABLE EnrolledStudents;