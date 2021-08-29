"""
Compound data type -  Tuple   - collection of data
   it is a compound data type because it made up of other data types

   Tuples are like list, but their elements are fixed that is, once a tuple is created,
   you cannot add new elements, delete elements, replace elements or reorder the elements
   in the tuple
   tuple - (immutable)   cannot be modified once created
    can mix elements types
"""
# a tuple
t = (1, 'mit', '3')
# t[2] = 7    gives an error, cannot modify

print(t[0])             # can access elements via indexing

print((2,3,5) + ("wow", "giraffe"))      # can add tuples

t_2 = (5, 6, "Yo")
t_add = t + t_2            # concatenation addition
print(t_add)
print(len(t_add))
print(t_add[1:4])        # can perform slicing


print('\n')
"""
tuples are useful in a couple of different scenarios

        Tuples are used to conveniently swap variable values 
        also used to create multiple variables at once
"""
#  multiple variable declaration
(Name, Age) = ("prince", 25)
print(Name)
print(Age)

# swapping of values
#
x = 23
y = 100

(x, y) = (y, x)
print("x = ", x)
print("y = ", y)


print('\n')

"""
Tuples are also used to return more than one value from a function
"""
def quotient_and_remainder(num1, num2):
    """

    :param num1: a positive integer
    :param num2: a positive integer
    :returns: a quotient and remainder of the two numbers
    """
    q = num1 // num2
    r = num1 % num2
    return (q, r)          # one object - Tuple, but two values retrieved - q, r
#   return q , r        can be written this way since the comma represents a tuple

(quo , rem) = quotient_and_remainder(4,5)
print(quo)
print(rem)


# can iterate over tuples

def get_data(aTuple):
    """
    :param aTuple: a tuple of the form ((int,str),(int,str),(int,str),(int,str),(int,str))
    :returns: min of all int , max of all int and num of all unique str
    """
    nums = ()
    words = ()
    for g in aTuple:
        nums = nums + (g[0],)
        if g[1] not in words:
            words = words + (g[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

# applying to any data you want!
tswift = ((2014,"Katy"),
          (2014, "Harry"),                    # a tuple
          (2012,"Jake"),
          (2010,"Taylor"),
          (2008,"Joe"),
          (2007, "Harry"))


(min_year, max_year, num_people) = get_data(tswift)

print("From", min_year, "to", max_year, \
        "Taylor swift wrote songs about", num_people, "people!")