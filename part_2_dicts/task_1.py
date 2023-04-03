'''
The variable contains a dictionary of geotags for each user.
The program displays a set of unique geotags for all users.

'''
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
unique_tags = set()
for user in ids.values():
    for tag in user:
        unique_tags.add(tag)
print(unique_tags)
