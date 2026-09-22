# Day 22 - Python Problem Solving

# Problem 1: Count digits

num = 58392
count = 0

while num > 0:
    count += 1
    num //= 10

print("Number of digits:". count)

# Problem 2: Sum of digits

num = 58392
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)

# Problem 3: Find largest digit

num = 58392
largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num //= 10

print("Largest digit:", largest)