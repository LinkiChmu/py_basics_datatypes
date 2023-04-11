'''
Given variable contains list of users search queries.
The program displays distribution of the number of words in queries
in the form:
Search queries containing 2 word(s): 42.86%
Search queries containing 3 word(s): 57.14%

'''

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

for size in set([len(row.split()) for row in queries]):
    print(
        f'Поисковых запросов, содержащих {size} слов(а):'
        f' {len([row for row in queries if len(row.split()) == size]) / len(queries):.2%}')
