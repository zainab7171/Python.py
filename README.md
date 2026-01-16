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
class Car:
    def __init__(self):
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def set_speed(self, value):
        if value >= 0:
            self.__speed = value
            print("Speed after setting:", self.__speed)
        else:
            print("Invalid speed")

    def accelerate(self, amount):
        self.__speed += amount
        print("Speed after acceleration:", self.__speed)

    def brake(self, amount):
        self.__speed -= amount
        if self.__speed < 0:
            self.__speed = 0
        print("Speed after braking
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw
class Employee:
    def __init__(self):
        self.__salary = 0

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount >= 0:
            self.__salary = amount
            print("Salary after setting:", self.__salary)
        else:
            print("Invalid salary")

    def increase_salary(self, percent):
        self.__salary += self.__salary * percent / 100
        print("Salary after increment:", self.__salary)


# Test Script
e = Employee()
e.set_salary(-1000)   # invalid
e.set_salary(5000)
e.increase_salary(10)
class Product:
    def __init__(self):
        self.__price = 0

    def get_price(self):
        return self.__price

    def set_price(self, amount):
        if amount > 0:
            self.__price = amount
            print("Price after setting:", self.__price)
        else:
            print("Invalid price")

    def apply_discount(self, percent):
        if 0 < percent < 100:
            self.__price -= self.__price * percent / 100
            print("Price after discount:", self.__price)


# Test Script
p = Product()
p.set_price(-50)     # invalid
p.set_price(1000)
p.apply_discount(20)

# 5. Final balance getter use karte hue print kiya
print(f"Final balance: {account.get_balance()}")