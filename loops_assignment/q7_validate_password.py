# 7. Validate Password
# Keep asking the user to enter a password until they enter "python123".

password = input("Enter password: ")

while password != "python123":
    print("Wrong password. Try again.")
    password = input("Enter password: ")

print("Access granted!")
