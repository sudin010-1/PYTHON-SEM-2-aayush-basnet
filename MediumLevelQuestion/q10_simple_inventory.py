# 10. Simple Inventory

inventory = {
    "apple": 20,
    "banana": 15,
    "mango": 10,
    "orange": 8
}

item = input("Enter an item name: ").strip().lower()

if item in inventory:
    sold = int(input("How many " + item + " were sold? "))

    if sold > inventory[item]:
        print("Not enough stock! Only", inventory[item], "available.")
    else:
        inventory[item] -= sold
        if inventory[item] == 0:
            del inventory[item]
            print(item, "is out of stock and removed from inventory.")
else:
    print("Item not found in inventory.")

print("Updated inventory:")
for name, qty in inventory.items():
    print(name, ":", qty)
