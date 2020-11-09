a = int(input())
b = int(input())
ch  = input()
def mat(a, b, ch):
    if ch == '+':
        print(a + b)
    elif ch == '-':
        print(a - b)
    elif ch == '*':
        print(a*b)
    else:
        print(a/b)
mat(a, b, ch)