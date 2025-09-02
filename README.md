# Student_Mang_Sys_PY
🎓 University Management System (Python OOPs Project)
This is a simple Object-Oriented Programming (OOP)-based Python project that simulates a University Management System. It demonstrates the use of core OOP principles like inheritance, abstraction, encapsulation, polymorphism, and includes examples of abstract base classes, method overriding, and more.

📚 Features
Abstract Class: Department is an abstract base class with department-specific subclasses like Science, Commerce, and Arts.

Inheritance and Method Overriding:

Person is the base class.

Student, GraduateStudent, and Teacher inherit from Person, with overridden displayProfile() methods.

Encapsulation:

The Result class demonstrates private attributes with getters and setters.

Polymorphism:

Function generateReport() works with a single student or a list of students.

Modular Design:

Clear structure for departments, persons (students/teachers), results, and report generation.

🏗️ Classes Overview
Department (ABC) – Abstract class for departments.

Science, Commerce, Arts – Derived classes implementing course lists.

Person – Base class for people.

Student → GraduateStudent – Represent students and specializations.

Teacher – Represent university staff.

Result – Manages student marks and grade with encapsulated access.

generateReport() – Generates reports for students.

🧪 Sample Output

Departments and Courses:
Science Courses: Physics, Chemistry, Biology
Commerce Courses: Accountancy, Economics, Business Studies
Arts Courses: History, Geography, Political Science

Raju's Marks: 88, Grade: A
Raju's Updated Marks: 92, Grade: A+

Profiles:
Student Profile - Name: Raju, Age: 20, Roll No: 101, Course: Physics
Graduate Student - Name: Ramesh, Age: 22, Roll No: 102, Course: Biology, Specialization: Genetics
Teacher Profile - Name: Dr. Sharma, Age: 40, Employee ID: T001, Subject: Mathematics

Reports:
Generating report for Raju (Roll No: 101)
Generating reports for all students:
  Raju (Roll No: 101)
  Ramesh (Roll No: 102)

👨‍💻 Author
Atharva Hanchate

