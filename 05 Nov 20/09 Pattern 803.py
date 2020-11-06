n = 7
for i in range (1, n):
    if i % 2 != 0:
        c = i + 1
    else:
        c = i
    for j in range (n-1, c, -1):
        print(" ", end =" ")
    for k in range (0, c):
        print("*", end = " ")
    print()