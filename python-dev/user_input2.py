# Exercise: User Input in Python
# Objective: To learn how to take user input in Python
# Task: Write a program that asks the user for their name, age, and location and then prints out a personalized message.

# Instructions:
# Use the input() function to ask the user for their name and store it in a variable called "name".

name = input("What is your name? ")

# Use the input() function to ask the user for their age and store it in a variable called "age".

age = input("How old are you? ")

# Use the input() function to ask the user for their location and store it in a variable called "location".

location = input("Where do you live? ")

# Print out a personalized message using the user's name, age, and location.
# For example: "Hello [name], you are [age] years old and live in [location]."
# Save and run the program to see the output.

message = f"Hello {name}, you are {age} years old and live in {location}"

#print(f"Hello {name}, you are {age} years old and live in {location}")

print(message)