import DirModule1
from DirModule1 import *
def priFun():
    print(__name__)
    if __name__ == '__main__':
        print("Print Data from Prog")
    else:
        print("Data from module")
    print(div(4, 4))
priFun()
import math
help(math)