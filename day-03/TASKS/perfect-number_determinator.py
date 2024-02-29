# Write the code ↓ to read the user's input for a positive integer.
# Be cautious when reading input of various data types.

print("\n")

print("PERFECT NUMBER DENOMINATOR FOR ALF")

print("\n")

num = int(input("Enter a non-negative integer: "))

while num < 0:
    print("Please enter a non-negative integer.")
    num = int(input("Enter a non-negative integer: "))


# Write the code ↓ to check if the entered integer is a Perfect Number using a loop.

result = 0

for i in range(1, num):
    if num % i == 0:
        result += i


# Write the code ↓ to display the Perfect Number check result.
# NOTE : You can use if-else statement or ternary operator to display the result.

print("\n")

if num == result:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")
