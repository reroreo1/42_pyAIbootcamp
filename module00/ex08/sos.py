from nis import cat
import sys
from warnings import catch_warnings

morse = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', ' ':'/', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
i = 1
chunk = ""
encrypt = ''
if(len(sys.argv) == 1):
    exit(0)
while (i < len(sys.argv)):
    chunk += sys.argv[i]
    if (i < len(sys.argv) - 1):
        chunk += ' '
    i += 1
print(chunk)
for letter in chunk:
    try:
            encrypt += morse[letter.upper()]
    except:
        encrypt = "error"
        break
print(encrypt)

