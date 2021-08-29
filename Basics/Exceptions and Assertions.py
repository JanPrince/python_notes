"""
Exceptions are used to handle errors in program
In python you can have handlers for exceptions

In a program you can put any lines of code that you think might be problematic/produce error
"""

#a = int(input("Tell me one number: "))
#b = int(input('Tell me another number: '))
#print('a/b = ', a/b)
#print('a+b = ', a+b)

"""
the above code can produce different errors based on users input
ValueError
ZeroDivisionError
TypeError
"""


# Examaples
#try:
#    a = int(input("Tell me one number: "))              # this block of code is problematic since it expects an integer
#    b = int(input('Tell me another number: '))          # from the user but; users are unpredictable and stubborn....
#    print(a/b)
#except:
#    print('there is a bug in this code')                # this line only runs when there is any error in the try block
#

# except caluses can be more specific
try:
    c = int(input("Tell me one number: "))
    d = int(input('Tell me another number: '))
    print(c/d)
except ZeroDivisionError:                           # only executes if this error comes up
    print('can\'t divide by 0')
except ValueError:                                  # same
    print("could not convert to a number")
except:                                              # for all other errors
    print("something went very wrong")


#   Raising exceptions
"""
we have been dealing with exceptions raised by python
but we can also raise own exceptions
"""
age = int(input("enter age: "))
if age == 34:
    print("heey you have the magic age.")
elif age < 1:
    raise ValueError                                        # can also raise with an info;   ValueError("something")
else:
    print('oh no you don\'t have the magic age')



print('\n')


#                                    Assertions
"""
A form of defensive programming
assert user_age != 0  reads;  make sure user_age is not 0 else produce an error and produce exit code 1 
"""
# eg: assert time = 3, means make sure time has a value of 3
try:
    user_age = int(input("enter your age: "))
    assert user_age != 0                              # produces an assertion error when user age is 0
except ValueError:
    print("invalid input")
except AssertionError:                                # An exception to handle Assertion error if produced
    print("Invalid Age")