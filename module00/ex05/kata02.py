kata = (1, 1, 1, 1, 1)

m = ""
d = ""
y = ""
h = ""
mini = ""
if(len(kata) == 5):
    if(kata[0] < 1000):
        y = "0"
    if(kata[0] < 100):
        y = "00"
    if(kata[0] < 10):
        y = "000"
    if(kata[1] < 10):
        m = "0"
    if(kata[2] < 10):
        d = "0"
    if(kata[3] < 10):
        h = "0"
    if(kata[4] < 10):
        mini = "0"
    print("{}{}/{}{}/{}{} {}{}:{}{}".format(m,kata[1],d,kata[2],y,kata[0],h,kata[3],mini,kata[4]))
else :
    print("you should put 5 positive digits in the kata")