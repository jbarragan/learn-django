def my_func(param1="default"):
    """
    THIS IS THE DOCSTRING
    """
    print("my first python function! {}".format(param1))

my_func()

def hello():
    return "hello"

print(hello())

def addNum(num1, num2):
    if type(num1)==type(num2)==type(10):
        return num1+num2
    else:
        return "Sorry, I need integers"

print(addNum(2, 4))
print(type(addNum(2, 4)))
print(addNum("2", "4"))
print(type(addNum("2", "4")))

# Lambda Expression

# Filter
my_list = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0

even = filter(even_bool, my_list)
print(even)
print(list(even))

even = filter(lambda num:num%2 == 0, my_list)
print(even)
print(list(even))

st = "hello"
st.lower()
st.upper()
st.split()

tweet = "Go Sports! #Sports"
tweet.split("#")
result = tweet.split("#")
print(result)

print('x' in [1,2,3])
print('x' in [1,2,3,'x'])
