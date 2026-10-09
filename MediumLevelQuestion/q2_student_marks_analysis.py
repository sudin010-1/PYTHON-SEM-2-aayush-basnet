# 2. Student Marks Analysis

marks = [45, 78, 62, 89, 55, 92, 38, 76]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above_average = 0
for mark in marks:
    if mark > average:
        above_average += 1

print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", round(average, 2))
print("Students above average:", above_average)
print("Marks in ascending order:", sorted(marks))
