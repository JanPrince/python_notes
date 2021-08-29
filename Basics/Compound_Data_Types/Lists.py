"""
List is a general data structure that is widely used in python programs. They are found in other languages often
referred to as dynamic arrays.

Lists are mutable and a sequence data type that allows them to be indexed and sliced
They can contain different types of objects, including other lists.
"""

a_list = []         # empty list


#      Indexing and slicing
Lst = [3, 4, 2, 34, 22, 9, 44]
print(Lst[-2])          # indexing
print(len(Lst))
print(Lst[1:5])        # slicing

print('\n')


#       Mutability
L = [2, 'a', 34, 3, 4, 18, "noo"]
i = 6
L[i - 3] = "mit"            # since lists are mutable, L is modified
print(L)

print('\n')


"""
Lists functions or operators
"""
#                   Add
# lists can also be concantenated using the '+' operator

b = [8, 9, 10]
a = [1, 2, 3, 4, 5]
all = a + [6, 7] + b
print(all)                 # NB: a and b are not changed


#   .append(..) - appends a new element to the end of the list.
users = ["john", "kate", "harry", 'joe']
users.append("Kaifu Lee")                               # mutates users
print(users)
users.append([2, 3])             # appending a list
print(users)

#  .extend(a list) -  adds the elements of one list to the other
jobs = ["doctor", "secretary", "plumber"]
new_jobs = ["engineer", "physicist", "developer"]
jobs.extend(new_jobs)   # mutates jobs,
print(jobs)
print(new_jobs)

# .insert(.. , ..)
prime = [1,3,7,11,13,17,19]
prime.insert(2, 5)              # insert 5 at position 2
print(prime)

print('\n')

#               Remove    - -   all functions mutate
Lssst = [2,1,3,"halo",6,1,3,"yeah",9]

# del(list[])  -- delete element at a specific index
del(Lssst[3])
print(Lssst)

# .pop() -  removes an element at the end of the list and returns the removed element
# .pop(index) - removes an element at the specified index and returns the removed element
Lssst.pop()            # removes the last element
print(Lssst)
Lssst.pop(1)          # removes the element at index 1
print(Lssst)
print('\n')
"""
NB: since .pop() returns the removed element, it is useful when removing an 
element from a list and storing it in a variable
"""
Yeah = Lssst.pop()
print(Yeah)


# .remove(element) -- removes specific element
numbers = [2,3,5,6,8,'guo',3,7,7,3,4]
numbers.remove("guo")
print(numbers)


print('\n')


#               Other list operators
# sorted(list) returns a sorted list but does not mutate list
# .sort(list)  sorts and mutates list
# .reverse(list)   mutates list

odd = [9, 7,0, 13,3]
print(sorted(odd))        # no mutation
print(odd)

odd.sort()               # mutates
print(odd)

odd.reverse()
print(odd)

print('\n')

#    conversion of lists and strings
# from strings to list - list(str)
name = "prince"
name_list = list(name)
print(name_list)

# List to String    --  " ".join(..)
my_name = ['j','a','n']
my_name_str = "".join(my_name)
print(my_name_str)


# .split()  -


#                       iterating over list
#  iterating using indexes
even = [2,4,6,8,10]
total = 0
for i in range(len(even)):
    total += even[i]
print(total)

# iterating over elements directly
natural = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for q in natural:
    sum = sum + q
print(sum)


print('\n')


#                       Aliasing -  changing one changes the other
#   .append() has a side effect

warm = ['red', 'yellow', 'orange']
hot  = warm                                 # this become alias
hot.append('pink')                          # appending pink to hot also affects warm
print(hot)
print(warm)

print('\n')

#                   Cloning list
cool = ['blue', 'green', 'grey']
chill = cool[:]                            # [:] for cloning
chill.append("black")
print(chill)
print(cool)

"""
NB: avoid mutating a list while iterating over it.
 instead, make a clone of the list, iterate over the clone while mutating the original list
"""
def remove_duplicates(L1,L2):
    L1_copy = L1[:]
    for e in L1_copy:               # iterating clone of L1
        if e in L2:
            L1.remove(e)            # mutating L1
    return  L1
L1 = [2,4,5,7,1,4,6]
L2 = [8,9,3,4,5,1,4]
print(remove_duplicates(L1,L2))





#    Multidimensional lists