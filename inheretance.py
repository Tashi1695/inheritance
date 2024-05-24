class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age)
        self.student_id = student_id
        self.major = major

    def get_details(self):
        return f"{super().get_details()}, Student ID: {self.student_id}, Major: {self.major}"

class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def get_details(self):
        return f"{super().get_details()}, Employee ID: {self.employee_id}, Subject: {self.subject}"

# Create Student and Teacher Objects
student = Student("Alice", 20, "S12345", "Computer Science")
teacher = Teacher("Bob", 45, "T98765", "Mathematics")

# Print details of the Student and Teacher
print(student.get_details())
print(teacher.get_details())
