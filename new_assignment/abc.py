# wap to input from user if user provides 1 take another input and if the input is an even no
# add it to a list if it is not convertible to int add it to invalid input list and ask the user
# to provide input from beginning if user provides 2 quit and show the updated list.


even_list = []
invalid_list = []

def add_number():
    try:
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            even_list.append(num)
        else:
            print("Enter an even number.")

    except:
        invalid = input("Invalid input. Enter again: ")
        invalid_list.append(invalid)

while True:
    choice = input("Enter 1 to add number or 2 to quit: ")

    if choice == "1":
        add_number()

    elif choice == "2":
        print("Even numbers:", even_list)
        print("Invalid inputs:", invalid_list)
        break

    else:
        print("Invalid choice.")