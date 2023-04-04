'''
Given a stream of logs by the number of pages viewed for each user
in the format 'user,date;views'.
The program calculates the average value of views per user,
i.e. the ratio of the sum of all views to the number of unique users.

'''
import re

stream = [
    'user4,2021-01-01;3',
    'user3,2022-01-07;4',
    'user2,2022-03-29;1',
    'user1,2020-04-04;13',
    'user2,2022-01-05;7',
    'user1,2021-06-14;4',
    'user3,2022-07-02;10',
    'user4,2021-03-21;19',
    'user4,2022-03-22;4',
    'user4,2022-04-22;8',
    'user4,2021-05-03;9',
    'user4,2022-05-11;11'
]
total_views = sum([int(re.split(r'[,;]', log)[2]) for log in stream])
unique_users_count = len(set([re.split(r'[,;]', log)[0] for log in stream]))

print(f'Среднее количество просмотров на уникального пользователя: '
      f'{total_views / unique_users_count:.2f}')
