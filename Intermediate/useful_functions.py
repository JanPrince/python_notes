"""
 The dir() function returns all attributes and methods of an object
"""

name = "prince"     # string
age = 21            # int
isFair = False      # boolean
weight = 60.2       # float

friends = ['john', 'potter', 'ram']     # list
nums = set()        # Set
d = {'hi': 3, 'hello':4, 'wave':2}          # dictionary
t = tuple()


# prints all attributes and method of a string
print(dir(name))

print(dir(d))

"""
    The help() function returns the class implementation an object.
"""

v = {4, 5, 6, 't'}
print(type(v))      # set
print(help(v))      # prints the class implementation of a set in python
