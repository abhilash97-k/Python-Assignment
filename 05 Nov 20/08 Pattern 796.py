n = 7
for i in range (1, n):
    if i % 2 != 0:
        c = i + 1
    else:
        c = c
    for j in range (0, c):
        print("*", end =" ")
    print()