def func():
    return 1

print(func())

s = "GLOBAL VARIABLE!"

def func():
    s = 50
    print(s)

func()
print(s)


def func():
    global s
    s = 50
    print(s)

func()
print(s)

def func():
    print(locals())
    print(globals())
    print(globals()['s'])

func()

def hello(name="Jaime"):
    return "Hello {}".format(name)

print(hello())

mynewgreet = hello

print(mynewgreet())


def hello(name="Jaime"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    def greet():
        return "THIS STRING IS INSIDE GREET()"

    def welcome():
        return "THIS STRING IS INSIDE WELCOME()"

    print(greet())
    print(welcome())
    print("End of Hello()")

hello()

def hello(name="Jaime"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    def greet():
        return "THIS STRING IS INSIDE GREET()"

    def welcome():
        return "THIS STRING IS INSIDE WELCOME()"

    if name == "Jaime":
        return greet
    else:
        return welcome

x = hello()
print(x())
x = hello("Jose")
print(x())

def hello():
    return "Hi Jaime!"

def other(func):
    print("HELLO")
    print(func())

other(hello)


def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("CODE HERE AFTER EXECUTING FUNC")

    return wrap_func

def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")


func_needs_decorator()
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()


@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")

func_needs_decorator()
