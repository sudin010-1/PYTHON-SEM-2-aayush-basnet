def even_numbers():
    for i in range(10):
        yield i * 2


for num in even_numbers():
    print(num)
