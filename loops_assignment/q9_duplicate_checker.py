# 9. List Duplicate Checker
# Check whether a list contains duplicate elements.
# If a duplicate is found, exit the loop and print the duplicate.

items = ["red", "blue", "green", "red", "yellow"]
checked = []
duplicate = None

for item in items:
    if item in checked:
        duplicate = item
        break  # exit the loop when duplicate is found
    checked.append(item)

if duplicate:
    print("Duplicate found:", duplicate)
else:
    print("No duplicates found.")
