# Lists
mylist = [1, 2, 3]
mylist = ["dsfdasd ", 1, 3, True, [1, 2, 3]]
print(mylist)
print(len(mylist))

mylist = ['a', 'b', 'c']
print(mylist[1])
print(mylist[1:])
print(mylist[:2])

print("Before")
print(mylist)
mylist[0] = "NEW ITEM"
print("After")
print(mylist)

mylist = ['a', 'b', 'c', 'd', 'e']
mylist.append("NEW ITEM")
print(mylist)

mylist = ['a', 'b', 'c', 'd', 'e']
mylist.append(['x', 'y', 'z'])
print(mylist)

mylist = ['a', 'b', 'c', 'd', 'e']
mylist.extend(['x', 'y', 'z'])
print(mylist)

mylist = ['a', 'b', 'c', 'd', 'e']
item = mylist.pop()
print(mylist)
print(item)

mylist = ['a', 'b', 'c', 'd', 'e']
item = mylist.pop(0)
print(mylist)
print(item)

mylist = ['a', 'b', 'c', 'd', 'e']
mylist.reverse()
print(mylist)

mylist = ['a', 'b', 'c', 'd', 'e']
mylist.reverse()
mylist.sort()
print(mylist)

mylist = [1, 2, ['x', 'y', 'z']]
print(mylist[2])
print(mylist[2][1])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# LIST COMPREHENSION
first_col = [row[0] for row in matrix]
print(first_col)
