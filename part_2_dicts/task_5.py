'''
Given a list of some length.
The program creates a dictionary, based on the original list,
of such a nesting level as the length of the original list.

'''
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
value = my_list.pop()
for i in range(len(my_list)):
    current_dict = {}
    key = my_list.pop()
    current_dict[key] = value
    value = current_dict
print(current_dict)

