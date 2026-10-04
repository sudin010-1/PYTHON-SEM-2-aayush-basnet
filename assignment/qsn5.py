cm = float(input("How many centimetres do you want to convert? "))

inches = cm / 2.54

yards = int(inches / 36)
inches = inches - yards * 36

feet = int(inches / 12)
inches = inches - feet * 12

print("This is", yards, "yards,", feet, "feet,", inches, "inches.")