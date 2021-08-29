"""
                                                Control flow  -  Branching
Conditionals
                                            control flow is kinda like decisions in python
if <condition>:
   <expression>
   <expression>
elif <condition>:
     <expression>
else:
   <expression>

   <condition> has a value True or False
   evaluates expressions in that block if <condition> is True

   Indentation is very important
"""
x = input("input a number for x: ")
y = input("input a number for y: ")
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore x/y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print('y is smaller')
