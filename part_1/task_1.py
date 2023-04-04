"""
Given a variable that stores a word from Latin letters.
The program displays:
- the middle letter if the number of letters in the word is odd;
- two middle letters if the number of letters is even.

"""
word = 'python'
print(word[(len(word)-1)//2:((len(word)+2)//2)])

