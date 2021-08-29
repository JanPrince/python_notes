class Queue(object):
    """
    Implementing Queue : (first in - first out)
    This queue takes in only one type of data (int)
    """
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.putloc = self.getloc = 0

    # method for putting in a value
    def put(self, value):
        """
        value to put in queue must be int
        """
        try:
            assert type(value) == int
        except AssertionError:
            print("Value is Invalid")
            return 1

        if self.putloc == self.size:
            print(" - Queue is full")
        else:
            self.queue.append(value)
            self.putloc += 1

    def get(self):
        if self.getloc == self.putloc:
            print(" - Queue is empty")
        else:
            get_value = self.queue[self.getloc]
            self.getloc +=  1
            return get_value


#                       Declaring an object of type Queue

my_que = Queue(4)
my_que.put(45)
my_que.put(3)
my_que.put(5)
my_que.put(-32)
my_que.put(12)      # queue is full
my_que.put(0)       # queue is full

for i in range(0, my_que.size):
    print(my_que.get())  # getting all the values (first-in, first-out)

print("-----------------------------\n")

que2 = Queue(3)

print("Putting in values")
que2.put(0.4)       # this is not kept in the queue
que2.put(56)
que2.put("hey")     # this is also not put in the queue
que2.put(-3)
que2.put(7)

print("\nGetting values")
print(que2.get())
print(que2.get())
print(que2.get())
print(que2.get())           # the queue is empty.
