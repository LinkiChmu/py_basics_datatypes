'''
Given variable contains list of users search queries.
The program displays distribution of the number of words in queries
in the form:
Search queries containing 2 word(s): 42.86%
Search queries containing 3 word(s): 57.14%

'''
import re

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
query_size = {}
for query in queries:
    size = len(re.split(r"\W+", query))
    query_size[size] = query_size.setdefault(size, 0) + 1
for size, count in sorted(query_size.items()):
    print(f'Поисковых запросов, содержащих {size} слов(а): {count / len(queries):.2%}')
