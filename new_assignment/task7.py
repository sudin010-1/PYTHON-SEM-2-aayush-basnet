def count_numbers():
    for i in range(1, 11):
        yield i


for num in count_numbers():
    print(num)
