#      Casting is the changing of the type of an object
nUm = 56
nUm_decimal = float(nUm)     # conversion of integer to float
print(nUm_decimal)

Age = 17
# print("i am " + Age + " years old")     this gives an error cause you can't concatenate a string and an integer
print("i am " + str(Age) + " years old")   #  str() converts the number into a string for concatenation