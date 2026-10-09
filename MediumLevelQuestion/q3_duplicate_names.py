# 3. Duplicate Names
# Create a collection containing only unique names.

names = ["Ram", "Sita", "Hari", "Ram", "Anu", "Sita", "Mina"]

unique_names = set(names)   # a set keeps only unique values

print("Total unique students:", len(unique_names))
print("Unique names in alphabetical order:", sorted(unique_names))
