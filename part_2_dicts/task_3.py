"""
A variable stores information about the costs and
income of advertising campaigns for various sources.
It is necessary to supplement the original structure with an ROI indicator,
which is calculated by the formula: (revenue / cost - 1) * 100.

"""
results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
for metrics in results.values():
    metrics['ROI'] = round((metrics.get('revenue') / metrics.get('cost') - 1) * 100, 2)

print(results)
