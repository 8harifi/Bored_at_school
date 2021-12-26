import sys

if len(sys.argv) == 1:
    equation = input("> ")
elif len(sys.argv) == 2:
    equation = sys.argv[1]
else:
    print("Wrong Usage !!")

