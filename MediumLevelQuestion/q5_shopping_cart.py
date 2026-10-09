# 5. Shopping Cart

cart = ["apple", "milk", "bread", "apple", "eggs", "milk"]
print("Original cart:", cart)

cart = list(set(cart))      # remove duplicate items
cart.append("cheese")       # add cheese
cart.remove("bread")        # remove bread
cart.sort()                 # sort alphabetically

print("Final cart:", cart)
print("Number of different items:", len(cart))
