class Dog():
    # Class object attribute
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

mydog = Dog("Lab", "Sammy")
print(type(mydog))
print(mydog.breed)
print(mydog.name)
print(type(mydog.breed))


otherdog = Dog(breed="Huskie", name="Colors")
print(otherdog.breed)
print(otherdog.name)
print(otherdog.species)


class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle()
myc.set_radius(100)
print(myc.radius)
print(myc.area())
