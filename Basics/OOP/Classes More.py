#               More on classes
"""
While Instance attributes are specific to each object,
class attributes are same for all objects.


It is better to use getters and setters to access data attributes

 - good style
 - easy to maintain code
 - prevents bug

"""

class Dog:                                  # same as Dog(object)
    # Class  Attributes                         Every Dog object created will be a mammal
    species = "mammal"

    # Initializer / Instance or data attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Dog object / create instances
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes / data attributes              using the dot operator
print(f"{philo.name} is {philo.age} and {mikey.name} is {mikey.age}")

# Is philo a mammal
if philo.species == "mammal":
    print("{} is a {}!".format(philo.name, philo.species))
print(mikey.species)



print("\n")

#           getters and setters


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    # getters - returns the values of any of the data attributes
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name

    # setters -
    def set_name(self, new_name= ""):           #
        self.name = new_name
    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return "Animal: " + str(self.name) + ": " + str(self.age)

"""
    NB: new_name= ""  is called a default argument. It is passed in automatically when the function is 
        called without an argument
"""


a = Animal(6)
print(a.age)                     # access data attributes - allowed but not recommended
print(a.get_age())               # access method - recommended

# default argument
a.set_name()                      # NB: No arguments passed - therefore the default arguments are passed in i.e""
print(a.get_name())

# Actual argument
c = Animal(2)
c.set_name("reiko")               # actual argument passed in.
print(c.get_name())







