# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.

print("\n")

print("FACTORIAL CALCULATOR FOR ALF!")

print("\n")

nn_integer = int(input("Please, enter a non-negative integer: "))

# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.

num = nn_integer
result = 1 # initialize starting value

while num > 0:
  result *= num
  num -= 1 


# Write the code ↓ to display the factorial result.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n")

print("The factorial of", str(nn_integer), "is", result)
