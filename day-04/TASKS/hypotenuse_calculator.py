import math

# Write the code ↓ to read the lengths of the two shorter sides of a right-angled triangle from the user.
# Be cautious when reading input of various data types.

print("\n")

print("HYPOTENUSE CALCULATOR FOR ALF!")

print("\n")

side_A = float(input("Please, enter the length of side A: "))
side_B = float(input("Please, enter the length of side B: "))

result = 0.0


# Write the code ↓ to calculate the hypotenuse using the Pythagorean theorem.
# The Pythagorean theorem: c^2 = a^2 + b^2, where c is the hypotenuse.

result = math.sqrt(math.pow(side_A, 2) + math.pow(side_B, 2))


# Write the code ↓ to display the calculated hypotenuse.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("The hypothenuse of the right-angled triangle is: {:.2f}".format(result))
