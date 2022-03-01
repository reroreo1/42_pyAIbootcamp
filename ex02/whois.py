import sys

n = len(sys.argv)

if n != 2:
    print("error")
    exit(0)

digit = int(sys.argv[1])
if (digit == 0):
    print("I m Zero")
elif (digit % 2 == 1):
    print("I m Odd")
elif (digit % 2 == 0):
    print("I m Even")

