#                                   Pass Statement
"""
The pass Statement is used to ignore an exception
"""

try:
    zerodiv = 4/0
except ZeroDivisionError:
    pass

print("I bypassed a zero-civision error. hurray!!")