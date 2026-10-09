name = input("Enter your full name: ")

name = name.strip()
words = name.split()
username = "_".join(words)
username = username.lower()

print("Username:", username)
