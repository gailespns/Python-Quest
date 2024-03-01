import json

name = input("Please enter your name: ")
age = input("Please enter your age: ")
favorite_food = input("Enter your favorite food: ")

user_input = {
    "name": name,
    "age": age,
    "favorite_food": favorite_food
}

json_data = json.dumps(user_input, indent=2)

with open("output.json", "w") as file:
    file.write(json_data)
