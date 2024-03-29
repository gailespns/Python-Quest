# BMI - NUTRITIONAL STATUS GUIDE
"""
    BMI         NUTRITIONAL STATUS

BELOW 18.5         UNDERWEIGHT
18.5 - 24.9       NORMAL WEIGHT
25.0 - 29.9        OVERWEIGHT
ABOVE 30.0          OBESITY
"""
 
# Write the code ↓ to read user's height and weight.
# Be cautious when reading input of various data types.

print("\n")

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))


# Write the code ↓ to perform the calculations of user's BMI and categorize its status.

BMI = (weight / (height**2))

if BMI < 18.5:
    NUTRITIONAL_STATUS = ("UNDERWEIGHT")
elif BMI > 18.5 and BMI < 24.9:
    NUTRITIONAL_STATUS = ("NORMAL WEIGHT")
elif BMI > 25 and BMI < 29.9:
    NUTRITIONAL_STATUS = ("OVERWEIGHT")
else:
    NUTRITIONAL_STATUS = ("OBESITY")


# Write the code ↓ to display the user's BMI and its classification.
# Select and employ a string concatenation method based on your personal preference and comfort level.
# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.

print("\n")

print("HEIGHT: ", height, "-", "WEIGHT: ", weight)
print("BMI: {:.2f}".format(BMI), "-", "NUTRITIONAL STATUS: ", NUTRITIONAL_STATUS)
