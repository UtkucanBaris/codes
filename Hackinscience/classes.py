# class Vehicle:
#     def __init__(self,maxspeed,vites):
#         self.maxspeed = maxspeed
#         self.vites = vites
# mod=Vehicle(240,18)
# print(mod.maxspeed,mod.vites)

# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 180, 12)
# print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
# class Bus(Vehicle):
#     def seating_capacity(self,capacity=50):
#         return super(Bus, self).seating_capacity(capacity=50)
# schoolbus=Bus("School Volvo", 180, 12)
# print(schoolbus.seating_capacity())

class Vehicle:
    # Class attribute
    color = "White"

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

