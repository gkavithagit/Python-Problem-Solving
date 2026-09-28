# Find the Longest Word in a sentence -----

sentences = "Python programming is interesting"

words = sentences.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)

# Count the Number of words in a Sentence -----

sentence = "Python is easy to learn"

words = sentence.split()

count = 0

for word in words:
    count += 1

print(count)

# Remove Duplicate Chracters From a String -----

text = "Programming"

seen = set()
result = ""

for char in text:
    if char not in seen:
        result += char
        seen.add(char)

print(result)