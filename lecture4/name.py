import sys

if len(sys.argv) < 2:
    print("Too few argumnets")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("My name is, ", sys.argv[1])