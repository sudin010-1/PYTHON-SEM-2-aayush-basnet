numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter index: "))
    print("Value:", numbers[index])
except ValueError:
    print("Invalid input. Please enter an integer.")
except IndexError:
    print("Index out of range.")
finally:
    print("Program finished.")
