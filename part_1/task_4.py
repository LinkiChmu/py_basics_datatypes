'''
There is an information about the average daily temperature (in Fahrenheit)
for some period by country.
The program calculates the average temperature for the period in Celsius for each country.

'''

countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
print('Средняя температура в странах:')
for country in countries_temperature:
    if len(country[1]) != 0:
        temp_avg_celsius = round(
            (sum(country[1]) - 32 * len(country[1])) * 5 / 9 / len(country[1]),
            1)
        print(f'{country[0]} - {temp_avg_celsius} C')
