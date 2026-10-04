# 5. Find the First Repeated Character
# Given a string, find the first character that appears more than once.

text = input("Enter a string: ")
seen = []
repeated = None

for ch in text:
    if ch in seen:
        repeated = ch
        break
    seen.append(ch)

if repeated:
    print("First repeated character:", repeated)
else:
    print("No repeated character found.")
