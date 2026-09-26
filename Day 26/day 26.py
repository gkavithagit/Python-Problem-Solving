# First Non-Repeating Character -----

from collections import Counter

text = input ("Enter a string:")
count = Counter(text)

for char in text:
    if count[char] == 1:
        print(char)
        break

# Two Sum -----

numbers = [2, 7, 11, 15]
target = 9

seen = {}

for num in numbers:
    needed = target - num

    if needed in seen:
        print(needed, num)
        break

    seen[num] = True

# Check Anagram -----

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")