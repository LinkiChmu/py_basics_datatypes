"""
Program accepts a list of email addresses and display their distribution by domain zones.
An example of the program's operation:
emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com' ]
Result:
gmail.com: 2
test.in: 1
ya.ru: 2
mail.ru: 1

"""
import re

emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']


def counting(emails: list) -> dict:
    dic = {}
    pattern = r'\w+@(\w+\.\w+)'
    for domain in re.findall(pattern, str(emails)):
        dic[domain] = dic.setdefault(domain, 0) + 1
    return dic


for k, v in counting(emails).items():
    print(k, v)
