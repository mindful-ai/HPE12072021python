# Find and list vowels in a given text

# input

text = input("Enter some text: ")

# process
# output

vowels = 'aeiou'
for vowel in vowels:
    print(vowel, ' ---> ', text.lower().count(vowel))

