# Problem 1: Character Frequency -----

word = "banana"

count = {}

for char in word:
    if char in count:
        count[char] = count[char] + 1
    else:
        count[char] = 1

print(count)

# Problem 2: First Non-Repeating Character -----

word = "aabbcdd"

count = {}

for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for char in word:
    if count[char] == 1:
        print(char)
        break

# Problem 3: Remove Duplicated from a List -----

numbers = [1,2,2,3,4,4,5]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)


