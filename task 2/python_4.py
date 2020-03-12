def reverse(string):
	rev = ""
	for c in reversed(string):
		rev+=c
	return rev

def palindrome(word):
	rev = reverse(word)
	if word == rev:
		return True
	return False
	
def vowel(word):
	vowels = ['a','e','i','o','u']
	vowels_ = []
	for letter in vowels:
		if letter in word:
			vowels_.append(letter)
	return vowels_

def consonant(word):
	consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
	consonants_ = []
	for letter in consonants:
		if letter in word:
			consonants_.append(letter)
	return consonants_ 


def alpha(word):
    if word.isalpha():
        print(word)
    else:
         print("Only input alphabetical characters please")

def run():
        words = open('words.txt','r').read().split('\n')
        lowercase = []
        for word in words:
                lowercase.append(word.lower())
        for word in words:
            if word.isalpha():
                print("---------------")
                print(word)
                is_pal = palindrome(word)

                if is_pal:
                        print("Palindrome: Yes")
                else:
                        print("Palindrome: No")
                        
                print("Letters: "+str(len(word)))
                vowels = vowel(word)
                print("Vowels: %s" % (', '.join(vowels)))
                consonants = consonant(word)
                print("Consonants: %s" % (', '.join(consonants)))
                rev = reverse(word)
                print(rev)
            else:
                print("Only input alphabetical characters please")

run()
# git status - view changed files
# git add python_4.py
# git commit -m "i added this function to"
# git push origin master
