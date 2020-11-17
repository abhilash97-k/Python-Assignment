def FibSer(n):
    if n <= 1:
        return n
    else:
        return FibSer(n - 1) + FibSer(n - 2)
print("Fibonacci series:")
for i in range(10):
    print(FibSer(i))