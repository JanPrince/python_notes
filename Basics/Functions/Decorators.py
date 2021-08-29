"""
                            Decorators augment the behaviour of other functions or methods.
        Any function that takes a function as a parameter and returns an augmented function can be used as a decorator


                    A decorator must return a function. Therefore the decorator function would need a wrapper
"""


def decorator(c):
    def inner_fun(*args):
        print("Inside decorator")
        c(*args)
        print("Quiting decorator")
    return inner_fun

@decorator
def square(x):
    print(x*x)

square(7)


print("-----------------------------------------------------------------\n\n")


def announce(f):        # This is the decorator: it takes a function as parameter
    """
    f: a function
    """
    def wrapper():  # this is called a wrapper
        print("About to run function")
        f()
        print("Done running the function")
    return wrapper

# to use the decorator


@announce
def hello():
    print("Hello world")


hello()

