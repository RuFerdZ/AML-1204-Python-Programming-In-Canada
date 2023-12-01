import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, {self.age}"

    def get_birth_year(self):
        current_year = datetime.datetime.now().year
        return current_year - self.age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.name}, {self.age}, {self.student_id}"


student = Student("John", 36, 123)
print(student)
print(f"birth year: {student.get_birth_year()}")
