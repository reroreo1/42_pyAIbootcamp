import sys

if(len(sys.argv) != 3):
    print("oops u need to enter the right number of arguments")
    exit(0)
line = sys.argv[1]
while True:
    try:
        x = int(sys.argv[2])
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
tab = line.split()
for word in tab:
    if(len(word) < x):
        tab.remove(word)
print(tab)
