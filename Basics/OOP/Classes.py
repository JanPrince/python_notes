"""
                   Classes

  - Everything in python is an object (and has a type.)
  - an object is an instance of type
    example;  2 is an instance of a type (integer)  //  True is an instance of a type (boolean)

  Every object has:
   - a type                                                         [1,2,3,6] has type: list
   - an internal data representation
   - a set of procedures for interaction with the object            [4,6,7,3].append(8) - procedure for interaction

  with Classes, we:
   - can create new objects with some type
   - can manipulate objects
   - destroy objects

  Classes make it easier to reuse code :
  - each class has a separate environment (no collision on function names)

  creating a class involves:
  - defining a class name
  - defining class attributes
"""


"""
                            Attributes
what are attributes:
 - Data and procedures that belong to a class
 
 Data attributes: 
  - how you can represent your object with data..
  - think of data as other objects that makes up the class or 
   
    example: a coordinate class is made of two numbers(int)
 
 
 Methods(procedural attributes): 
   - think of methods as functions that work with only this class
   - how to interact with the object

 '.'operator is used to access any attributes
    - data attributes of an object
    - methods of an object 
    
  Special methods in classes:
   - __str__        when print is used on the object created
   - __add__        when two objects of the created class is being added using the '+' operator
   - __sub__
   - __len__(self)  

    NB: if you have not implemented a special method such as __str__ and you try to add 
        Coordinate objects with '+' , it will give an error
"""


#                       Implementing the Class

class Coordinate(object):
    # data attributes   (data representation) : what is the data that makes up the object
    # Initializer / Instance Attributes
    def __init__(self, x, y):                  # special method that describes how an instance is created
        self.x = x
        self.y = y

    # procedural attributes
    def distance(self, other):          # this method is used to interact with Coordinate objects created
        """
        input: takes in two Coordinate objects
        :returns the distance bet two Coordinate objects
        """
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5     # same as square root

    def __str__(self):                                 # python calls this method when you use print on your class
        """
        special method defined; that tells python what to do when you call print
        on an object of this type(Coordinate)
        """
        return "<" + str(self.x) + "," + str(self.y) + '>'


#                           Using the class

origin = Coordinate(2, 4)        # creates a new object of type, Coordinate.  (An instance of Coordinate)
zero = Coordinate(0, 0)

print(origin)                  # using print calls the __str__ method in the class

print(origin.x)                 # here, the "." operator is used to access data attribute
length = origin.distance(zero)   # here, method/procedural attribute is used via "." operator for manipulating
print(length)

c = Coordinate(3, 4)
print(c)
print(type(c))
print(type(Coordinate))              # returns <class 'type'> which means Coordinate is a type (data type) like str

# print(origin + zero)              # produces an error since __add__ has not been implemented in the class


"""
if you would like to figure if a particular object is an instance of a particular class,
use         isinstance(.. , ..)
"""
# example; to check if an object is a Coordinate
print(isinstance(c, Coordinate))                    # returns True if c is an instance of a Coordinate


print('\n')


"""
Create a new data type to represent a number as fraction

    Internal representation is two integers (data attributes):
        - numerator
        - denominator
    Methods / how to interact (Procedural attributes):
        - add, subtract 
        - print representation
        - invert the fraction
        - convert to float
"""


#                       Implementing
class Fraction(object):
    """
    A number represented as  a fraction
    """
    def __init__(self, num, denom):
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom

    # methods
    def __str__(self):
        """ returns a string representation of self"""
        return str(self.num) + "/" + str(self.denom)

    def __add__(self, other):
        """ :returns a new fraction representing the addition"""
        top = self.num*other.denom + other.num*self.denom
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __sub__(self, other):
        """ :returns a new fraction representing the subtraction"""
        top = self.num*other.denom + other.num*self.denom
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __mul__(self, other):
        """ :returns a new fraction representing the multiplication"""
        top = self.num * other.num
        bott = self.denom * other.denom
        return Fraction(top, bott)

    def __float__(self):
        """ returns a float value of the fraction"""
        return self.num / self.denom

    def inverse(self):                                 # my own method
        """ returns a new fraction representing the inverted fraction"""
        return Fraction(self.denom, self.num)


#               using class
a = Fraction(1, 4)
b = Fraction(3, 5)
c = Fraction(14, 3)
d = a + b               # d is a Fraction object            # calls __add__ method

print(d)                                                    # calls __str__ method
print("Decimal of a =", float(a))                           # calls __float__ method
print(Fraction.__float__(a))
print(c.inverse())                                          # calls inverse(self) method

diff = Fraction(8, 3) - Fraction(6, 23)                       # calls __sub__ method
print(diff)

print(a * b)                                                 # calls __mul__ method

try:
    z = Fraction(2.32, 4)                       # produces an AssertionError
except AssertionError:
    print('sorry your num or denom is a decimal')
