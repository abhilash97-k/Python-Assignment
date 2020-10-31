n = 5
for i in range (n):
    print(' '*(n-i-1)+(chr(i+1+64)+' ')*(i+1))
for i in range (n):
    print(' '*(i+1)+(chr(n-i-1+64)+' ')*(n-i-1))