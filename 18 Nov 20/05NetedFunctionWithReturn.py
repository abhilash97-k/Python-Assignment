def out():
    print("Outer function")
    def inn():
        print("Inner function")
    print("outer calling inner")
    return inn



f1 = out()
f1()
f1()