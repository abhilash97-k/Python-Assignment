def out():
    print("Outer function")
    def inn():
        print("Inner function")
    print("outer calling inner")
    inn()



out()
