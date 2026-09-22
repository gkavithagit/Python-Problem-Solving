# ----- Python Problem Solving ----

# ---- 1. Reverse a number -----

number = 12345
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print(reverse)

# ----- 2. Check Palindrome number -----

number = 1221
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")