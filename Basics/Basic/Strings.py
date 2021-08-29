#     Strings     ---  Python data type
#    Strings are immutable (cannot be modified)


Name = "Prince"      # Strings are written in " "  or ' '
Last_Name = "Jan"

# concatenation of strings
print("My name is " + Name + Last_Name)  # concatenation with ' + ' can only be used on strings
print("my name is", Name, Last_Name)     # when using ',' for conca... it automatically generates spaces
                                         # and can also be used to add strings and integers without casting
Age = 56
print("i am", Age, 'years old')

print('\n')
# \ - the escape and \n - new line
print("Albert Einstein said \"Imagination is more important than knowledge\" ")
print("Elon Musk says and i quote \n If something is important to you, you do it even if the odds are against You")


print('\n')

#                             String functions


#   .lower() and .upper()
School_name = "ADONTEN"
print(School_name.lower())    # vice versa with .upper

print('\n')

#   .isupper() and .islower()   this functions return a boolean depending on whether the string is entirely
#   uppercase or lowercase
friend = 'joshua'
print(friend.isupper())      # returns false
print(friend.islower())     # returns True

# finding the length of a string
print(len(friend))               # returns the number of characters found in the variable

# indexing
# starts from 0.   0 representing the first character

love = 'i love coding'
print(love[0])
print(love[6])    # NB: spaces are also indexed
print(love[-1])    # indexing a -ve number means beginning from the last character

#  Slicing
city = "Washington"
print(city[0:4])   # prints characters only from the ToDo[0] to ToDo[3]  (4 - 1)

new_city = 'Accra'
print(new_city.index('r'))    # .index() used to find the index(position) of a character in a string


print('\n')
#    .replace()
Home = "i live in Washington DC"
Home.replace('live', 'work')         # not gonna work because strings are immutable
print(Home)
print(Home.replace('live', 'work'))    # works this way
