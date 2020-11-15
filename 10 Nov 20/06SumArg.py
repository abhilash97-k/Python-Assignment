def su(*args):
    a = 0
    for i in args:
        a = a + i

    return a

print(su(2, 4, 6, 8, 10))
