# College Management System

## Overview

The **College Management System** is a simple Python application designed to manage information about students, teachers, and colleges. Using Object-Oriented Programming (OOP) principles, the program allows the user to create colleges, add students and teachers to those colleges, display and search for students and teachers, and handle various other administrative tasks. It works through a command-line interface and is structured around four primary classes: `Person`, `Student`, `Teacher`, and `College`.

## Features

The College Management System offers the following key features:

1. **College Creation:**
   - You can create a college by specifying the college name. The system ensures that colleges are unique, preventing duplicate entries.

2. **Add Students:**
   - You can add students to a specific college by entering their roll number, name, branch, and job update status.

3. **Add Teachers:**
   - You can add teachers to a specific college by providing their roll number, name, and the subject they teach.

4. **Display Students:**
   - You can view the list of all students added to a particular college, along with details such as their roll number, name, branch, and job update.

5. **Display Teachers:**
   - You can view the list of all teachers in a particular college, along with their roll number, name, and the subjects they teach.

6. **Search Students:**
   - You can search for a student by name. The system will check the entered name and confirm if the student exists within the specified college.

7. **Search Teachers:**
   - Similarly, you can search for a teacher by name and retrieve the details of the teacher, including the subject they teach.

8. **Exit Option:**
   - You can exit the program at any time with a simple exit option.

## Classes and Attributes

The program is structured using classes to represent different entities within the system. Each class has its own attributes and methods.

### 1. **Person Class**
   - **Attributes:**
     - `rollno`: The unique identifier for each person (either student or teacher).
     - `name`: The name of the person.
   - **Methods:**
     - `__init__(self, rollno, name)`: Constructor to initialize `rollno` and `name` attributes.
   
   This class is a base class for both students and teachers, serving as a parent class for inheritance.

### 2. **Student Class**
   - **Inherits from:** `Person`
   - **Attributes:**
     - `branch`: The field of study the student is enrolled in (e.g., Computer Science, Mechanical Engineering, etc.).
     - `jobupdate`: Information about the student's current job or internship status.
   - **Methods:**
     - `__init__(self, rollno, name, branch, jobupdate)`: Constructor to initialize `rollno`, `name`, `branch`, and `jobupdate` attributes.

### 3. **Teacher Class**
   - **Inherits from:** `Person`
   - **Attributes:**
     - `subject`: The subject the teacher specializes in (e.g., Mathematics, Physics, Computer Science).
   - **Methods:**
     - `__init__(self, rollno, name, subject)`: Constructor to initialize `rollno`, `name`, and `subject` attributes.

### 4. **College Class**
   - **Attributes:**
     - `cname`: The name of the college.
     - `students`: A list that stores student objects.
     - `teachers`: A list that stores teacher objects.
   - **Methods:**
     - `__init__(self, cname)`: Constructor to initialize `cname`, `students`, and `teachers`.
     - `add_student(self, student)`: Method to add a student to the college's student list.
     - `add_teacher(self, teacher)`: Method to add a teacher to the college's teacher list.
     - `display_students(self)`: A placeholder method to display all students in the college.
     - `display_teachers(self)`: A placeholder method to display all teachers in the college.

## User Interaction

The user interacts with the system via a simple menu interface where the following actions can be performed:

1. **Create College**
   - Create a new college by providing a unique name. The system will check for duplicates and notify the user if the college already exists.
   
2. **Add Student**
   - Add a new student to an existing college. The user will be prompted to provide details such as roll number, name, branch, and job status.

3. **Add Teacher**
   - Add a teacher to an existing college. The user will be asked to provide the teacher's roll number, name, and subject they teach.

4. **Display Students**
   - The system will display the list of all students in a given college, including their roll number, name, branch, and job update.

5. **Display Teachers**
   - Display all teachers in the given college, showing their roll number, name, and subject taught.

6. **Search Students**
   - Allows users to search for a student by name. The system will confirm if the student exists in the college and provide their details if found.

7. **Search Teachers**
   - Search for a teacher by name and display their subject if found.

8. **Exit**
   - Ends the program.


