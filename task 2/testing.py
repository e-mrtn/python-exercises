words = open('words.txt','r').read().split('\n')

for word in words:
    if not word.isalpha():
        print(word,"alphabetical")
