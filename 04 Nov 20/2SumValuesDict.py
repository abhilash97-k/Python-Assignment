n = int(input("Enter the details:"))
d = {}
for i in range (n):
    print("Enter name of student")
    keys = input()
    print("Enter marks")
    values = int(input())
    d[keys] = values
print(d)
sum1 = sum(d[item] for item in d)
print (sum1)
