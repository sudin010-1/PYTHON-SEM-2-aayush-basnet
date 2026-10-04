number = int(input("Please enter a number: "))

original = number

binary = ""

if number >= 128:
    binary = binary + "1"
    number = number - 128
else:
    binary = binary + "0"

if number >= 64:
    binary = binary + "1"
    number = number - 64
else:
    binary = binary + "0"

if number >= 32:
    binary = binary + "1"
    number = number - 32
else:
    binary = binary + "0"

if number >= 16:
    binary = binary + "1"
    number = number - 16
else:
    binary = binary + "0"

if number >= 8:
    binary = binary + "1"
    number = number - 8
else:
    binary = binary + "0"

if number >= 4:
    binary = binary + "1"
    number = number - 4
else:
    binary = binary + "0"

if number >= 2:
    binary = binary + "1"
    number = number - 2
else:
    binary = binary + "0"

if number >= 1:
    binary = binary + "1"
else:
    binary = binary + "0"

print("The binary equivalent of", original, "is", binary)