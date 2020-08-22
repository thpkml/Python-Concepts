# Superclass
class Automobile:
    def __init__(self, brand, wheels, speed):
        self.brand = brand
        self.wheels = wheels
        self.speed = speed

    def horn(self):
        print("Honk!!")

# subclass
class Car(Automobile):
    def horn(self):
        print("Peeep!!") # overrides the horn method of its superclass

    def parentHorn(self):
        super().horn() # calls superclass' method

# subclass
class Bus(Automobile):
    def horn(self):
        print("Dong Dong!!")


# objects/instances
bmw = Car("BMW", 4, 240)
bigRed = Bus("Mercedes", 6, 120)

print(bmw.speed)
print(bigRed.speed)
bmw.horn()
bmw.parentHorn()
bigRed.horn()