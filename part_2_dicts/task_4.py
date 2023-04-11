'''
A variable stores statistics of advertising channels by sales volume.
The program returns the name of channel with the highest sales volume.

'''
stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

print(max(stats, key=stats.get))
