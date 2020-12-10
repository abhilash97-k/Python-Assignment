import time
class test:
    def _init_(self):
        print("Object Initalization")
    def _del_(self):
        print("Fulfilling last wish and performing cleanup activities...")
t1=test()
t1=None
time.sleep(5)
print("End of application")