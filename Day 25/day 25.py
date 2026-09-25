# Find the Largest Digit -----

num = 58321

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print("Largest digit:", largest)

# Count Even and Odd Digits -----

num = 58321

even_count = 0
odd_count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

    num = num // 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)

# Count Frequency of a Digit -----

num = 583825
target = 8

count = 0

while num > 0:
    digit = num % 10
if digit == target:
    count = count + 1

num = num // 10

print(target, "appears", count, "times")
