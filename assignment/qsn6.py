cost = float(input("How much did the item cost: "))
money = float(input("How much did the person give you: "))

change = money - cost

print("The person's change is $", change)

change = int(change * 100)

twenties = change // 2000
change = change % 2000

tens = change // 1000
change = change % 1000

fives = change // 500
change = change % 500

ones = change // 100
change = change % 100

quarters = change // 25
change = change % 25

dimes = change // 10
change = change % 10

nickels = change // 5
change = change % 5

pennies = change

print(twenties, "twenties")
print(tens, "tens")
print(fives, "fives")
print(ones, "ones")
print(quarters, "quarters")
print(dimes, "dimes")
print(nickels, "nickels")
print(pennies, "pennies")