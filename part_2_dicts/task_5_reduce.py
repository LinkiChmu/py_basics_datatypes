"""
Given a list of some length.
The program creates a dictionary, based on the original list,
of such a nesting level as the length of the original list.

"""
from functools import reduce

my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(reduce(lambda val, key: {key: val}, reversed(my_list)))