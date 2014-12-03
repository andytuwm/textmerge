__author__ = 'Andy'

FILE1 = "dict.txt"
FILE2 = "dict2.txt"
words = set()

with open(FILE1) as f:
    for line in f:
        if "'" not in line:
            words.add(line)

with open(FILE2) as f:
    for line in f:
        if "'" not in line:
            words.add(line)

with open('newdict.txt', 'a') as file:
    for word in sorted(words):
        file.write(word)