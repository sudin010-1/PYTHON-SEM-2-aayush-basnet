# 7. Common Elements

list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80, 90]

set1 = set(list1)
set2 = set(list2)

common = sorted(set1 & set2)       # intersection
only_list1 = sorted(set1 - set2)   # difference
only_list2 = sorted(set2 - set1)

print("Values present in both lists:", common)
print("Values present only in list1:", only_list1)
print("Values present only in list2:", only_list2)
