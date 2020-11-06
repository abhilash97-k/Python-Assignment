n = 5
for i in range (1, n+1):
    for j in range (1, n+1):
        if i == j == (n//2)+1:
            print("0", end=" ")
        elif i == (n//2)+1 or j == (n//2)+1:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()