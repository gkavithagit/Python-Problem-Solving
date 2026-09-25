# Find the Second Largest Number -----

numbers = [10, 5, 8, 20, 15]

largest = numbers[0]
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second largest:", second_largest)

# Move All Zeros to the End -----

numbers = [0, 1, 0, 3, 12]

result = []
zero_count = 0

for num in numbers:
    if num == 0:
        zero_count == 1
    else:
        result.append(num)

for i in range(zero_count):
    result.append(0)

print(result)

# Find the Missing Number -----

numbers = [1, 2, 3, 5, 6]
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing = expected_sum - actual_sum
print("Missing number:'", missing)
