'''
The program asks the user for numbers in sequence (one at a time);
after the first zero displays the sum of all previously entered numbers.

'''
print("Вводите числа по одному:")
print(sum([int(i) for i in iter(input, '0')]))
