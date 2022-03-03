kata = (0,4,132.4222,10000,12345.67)

mod = ""
ex = ""
if(len(kata) == 5):
    if(kata[0] < 10):
        mod = "0"
    if(kata[1] < 10):
        ex = "0"
    print("module_{}{}, ex_{}{} : {:.2f}, {:.2e}, {:.2e}".format(mod,kata[0],ex,kata[1],kata[2],kata[3],kata[4]))
else:
    print("u need 5 elements in the kata")