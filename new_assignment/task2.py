try:
    num = int(input("Enter an integer: "))
    print("Square:", num * num)
except ValueError:
    print("Invalid input. Please enter an integer.")
finally:
    print("Program execution completed.")
