'''
A variable stores statistics of advertising channels by sales volume.
The program returns the name of channel with the highest sales volume.

'''
stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
max_volume = 0
max_channel = ''
for channel, volume in stats.items():
    if volume > max_volume:
        max_volume = volume 
        max_channel = channel
print(f'Максимальный объем продаж на рекламном канале: {max_channel}')
