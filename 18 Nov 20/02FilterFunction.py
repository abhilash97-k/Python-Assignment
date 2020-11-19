def isEven(x):
    if x % 2 == 0:
        return x
    else:
        return False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = list(filter(isEven, l))
print(x)