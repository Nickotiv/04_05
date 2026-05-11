class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def info(self):
        return (f"Brand: {self.brand}, Speed: {self.speed} km/h")
    def honk(self):
        return "Beep beep!"
        
class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        self.brand = brand
        self.speed = speed
        self.doors = doors
        
    def info(self):
        return (f"Brand: {self.brand}, Speed: {self.speed} km/h, Doors: {self.doors}")
    def open_trunk(self):
        return "Trunk opened"
        
class Motorcycle(Vehicle):
    def __init__(self,brand, speed, has_sidecar):
        self.brand = brand
        self.speed = speed
        self.has_sidecar = has_sidecar
    def honk(self):
        return "Beep! (louder)"
        
    def wheelie(self):
        return "Doing a wheelie!"

car = Car("Toyota", 180, 4)

print(car.info())           #→ "Brand: Toyota, Speed: 180 km/h, Doors: 4"
print(car.honk())           #→ "Beep beep!"
print(car.open_trunk())     #→ "Trunk opened"

bike = Motorcycle("Harley", 120, False)

print(bike.info())          #→ "Brand: Harley, Speed: 120 km/h"
print(bike.honk())          #→ "Beep! (louder)"
print(bike.wheelie())       #→ "Doing a wheelie!"
#print(bike.open_trunk())    #→ AttributeError
