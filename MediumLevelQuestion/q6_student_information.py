student = {
    "name": "Ram",
    "age": 19,
    "course": "BCA",
    "marks": 78
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])

student["marks"] = student["marks"] + 5

if student["marks"] >= 40:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

print("Updated dictionary:", student)
