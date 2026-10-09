# 6. Student Information Dictionary

student = {
    "name": "Ram",
    "age": 19,
    "course": "BCA",
    "marks": 78
}

print("Student Information:")
for key, value in student.items():
    print(key, ":", value)

# Increase marks by 5
student["marks"] = student["marks"] + 5

# Add status key
if student["marks"] >= 40:
    student["status"] = "Pass"
else:
    student["status"] = "Fail"

print("\nUpdated Dictionary:")
print(student)
