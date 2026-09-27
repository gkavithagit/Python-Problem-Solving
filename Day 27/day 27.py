# Comm Elements Between Two Lists -----

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print(common)

# Largest Difference Between Two Elements -----

numbers = [2, 7, 4, 10, 3]

smallest = numbers[0]
largest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

    if num > largest:
        largest = num

difference = largest - smallest

print(difference)

# All Pairs With a Given Sum -----

numbers = [2, 4, 3, 5, 7, 8]
target = 10

seen = set()

for num in numbers:
    needed = target - num

    if needed in seen:
        print(needed, num)

    seen.add(num)