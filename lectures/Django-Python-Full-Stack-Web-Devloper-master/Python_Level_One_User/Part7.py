# COMPARISON OPERATORS
# Greater than
1 > 2
# Less than
1 < 2
# Greater than or equal to
1 >= 1
# Less than or equal to
1 <= 1
# Equality
1 == 1
1 == "1" # False
"hi" == "bye"

# LOGICAL OPERATORS
# and
(1 > 2) and (2 < 3)
# or
(1 > 2) or (2 < 3)


# IF
if 1<2:
    print("yes!")

if 1<2:
    if 2 < 3:
        print("yes!")

if 1<2:
    print("First Block")
    if 20 < 3:
        print("Second Block")

if 10 < 2:
    print("Hello")
else:
    print("Last")

if 10 < 2:
    print("Hello")
elif 3 == 3:
    print("elif")
else:
    print("Last")

# FOR LOOPS
seq = [1, 2, 3, 4, 5, 6]
for item in seq:
    print(item)

d = {"Sam": 1, "Frank": 2, "Dan": 3}
for item in d:
    print(item)

for k in d:
    print(d[k])

mypairs = [(1,2), (3,4), (5,6)]
for pair in mypairs:
    print(pair)

for (tup1, tup2) in mypairs:
    print(tup2)
    print(tup1)

for tup1, tup2 in mypairs:
    print(tup2)
    print(tup1)

i = 1
while i < 5:
    print("i is: {}".format(i))
    i = i+1

my_list = list(range(0,5))
print(my_list)

my_list = list(range(0,20,2))
print(my_list)

for item in range(10):
    print(item)

x = [1, 2, 3, 4]

out = []

for num in x:
    out.append(num**2)

print(out)

print([num**2 for num in x])
