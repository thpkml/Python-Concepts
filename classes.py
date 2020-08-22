# name a class 'Dog'

class Dog:
    # define its constructor
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color

    # define Dog's methods
    def bark(self):
        print("Woof!")


# Create an instance/object of class Dog
dawg = Dog("Dawg", "lab", "chocolate")
# call dawg's color
print(dawg.color)
# call dawg's bark method
dawg.bark()

# Create more dogs and play around
jiju = Dog("Jiju", "bull", "grey")
teeni = Dog("Teeni", "poodle", "white")

print(teeni.name + " goes: ")
teeni.bark()
print(jiju.name + " says: " + teeni.name + " is a " + teeni.color + " " + teeni.breed)
