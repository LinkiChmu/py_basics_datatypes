"""
Given a list of some length.
The program creates a dictionary, based on the original list,
of such a nesting level as the length of the original list.

"""
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
new_list = list(my_list)
value = new_list.pop()
for i in range(len(new_list)):
    value = {new_list.pop(): value}

print(value)

