n = 5
a = 1
b = n * 2 - 1
for i in range(1, n + 1):
    for j in range(1, n * 2 + 1):
        if j == a or j == b:
            print("*", end="")
        else:
            print(" ", end="")
    a += 1
    b -= 1
    print()