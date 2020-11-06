n = 5
for i in range (1, n+1):
    for j in range (1, n+1):
        if i == j == (n//2)+1:
            print("O", end=" ")
        else:
            print("X", end=" ")
    print()