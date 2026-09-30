# Find the Majority Element -----

nums = [2, 2, 1, 2, 3, 2, 2]

candidate = None
count = 0

for num in nums:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)

# Find Elements that Appears Only Once -----

nums = [4, 2, 7, 2, 4, 9, 5]

result = []

for num in nums:
    if nums.count(num) == 1:
        result.append(num)

print(result)

# Rotate a List to the Right by K Positions -----

nums = [1, 2, 3, 4, 5]
k = 2

k = k % len(nums)

nums.reverse()

nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:])

print(nums)