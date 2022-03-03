kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

if(len(kata) == 0):
    print("There are no words in the dictionary")
for x in kata:
    print("{} was created by {}".format(x,kata[x]))