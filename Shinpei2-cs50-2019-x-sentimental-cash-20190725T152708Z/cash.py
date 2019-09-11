# importing get_float
from cs50 import get_float

# prompt to input cash by float until the value is valid
cash = 0
while True:
    cash = get_float("Change owed: ")
    if 0 < cash:
        break

# cash convert dollars
cash = cash * 100

# count the number of coins
count = 0

# count 25pence coins
while cash >= 25:
    cash -= 25
    count += 1

# count 10pence coins
while cash >= 10:
    cash -= 10
    count += 1

# count 5pence coins
while cash >= 5:
    cash -= 5
    count += 1

# count 1pence coins
while cash >= 1:
    cash -= 1
    count += 1

# print coin counts
print(count)