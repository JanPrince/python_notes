import time
"""
hello there!

-----------------------Program Efficiency 1 ----------------
How to know the efficiency of programs
    - Two things are taken into consideration :
                                                1. Time  --- (Primary) the runtime of algorithms
                                                2. Space --- size of storage the program occupies or uses

    NB: we will focus on time efficiency

    How to evaluate the efficiency of programs;
        1. measure with a timer
        2. count the operations
        3. abstract notation of ORDER OF GROWTH  -- most appropriate way of accessing the impact of choices of
                                                algorithm in solving a computational problem. 
                                                    Used by computer scientists
"""


# 1. Measuring with timer

def c_to_f(celsius):
    """

    :param celsius: input in celsius
    :return: an int in f
    """
    con = celsius * (9/5) + 32
    return con


t0 = time.clock()
c_to_f(10000000)
t1 = time.clock() - t0

print(t1)