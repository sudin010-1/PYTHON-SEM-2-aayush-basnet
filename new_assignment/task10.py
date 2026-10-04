def cube_gen(nums):
    for n in nums:
        yield n ** 3


numbers = []

try:
    for i in range(1, 6):
        num = int(input("Enter number " + str(i) + ": "))
        numbers.append(num)

    squares = [n * n for n in numbers]
    print()
    print("Squares:", squares)

    print()
    print("Cubes:")
    for c in cube_gen(numbers):
        print(c)
except ValueError:
    print("Invalid input. Please enter numbers only.")
finally:
    print()
    print("Thank you for using the program.")
