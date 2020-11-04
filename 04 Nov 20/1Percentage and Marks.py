n = int(input("Enter the details:"))
d = {}
for i in range (n):
    keys = input()
    values = input()
    d[keys] = values
print(d)
for i in range (n):
    su = su + d[i]
print (su)
