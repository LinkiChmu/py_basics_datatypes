'''
The program asks the user for numbers in sequence (one at a time);
after the first zero displays the sum of all previously entered numbers.

'''

numbers_sum = 0
number = int(input('Введите число:\n'))
while number != 0:
    numbers_sum += number
    number = int(input('Введите число:\n'))
print(numbers_sum)
