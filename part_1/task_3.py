'''
We are making MVP of dating service and we have a list of guys and girls.
We put forward a hypothesis: we will get the best recommendations,
if we just sort the names alphabetically and introduce people
with the same indices after sorting!
But we will not introduce anyone if someone can be left without a partner.

'''

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    print('Идеальные пары:')
    pairs = list(zip(sorted(boys), sorted(girls)))
    for pair in pairs:
        print(f'{pair[0]} и {pair[1]}')
else:
    print('Внимание, кто-то может остаться без пары!')
