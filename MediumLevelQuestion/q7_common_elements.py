list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80, 90]

both = []
only1 = []
only2 = []

for i in list1:
    if i in list2:
        both.append(i)
    else:
        only1.append(i)

for i in list2:
    if i not in list1:
        only2.append(i)

print("Present in both lists:", both)
print("Present only in list1:", only1)
print("Present only in list2:", only2)
