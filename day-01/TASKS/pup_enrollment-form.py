# Write the code ↓ to read user's input.
# Be cautious when reading input of various data types.

print("\n")

name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gwa = float(input("Enter your previous general weighted average: "))
is_member = input("Are you a member of AWS Cloud Club? (yes/no): ").lower() == "yes"


# Write the code ↓ to display the user's personal information.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n")

print("Your enrollment form:")
print("Name:", name)
print("Age:", age)
print("GWA:", gwa)
print("Awstraunot:", is_member)
