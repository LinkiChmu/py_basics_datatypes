"""
The function counts how many words start with vowels and
how many start with consonants in a text.
The text can be written using both Cyrillic and Latin letters

"""
import re

some_text = '''
Эталонной реализацией Python является интерпретатор CPython, 
поддерживающий большинство активно используемых платформ. 
Он распространяется под свободной лицензией Python Software Foundation License, 
позволяющей использовать его без ограничений в любых приложениях, включая проприетарные.
'''


def vowel_cons(some_text: str) -> list:
    vowels = len(re.findall(r'\b[aeiouyУЕЫАОЭЁЯИЮ]', some_text, flags=re.IGNORECASE))
    cons = len(some_text.split()) - vowels
    return [vowels, cons]


print('Слов на гласные буквы:', vowel_cons(some_text)[0], '\nСлов на согласные буквы:', vowel_cons(some_text)[1])
