# Write a function that takes a string and returns the count of vowels and consonants separately.
def count(text):
    vowel="aeiou"
    countvowel=0
    countconsonants=0
    for char in text.lower():
        if char in vowel:
            countvowel += 1
        elif char.isalpha():
            countconsonants +=1
    return countvowel,countconsonants            
countvowel,countconsonants=count("Saumya Singh")
print(f"Vowels are {countvowel} and consonants are {countconsonants}")
