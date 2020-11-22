"""
[5] size: 1 top: 5
[8, 5] size: 2 top: 8
[5] size: 1 top: 5
[3, 5] size: 2 top: 3
[5] size: 1 top: 5
[1, 5] size: 2 top: 1
"""
from node import *


class Stack:
    __slots__ = ['__top', '__size']

    def __init__(self):
        self.__top = None
        self.__size = 0

    def __stringify__(self, node):
        if node is None:
            return ''
        else:
            rest = self.__stringify__(node.get_next())
            if rest == "":
                return str(node.get_value())
            else:
                return rest + ", " + str(node.get_value())

    def __repr__(self):
        return f'[{self.__stringify__(self.__top)}]'

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def push(self, value):
        node = Node(value, self.__top)
        self.__top = node
        self.__size += 1
    
    def peak(self):
        if self.is_empty():
            raise IndexError("Can't peak into an empty stack")
        return self.__top.get_value()

    def pop(self):
        if self.is_empty():
            raise IndexError("Can't pop an empty stack")
        current_value = self.__top.get_value()
        self.__top = self.__top.get_next()
        self.__size -= 1
        return current_value


