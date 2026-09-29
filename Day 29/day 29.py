# Compress a String -----

from itertools import groupby

text = "aaabbccccd"

result = ""

for char, group in groupby(text):
    result += char + str(len(list(group)))

print(result)

# Sum of Digits Until One Digit Remains -----

num = 9875

while num >= 10:

    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    num = total

print(num)

# Convert Decimal to Binary -----

num = 10
binary = ""

while num > 0:
    remainder = num % 2
    binary = str(remainder) + binary 
    num = num // 2

print(binary)