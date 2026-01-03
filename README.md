# Python.py
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Child class
class Bike(Vehicle):

    def start(self):
        print("Bike starts with a kick or self-start")


# Creating object of Bike
b = Bike()
b.start()

INHERITANCE:
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def show(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


# Object create karna
s1 = Student("Ali", 101)
s1.show()