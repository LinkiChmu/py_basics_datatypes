'''
There is a list with transport numbers.
The program will check each number for validity (1 letter, 3 numbers, 2 letters, 2-3 numbers).
Note that not all letters of the Cyrillic alphabet are used in transport numbers.

'''

import re

letters_valid = {'А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х'}
car_ids = ['А222ВС96', 'АБ22ВВ193']

for car_id in car_ids:
    # checking the validity of letters and mask-checking
    if len(set(re.findall(r'[а-яА-Я]', car_id)).difference(letters_valid)) == 0 \
            and len(re.findall(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}', car_id)[0]) == len(car_id):
        print(f'Номер {car_id[:6]} валиден. Регион: {car_id[6:]}')
    else:
        print(f'Номер {car_id} не валиден')
