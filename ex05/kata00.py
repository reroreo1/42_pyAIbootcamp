kata = (19, 42, 21)
if(isinstance(kata,tuple) and len(kata) == 0):
    print("There are no numbers")
elif(isinstance(kata,int)):
    print("The number is {}".format(kata))
elif(len(kata) > 1):
    s = "{}".format(kata[0])
    i = 1
    while (i < len(kata)):
        s += ", {}".format(kata[i])
        i += 1
print("the {} numbers are : {}".format(i,s))