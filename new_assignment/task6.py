numbers = [12, 5, 8, 21, 10, 33, 16, 7]

greater = [x for x in numbers if x > 10]
odd = [x for x in numbers if x % 2 != 0]
cubes = [x ** 3 for x in numbers]

print("Greater than 10:", greater)
print("Odd numbers:", odd)
print("Cubes:", cubes)
