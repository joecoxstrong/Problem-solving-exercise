# # Write a code that takes a string as input and returns the string reversed
word = input('Please enter a word to be reversed: ')
reversed_word = ''
for index in range(len(word)-1,-1,-1):
    reversed_word += word[index]
print(reversed_word)

# Capicalize a letter
word = input('Enter a word or phrase to be capitalized: ')
cap_word = word.title()
print(cap_word)


#compress a string of characters e.g. aaabbbbbccccaacccbbbaaabbbaaa => 3a5b4c2a3c3b3a3b3a

user_string=input('Enter a string to be compressed: ')
compressed_string = ''
count = 1
for i in range(len(user_string)-1):
    if user_string[i] == user_string[i+1]:
        count = count+1
    else:
        compressed_string = compressed_string + str(count) + user_string[i] 
        count = 1
compressed_string = compressed_string + str(count) + user_string[i+1] 
print(compressed_string)


# Palindrome test
word = input('Please enter a word to be reversed: ')
reversed_word = ''
for index in range(len(word)-1,-1,-1):
    reversed_word += word[index]
if reversed_word == word:
    print('Yes this is a Palindrome!')
else:
    print('Sorry, this is not a Palindrome.')    
    
