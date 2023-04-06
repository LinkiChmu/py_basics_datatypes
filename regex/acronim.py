"""
Program returns an acronym for the string passed to it with words.
Examples of how the program works:
some_words = 'Information Technology’
Result: IT
some_words = 'Near Field Communication'
Result: NFC

"""
import re


def acronym(some_words):
    return re.sub(r'(\w)\w+\s?', r'\1', some_words).upper()


print(acronym('Информационные технологии'))
print(acronym('Near Field Communication'))
