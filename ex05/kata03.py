kata = "the right format"

i = "";
if(len(kata) > 42):
    print("kata lenght should be less or equal to 42")
    exit(0)
chunk = len(kata)
while(len(i) != 42 - chunk - 1):
    i += '-'
i += kata
print(i) 