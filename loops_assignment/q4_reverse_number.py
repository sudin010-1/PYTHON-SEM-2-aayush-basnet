# 4. Reverse a Number
# Reverse a given number using a loop.

num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse of", original, "is", reverse)
