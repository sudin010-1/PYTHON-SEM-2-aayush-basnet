def numbers():
    for i in range(1, 6):
        yield i


my_list = [1, 2, 3, 4, 5]
my_gen = numbers()

print("List:", my_list)
print("Generator:", my_gen)

for num in my_gen:
    print(num)
