# Count Vowels
# Ask the user for a sentence and count:
# a, e, i, o, u
line=input("Enter the setence:")
vowel="aeiou"
count=0
for i in line.lower():
    if i in vowel:
        count=count+1
print("Number of vowels are=",count)