import sys

if (len(sys.argv) > 3):
	print("too much args")
	exit(0)
elif (len(sys.argv) == 1):
	print()
	exit(0)
if (sys.argv[1].isalpha() == True and sys.argv[2].isalpha() == True):
        print("only integers")
        exit(0)
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

print("Sum:		",n1 + n2)
print("Difference:		",n1 - n2)
print("Product:		",n1 * n2)
if (n2 == 0):
	print("Quotient: ERROR (division by zero)")
else:
	print("Quotient:	",n1 / n2)
if (n2 == 0):
	print("Remainder: ERROR (modulo by zero)")
else:
	print("Remainder:	",n1 % n2)