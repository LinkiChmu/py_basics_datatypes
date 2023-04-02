'''
Given a variable that stores a word from Latin letters.
The program displays:
- the middle letter if the number of letters in the word is odd;
- two middle letters if the number of letters is even.

'''
word = 'python'
size = len(word)
print(word[size//2] if size % 2 == 1 else word[(size//2 - 1):(size//2 + 1)])
