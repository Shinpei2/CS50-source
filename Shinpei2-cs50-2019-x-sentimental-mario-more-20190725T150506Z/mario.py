# importing get_int
from cs50 import get_int

height = 0

# prompt to input height until height is between 1 and 8
while True:
    height = get_int("Height: ")
    if 1 <= height <= 8:
        break

# print("Success!", height)

# print blank and block

# print 1 record
for i in range(height):

    # print blank spaces
    blank = height - 1 - i
    for j in range(blank):
        print(" ", end="")

    # print left blocks
    for j in range(i+1):
        print("#", sep="", end="")

    # blank (2 spases)
    print("  ", end="")

    # print right blocks
    for j in range(i+1):
        print("#", sep="", end="")

    # go to a new line
    print("")

