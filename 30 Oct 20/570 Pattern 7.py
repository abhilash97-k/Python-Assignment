n = 5
for i in range (n):
    print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
for i in range (n):
    print(' '*(i+1)+(str(n-i-1)+' ')*(n-i-1))