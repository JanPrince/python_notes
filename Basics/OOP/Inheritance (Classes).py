import random         # note: this is a class someone has written therefore, it has methods.
import string

"""
Hello there!
today is a happy day

    Inheritance is all about a new class being derived another class

The base class is the already existing class(parent), and the DerivedClass is the new class(child)
that inherits attributes from the BaseClass.

        Hierarchies
            - Parent / base / super class
            - Child / derived / sub class
                .inherits all data and behaviours from the parent class
                .adds more info
                .adds more behaviour
                .overides behaviour

Case Study:  super class - Animal
             subclasses  - 1. Person:
                                    subclass of Person - 1. Student
                           2. Cat
                           3. Rabbit


        example:
            class Fraction(object):
        We define a parent Fraction class in the example above,
        which implicitly inherits from " object "
            Inheriting from 'object' means being able to access the basic python
            data types in our class. Eg - strings, integers, lists, etc.
            and also inheriting bbasic operations like
            binding variables, etc
"""


# Case study 1

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    # getters - returns the values of any of the data attributes
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    # setters - Modifies data attributes
    def set_name(self, new_name=""):
        self.name = new_name

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return "Animal: " + str(self.name) + ": " + str(self.age)


# Subclass 1
class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat: " + str(self.name) + ": " + str(self.age)



"""
The Cat class inherits all data attributes form the Animal class including:
            - __init__()
            - and all methods including __str__()
            
    In the Cat class we add two mor methods
    
    Creating a new __str__() method in the Cat class overrides the Animal class __str__().
    
    NB: you can't use the Cat class methods on an instance of the Animal class  
"""


# subclass 2
class Person(Animal):
    """
    This class specifies attribute and behaviours of a person
    from the Animal class
    """
    def __init__(self, name, age):          # overrides Animal __init__ method
        Animal.__init__(self, age)       # calls the animal's __init_ method
        self.set_name(name)                 # calls the Animal's method
        self.friends = []                   # a new data attribute

    # adds new methods / info
    def get_friends(self):
        return self.friends

    def add_friend(self, friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.age - other.age
        print("year difference = " + str(abs(diff)))

    def __str__(self):                                  # overrides Animal's __str__ method
        return "person: " + str(self.name) + ": " + str(self.age)


print("\n -----person tests-----")
p1 = Person("jack", 23)
p2 = Person('jill', 30)

print(p1.get_name())
print(p1.get_age())                     # this methods are inherited from the Animal class
print(p2.get_name())
print(p2.get_age())

print(p1)
p1.speak()
p1.age_diff(p2)


"""
HELLO THERE
NB:             subclasses can have methods with the same name as superclass.
                but for an instance of a class, python looks up for the method in the current class definition,
                if not found, looks for method name up the hierarchy (parents, grandparents and so on)  
"""


# Sub subclass
class Student(Person):
    """
    inherits attributes from the Person class which is a child class of the Animal class
    therefore: the Animal class is a grandparent to the Student class

    NB: Student class inherits from both Person and Animal class.
    """
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)     # this tells python to initialize name and age as done in Person class
        self.major = major

    def change_major(self, new_major):
        self.major = new_major

    def get_major(self):
        return self.major

    def speak(self):
        r = random.random()         # random() is a method in the random class and it returns a float bet (0 and 1)
        if r < 0.25:                               #      0 inclusive
            print("i have homework")
        elif 0.25 <= r < 0.5:
            print("i need sleep")
        elif 0.5 <= r < 0.7:
            print("i should eat")
        else:
            print("i am watching tv")

    def __str__(self):
        return "student: " + str(self.name) + ": " + str(self.age) + ": " + str(self.major)


print("\n---------Student test---------")
s1 = Student('Alice', 24, 'CS')
s2 = Student("beth", 19)
print(s1)
print(s2)
s2.set_name("Bethy")

print(s1.get_name(), 'says ', end=" ")
s1.speak()
print(s2.get_name(), 'says', end=' ')
s2.speak()


# Class variables  -  class variables and their values are shared between all instances of a class
class Rabbit(Animal):
    tag = 1         # tag variable is used to give unique id to each new rabbit instance.
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.id = Rabbit.tag         # accessing class variable. NB: not using self but the class name
        Rabbit.tag += 1

    def get_id(self):
        return str(self.id).zfill(3)


print('\n -------Rabbit test-------')
r1 = Rabbit(2)
r2 = Rabbit(3)
rab = Rabbit(5)


print(r2)       # uses __str__ from Animal class
print(r1.get_id())
print(r2.get_id())
print(rab.get_id())