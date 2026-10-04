# 6. Factorial Calculator
# Calculate the factorial of a number using a for loop.

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)
