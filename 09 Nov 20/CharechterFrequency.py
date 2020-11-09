a = "Hello World"
for n in a:
    keys = d.keys()
    if n in keys:
        d[n] += 1
    else:
        d[n] = 1