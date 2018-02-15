# print("Hello) # Error
mylisthere = []
# print(mylist) # Error

try:
    f = open("simple.txt", "r")
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA")
except:
    print("ERROR: OTHER ERROR")
else:
    print("SUCCESS")
finally:
    f.close()

print("At the end")
