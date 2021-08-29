"""
Functions  -
functions are mechanisms used to achieve abstraction and decomposition

Abstraction
idea : knowing how to use something but not knowing how it works.
Abstraction is achieved with function specifications or docstrings (a type of comment)
suppress details with abstraction

Decomposition
Idea : different things working to produce an end goal (case study: small projectors working to produce one large image)
In programming - dividing codes into modules (i.e use of functions)
Decomposition is achieved with functions

dividing code into modules:
 - keeps code organized
 - intended to be reusable
 - used to break up code

functions are not run in a program until they are called or invoked

function characteristics. has:
 1. name
 2. parameter (0 or more)
 3. docstrings (optional but recommended
 4. a body
 5. returns something - you are allowed to return only one object
"""


def iseven(i):
    """
    :input i: i, a positive integer
    :returns: True if i is even and False if otherwise
    """
    print("hey i am inside isEven function")
    return i % 2 == 0


user = 5

iseven(user)
"""above, the function is invoked using its name and arguments;
it is invoked as a statement therefore it's return value is ignored"""
print(iseven(user))          # here the return value of the function is printed

print('\n')

user_results = iseven(user)     # return value of the function is stored in a variable
print(user_results)

print('\n')





"""
functions return values
functions that do not have a return value automatically returns  None; such a function is called a None function / void

None is a data type
"""


def Iseven(num):
    """
    :param num: a positive integer
    :return: True if num is even and false  if otherwise
    """
    print(num % 2 == 0)


user_num = 8
Iseven(user_num)
print(Iseven(user_num))          # prints None because function has no return value
# or
answer = Iseven(user_num)
print(type(answer))               # None type

print('\n')

"""
Arguments 
a function's argument can be passed in as positional or keyword
"""


def max(a,b,text):
    """
    :param a: integer
    :param b: integer
    :param text: a word
    :return: the max integer and the word
    """
    if a > b:
        return str(a) + text
    elif b > a:
        return str(b) + text


user_1 = 34
user_2 = 23
word = 'hurray'

'''
# for positional arguments,
max_num = max(user_1, user_2, word)
print(max_num)   '''

# for keyword arguments
max_num = max(text=word, a= user_1, b= user_2)
print(max_num)


"""
functions can be nested

every time a function is invoked, a new scope/environment is created.
"""
print('\n')


#                   Default functions
"""
    Default arguments are set when implementing a function
    They are only used when the function is called without 
    an actual argument for that parameter
"""

def Greet(name, greetings="Hello"):     # here the parameter 'greetings' has a default argument - "Hello"
    return greetings +" "+ name + "!"


print(Greet("John", "HI"))    # NB: here, an actual argument is passed for both parameters

print(Greet("prince"))         """ NB: here, no argument passed for the 'greetings' parameter therefore,
                                        the default argument is passed automatically (returns Hello prince!) """
