# %% Vehicle Hierarcy
from abc import ABC, abstractmethod
class Vehicle:
    def __init__(self,make,model):
        self.make = make 
        self.model = model
    def describe(self):
        return f"This car is {self.model} {self.make}"
    @abstractmethod
    def wheels(self):
        pass
     
class Truck(Vehicle):
    def __init__(self, make, model,capacity):
        super().__init__(make, model)
        self.capacity = capacity
    def describe(self):
       base = super().describe()
       return f"{base} (capacity: {self.capacity})"
    def wheels(self):
        return 8

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def wheels(self):
        return 4
vehicles = [Car("Toyota", "Corolla"), Truck("Ford", "F150", 1000), Car("Honda", "Civic")]

for v in vehicles:
    print(f"{v.describe()} - {v.wheels()} wheels" )
        