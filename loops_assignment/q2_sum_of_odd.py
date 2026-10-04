# 2. Sum of Odd Numbers
# Calculate the sum of all odd numbers from 1 up to a given number n.

n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        total += i

print("Sum of odd numbers from 1 to", n, "is", total)
