"""
    On of the best features in python
"""


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# the square of each num in nums is stored in another list
# results = []
# for x in nums:
#     results.append(x*x)
#
# print(results)


#                List comprehensions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = [x*x for x in nums]
print(results)

# Using a filter
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results1 =[x*x for x in nums1 if x % 2 == 0]        # squares only even numbers
print(results1)
