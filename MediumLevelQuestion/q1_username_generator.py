# 1. Username Generator
# Ask the user to enter their full name and create a username by
# removing extra spaces, converting to lowercase and joining words with "_".

full_name = input("Enter your full name: ")

words = full_name.split()          # split() removes all extra spaces
username = "_".join(words).lower()

print("Username:", username)
