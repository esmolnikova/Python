def generator(n):
    for i in range(1, n+1, 2):
        yield i

gener = generator(15)
for i in gener:
    print(i)
