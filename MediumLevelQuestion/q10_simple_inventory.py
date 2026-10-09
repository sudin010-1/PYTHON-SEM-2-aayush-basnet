inventory = {
    "apple": 20,
    "banana": 15,
    "mango": 10,
    "orange": 8
}

item = input("Enter item name: ")
item = item.lower()

if item in inventory:
    sold = int(input("How many were sold? "))
    inventory[item] = inventory[item] - sold
    if inventory[item] <= 0:
        del inventory[item]
else:
    print("Item not found")

print("Updated inventory:", inventory)
