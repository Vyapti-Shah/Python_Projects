# abstract class - a class which contains one or more abstract methods 
#                - Prevents a user from creating an object of that class
#                - compels a user to override abstract methods in a child class
# abstract method - a method that has a declarationn but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):  #abstract class
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("Stop the Car")

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("Stop the Motorcycle")

#vehicle = Vehicle()   #as it is an abstract class you cannot form a vehicle object
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()