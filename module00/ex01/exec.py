import sys

strings = sys.argv
del strings[0]
str = ""
for arg in strings:
	str += arg.swapcase() + " "
print(str)