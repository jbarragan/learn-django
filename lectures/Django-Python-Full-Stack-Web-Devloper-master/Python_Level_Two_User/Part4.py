# INHERITANCE
class Animal():
    def __init__(self):
        print("Animal Created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("EATING")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("DOG EATING")

mya = Animal()
mya.whoAmI()
mya.eat()

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()

# SPECIAL METHODS
mylist = [1,2,3]
print(mylist)
print(len(mylist))

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Book: {} by {} with {} pages".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed!")


b = Book("Machine", "Toyota", 200)
print(b)
print(len(b))
del b
