#      Integers ---- Python Data types
#      Immutable too.
# Decimals in python are called floats
from math import*
# the math module provides us with more math functions.

Age = 34
print(Age)
print(type(Age))    # returns the type of the object
print(float(Age))   # returns decimal form of the integer (Casting)
my_number = -45
print(Age + my_number)

x = 4.08665
y = 5
print(x + y)
print(x * y)
print(x / y)
print(x ** y)


print('\n')
print(3 * 4 + 5)
print(3 * (4 + 5))


print('\n')

#    Modulus(%)
print(7 % 2)     # retuns the reminder when 7 is divided by 2


#              Functions on integers and floats (numbers)

#       abs(..) absolute
negative_num = -344
print(abs(negative_num))         # returns the positive of any number

#      pow(x , y)    - x to the power y
print(pow(4, 2))    # same as
print(4 ** 2)


#  max(..) and min(..)
print(max(4 , 56))
print(min(-2, -4))

# round(..) for rounding floats
print(round(3.4899737))  # rounds down to 3      ; you should know why....   :)
print(round(4.87))      # rounds up to 4

print('\n')

#     using functions from the math module

#       floor(..)
print(floor(3.7))   # always rounds it down i.e 3
print(floor(3.4))
#      ceil(..)
print(ceil(3.7))    # always rounds it up
print(ceil(3.4))


#     sqrt(..)    takes the square root
print(sqrt(49))       # NB: returns a float