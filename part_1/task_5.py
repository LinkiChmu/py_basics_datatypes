"""
There is a list with transport numbers.
The program will check each number for validity (1 letter, 3 numbers, 2 letters, 2-3 numbers).
Note that not all letters of the Cyrillic alphabet are used in transport numbers.

"""

import re

letters_valid = {'А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х'}
car_ids = ['А222ВС96', 'АБ22ВВ193']
pattern = r'([АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2})(\d{2,3})'

for id in car_ids:
    # checking the validity of letters and mask-checking
    result = re.match(pattern, id)
    if result:
        print(f'Номер {result.group(1)} валиден. Регион: {result.group(2)}')
    else:
        print(f'Номер {id} не валиден')
