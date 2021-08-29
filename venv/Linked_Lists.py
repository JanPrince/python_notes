"""
    A linked list is a collection of nodes, each made up of a reference and a value.
            Linked lists can be used to implement complex data structures like lists, stacks, queues, and
            associative arrays.
"""

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, val):
        self.data = val

    def setNext(self, valu):
        self.next = valu


class LinkedList:
    def __init__(self):
        self.head = None

    
