# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.

print("\n")

print("SIMPLE CALCULATOR FOR ALF!")

print("\n")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ")


# Write the code ↓ to perform the calculations based on the selected operation.

if operator == "+":
    ans = first_number + second_number
elif operator == "-":
    ans = first_number - second_number
elif operator == "x":
    ans = first_number * second_number
else:
    ans = first_number / second_number


# Write the code ↓ to display the result.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n")

print("The result of", first_number, operator, second_number, "is {:.2f}".format(ans))

