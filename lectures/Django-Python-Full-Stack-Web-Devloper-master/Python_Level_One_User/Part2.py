# STRINGS

'hello'
"hello"

"I'm Jaime"

mystring = 'abcdefg'
print(mystring)

# Indexing
print(mystring[0])
print(mystring[-1])
print(mystring[3])

# Slicing
print(mystring[2:])
print(mystring[4:])
print(mystring[:3])
print(mystring[2:5])
print(mystring[:])
print(mystring[::-1])
print(mystring[::-2])

# Basic Methods
x = mystring.upper()
print(x)
print(x.lower())
print(x.capitalize())
mystring = "Hello World"
x = mystring.split()
print(x)
x = mystring.split("o")
print(x)

# Print Formatting
x = "Insert another string here: {}".format("INSERT ME!")
print(x)
x = "Item One: {} Item Two: {}".format("dog", "cat")
print(x)
x = "Item One: {y} Item Two: {x}".format(x = "dog", y = "cat")
print(x)
x = "Item One: {y} Item Two: {y}".format(x = "dog", y = "cat")
print(x)
