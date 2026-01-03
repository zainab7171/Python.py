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