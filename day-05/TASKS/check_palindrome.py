# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.

print("\n")

print("PALINDROME CHECKER FOR ALF!")

print("\n")

word = input("Please, enter a word/s to check: ")
wordLower = word.lower()


# Write the code ↓ to check if the entered word is a palindrome.
# Utilize string functions to compare the original word with its reverse.

reverse = ""

for char in wordLower:
    reverse = char + reverse


# Write the code ↓ to display whether the entered word is a palindrome or not.
# Select and employ a string concatenation method based on your personal preference and comfort level.

print("\n")

if wordLower == reverse:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
