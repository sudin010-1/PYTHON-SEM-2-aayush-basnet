# 3. Multiplication Table Printer
# Print the multiplication table for a given number up to 10,
# but skip the third iteration.

num = int(input("Enter a number: "))

for i in range(1, 11):
    if i == 3:
        continue  # skip the third iteration
    print(num, "x", i, "=", num * i)
