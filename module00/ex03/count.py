import string 
import sys

def text_analyzer(jomla):
    upper = 0
    lower = 0
    punc = 0
    space = 0
    if (isinstance(jomla, str) == False):
        print("error")
        exit(0)
    if (bool(jomla) == False):
        x = input("what is the text to analyze")
        jomla = x
    print("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles")
    for char in jomla:
        if(char.isupper() == 1):
            upper += 1
        elif(char.islower() == 1):
            lower += 1
        elif(char.isspace() == 1):
            space += 1
        elif(char in string.punctuation):
            punc  += 1
    print("The text contains" ,len(jomla), "character(s) :")
    print("- " , lower," lower letter(s)")
    print("- " , upper," upper letter(s)")
    print("- " , punc," punctuation mark(s)")
    print("- " , space," space(s)")

n = len(sys.argv)
if (n > 2):
    print("error")

text_analyzer(sys.arg[1])



