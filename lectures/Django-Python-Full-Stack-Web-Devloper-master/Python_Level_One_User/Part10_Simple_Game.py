###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])
result = digits[:3]

# Another hint:

def matches(a1, a2):
    count = 0
    for i,v1 in enumerate(a1):
        if v1 == a2[i]: count+=1
    return count

def closes(a1, a2):
    count = 0
    for v1 in a1:
        if v1 in a2: count+=1
    return count

while True:
    guess = input("What is your guess? ")
    print(guess)
    if len(guess) != 3 or not guess.isdigit():
        print("Enter a 3 digits number")
        continue
    guess = list(map(int, list(guess)))
    m = matches(result, guess)
    if m == 3:
        print("You are correct!!!")
        break
    if m > 0:
        print("Match")
        continue
    c = closes(result, guess)
    if c > 0:
        print("Close")
    else:
        print("Nope")

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
