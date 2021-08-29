"""
Recursion
 - reducing a problem to simpler versions of the same program
 - Semantically: programming technique where a function calls itself
      must have one or more base cases that are easy to solve

      Recursion - a friend of iterations
"""

#                               Multiplication

#   Iteration
"""
multiplying a*b is same as adding a to itself b times
"""

def mult_iter(a,b):
    result = 0
    while b > 0:                                  # iteration
        result = result + a
        b -= 1
    return result

print(mult_iter(3, 5))

#    Recursive solution
"""
recursive step: think of how to reduce the problem to the simpler version of the same problem - multiplication
a * b = a +  a*(b-1)

base case: keep reducing problem until you reach a simple case that can be solved directly
i.e    when b = 1,     a * b = a 

"""

def mult(x,y):
    if y == 1:                                  # base case
        return x
    else:
        return x + mult(x, y-1)                 # recursive step

print(mult(4,3))

print('\n')


#                           Factorial

#      Recursive solution
"""
 n! = n * n-1 * n-2 * n-3 * ... * 1
 for what n do we know the factorial,  n = 1.   
 therefore  base case is   if n == 1:
                              return 1
                              
Rewrite problem in terms of something simpler to reach base case
n! is same as          n! = n + (n-1)!
"""

def fact(n):
    if n == 1:                  # base case
        return 1
    else:
        return n + fact(n-1)    # recursive step

print(fact(4))


#                       Iterative solution

def fact_iter(n):
    prod = 0
    for i in range(1, n+1):
        prod = prod * i                     # fact_iter(3) = 0 + 1 + 2 + 3
        return prod

print(fact(4))

"""
                                Notes
- recursion may be simpler, more intuitive.
- recursion may be efficient from programmer POV
- recursion may not be efficient from computer POV
"""

print('\n')
#           Recursion with multiple base case  (fibonacci numbers)
"""
 A series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
 The simplest is the series 1, 1, 2, 3, 5, 8, etc
"""

def Fib(x):
    """
    assumes x an  integer >= 0
    returns Fibonacci of x
    """
    if x == 0 or x == 1:                        # base cases
        return 1
    else:
        return Fib(x - 1) + Fib(x - 2)

print(Fib(1))
print(Fib(2))
print(Fib(3))
print(Fib(4))                                # results produce are sum of two of its preceding numbers
print(Fib(5))
print(Fib(6))


#             Recursion on non-numerics  (how to check if a string is a palindrome)

def Ispalin(s):

    def Tochars(s):
        """
        s : assume to  be a string
        spaces are ignored
        returns a string with only characters/alphabets
        """
        s = s.lower()
        ans = ''
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:                         # base case - it is a palindrome if it is one letter
            return True
        else:
            return s[0] == s[-1]  and isPal(s[1:-1])        # recursive case
    return isPal(Tochars(s))

word = "aba"
print(Ispalin(word))
print(Ispalin("hello"))