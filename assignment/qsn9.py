import math

sideA = float(input("Enter side A: "))
sideB = float(input("Enter side B: "))

sideC = math.sqrt(sideA * sideA + sideB * sideB)

print("The hypotenuse is", sideC)