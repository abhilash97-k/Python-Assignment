a = ["a", "b", "c", "d", "e", "f"]
b = ["a", "a", "a", "a", "a", "a"]
print(all(c == 'b' for c in a))
print(all(c == 'a' for c in b))