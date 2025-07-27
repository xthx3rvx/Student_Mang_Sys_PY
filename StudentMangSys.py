from abc import ABC, abstractmethod

class Department(ABC):
    @abstractmethod
    def courseList(self):
        pass

class Science(Department):
    def courseList(self):
        print("Science Courses: Physics, Chemistry, Biology")

class Commerce(Department):
    def courseList(self):
        print("Commerce Courses: Accountancy, Economics, Business Studies")

class Arts(Department):
    def courseList(self):
        print("Arts Courses: History, Geography, Political Science")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayProfile(self): 
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, rollNo, course):
        super().__init__(name, age)
        self.rollNo = rollNo
        self.course = course

    def displayProfile(self):  
        print(f"Student Profile - Name: {self.name}, Age: {self.age}, Roll No: {self.rollNo}, Course: {self.course}")

class GraduateStudent(Student): 
    def __init__(self, name, age, rollNo, course, specialization):
        super().__init__(name, age, rollNo, course)
        self.specialization = specialization

    def displayProfile(self): 
        print(f"Graduate Student - Name: {self.name}, Age: {self.age}, Roll No: {self.rollNo}, Course: {self.course}, Specialization: {self.specialization}")

class Teacher(Person):
    def __init__(self, name, age, employeeID, subject):
        super().__init__(name, age)
        self.employeeID = employeeID
        self.subject = subject

    def displayProfile(self):  
        print(f"Teacher Profile - Name: {self.name}, Age: {self.age}, Employee ID: {self.employeeID}, Subject: {self.subject}")

class Result:
    def __init__(self, marks, grade):
        self.__marks = marks
        self.__grade = grade

    def getMarks(self):
        return self.__marks

    def setMarks(self, marks):
        self.__marks = marks

    def getGrade(self):
        return self.__grade

    def setGrade(self, grade):
        self.__grade = grade

def generateReport(student=None, student_list=None):
    if student is not None:
        print(f"Generating report for {student.name} (Roll No: {student.rollNo})")
    elif student_list is not None:
        print("Generating reports for all students:")
        for s in student_list:
            print(f"  {s.name} (Roll No: {s.rollNo})")
    else:
        print("No student data provided.")

if __name__ == "__main__":
    
    print("Departments and Courses:")
    sci = Science()
    com = Commerce()
    art = Arts()
    sci.courseList()
    com.courseList()
    art.courseList()
    print()

    s1 = Student("Raju", 20, 101, "Physics")
    s2 = GraduateStudent("Ramesh", 22, 102, "Biology", "Genetics")
    t1 = Teacher("Dr. Sharma", 40, "T001", "Mathematics")

    r1 = Result(88, "A")
    print(f"{s1.name}'s Marks: {r1.getMarks()}, Grade: {r1.getGrade()}")
    r1.setMarks(92)
    r1.setGrade("A+")
    print(f"{s1.name}'s Updated Marks: {r1.getMarks()}, Grade: {r1.getGrade()}")
    print()

    print("Profiles:")
    s1.displayProfile()
    s2.displayProfile()
    t1.displayProfile()
    print()

    print("Reports:")
    generateReport(student=s1)
    generateReport(student_list=[s1, s2])
