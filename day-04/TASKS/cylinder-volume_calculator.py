import math

# Write the code ↓ to read the radius and height of a cylinder from the user.
# Be cautious when reading input of various data types.

print("\n")
      
radius= float(input("Please, enter the radius of cylinder: "))
height = float(input("Please, enter the height of cylinder: "))
result = 0.0
pi = 3.14159


# Write the code ↓ to calculate the volume of the cylinder using the formula V = πr^2h.
# Formula to calculate the volume (V) of a cylinder:
# V = π * r^2 * h

result = pi * math.pow(radius,2) * height


# Write the code ↓ to display the calculated volume with 2 decimal places.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n")

print ("The hypotenuse of the right-angled triangle is: {:.2f}".format(result))
