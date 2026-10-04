binary = input("Please enter an eight digit binary number: ")

decimal = 0

decimal = decimal + int(binary[0]) * 128
decimal = decimal + int(binary[1]) * 64
decimal = decimal + int(binary[2]) * 32
decimal = decimal + int(binary[3]) * 16
decimal = decimal + int(binary[4]) * 8
decimal = decimal + int(binary[5]) * 4
decimal = decimal + int(binary[6]) * 2
decimal = decimal + int(binary[7]) * 1

print("The decimal equivalent of", binary, "is", decimal)