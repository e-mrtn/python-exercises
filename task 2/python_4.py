words = open('words.txt','r').read().split('\n')

lowercase = []
for word in words:
    lowercase.append(word.lower())

def reverse():
    reverse = word[::-1]
    return reverse

def palindrome():
    reverse = word[::-1]
    if word == reverse:
        print("Palindrome? Yes")
    else:
        print("Palindrome? No")
        
    return palindrome

def length():
    l = len(word)
    print("Letters:",l)
    return l

def vowel():
    vowels = ["a","e","i","o","u"]
    check = []
    for letter in word:
            for vowel in vowels:
                if letter == vowel:
                    if vowel not in check:
                            check.append(vowel)

    print("Vowels: %s" % (', '.join(check)))
    return check

def consonant():
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    check = []
    for letter in word:
            for consonant in consonants:
                if letter == consonant:
                    if consonant not in check:
                        check.append(consonant)
    print("Consonants: %s" % (', '.join(check)))
    return check
        
def run():
    for word in words:
        print("---------------")
        print("Word:",word)
        palindrome()
        length()
        vowel()
        consonant()
        print(word[::-1])

counter = 0
for word in words:
    if word.isalpha():
        counter = counter + 1
        continue
    else:
        print(word, "is non alphabetical")

count = len(words)
if counter == count:
    run()
        
