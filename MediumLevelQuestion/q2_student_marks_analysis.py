marks = [45, 78, 62, 89, 55, 92, 38, 76]

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

count = 0
for m in marks:
    if m > average:
        count = count + 1

marks.sort()

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Students above average:", count)
print("Marks in ascending order:", marks)
