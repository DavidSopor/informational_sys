from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, surname):
        self.name=name 
        self.surname=surname
    
    @abstractmethod
    def introduce_yourself(self):
        pass

class Student(Person):
    def __init__(self, name, surname, grade):
        super().__init__(name, surname)
        self.grade=grade 
    
    def introduce_yourself(self):
        print(f"Hi my name is {self.name} and surname is {self.surname}")
    
    def __str__(self):
        return f"Student, name: {self.name} surname: {self.surname} grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, surname, degree):
        super().__init__(name, surname)
        self.degree=degree 
    
    def introduce_yourself(self):
        print(f"Hi my name is {self.name} and surname is {self.surname} and I am teacher")
    
    def __str__(self):
        return f"Teacher, name: {self.name} surname: {self.surname} degree: {self.degree}"
    
class Cleaner(Person):
    def __init__(self, name, surname, age, work_time):
        super().__init__(name, surname)
        self.age = age
        self.work_time = work_time

    def introduce_yourself(self):
        print(f"Hello I'm {self.name} {self.surname} and I'm cleaner")

    def __str__(self):
        return f"Cleaner, name: {self.name} {self.surname} age: {self.age} work time: {self.work_time}"