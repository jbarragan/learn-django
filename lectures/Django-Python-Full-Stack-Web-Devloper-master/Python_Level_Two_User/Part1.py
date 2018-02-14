x = 25

def my_func():
    x = 50
    return x

print(x)
print(my_func())
print(x)

# LOCAL
lambda x: x**2

# Enclosing functions locals
name = "This is a global name!"

def greet():
    name = "sammy"

    def hello():
        print("hello {}".format(name))

    hello()

greet()
print(name)


# Builtin level
# len = 23 # Redefining len, avoid it.

x = 50

def func(x):
    print('x is: {}'.format(x))
    x = 1000
    print('local x changed to: {}'.format(x))

func(x)
print(x)


x = 50

def func():
    global x
    x = 1000
    print('global x changed to: {}'.format(x))

print("Before function call x = {}".format(x))
func()
print("After function call x = {}".format(x))
