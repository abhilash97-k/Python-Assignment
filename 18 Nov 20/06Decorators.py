def wish(name):
    print("Hello", name, "Good morning")

def decor(func):
    def inner(name):
        if name == "Sunny":
            print("Hello Sunny Bad Morning")
        else:
            func(name)
    return inner

@decor
def wish(name):
    print("Hello", name, "Good Morning")

wish("Sunny")
wish("Rahul")