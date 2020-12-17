# ! Used in browser for mainting history of website  < >
# ! ctrl+z  uses stack

# ~ LIFO


# ~ in python it can be implimented using
# ^-> list
# ^-> collections.deque
# ^-> queue.LifoQueue

'''
s = []
s.append('https://www.cnn.com/')
s.append('https://www.cnn.com/world')
s.append('https://www.cnn.com/india')
s.append('https://www.cnn.com/china')


# last link visited
print(s.pop())

'''

# ~ 0r

# ^  using dequeue  (doubley linked list implimemtation)

from collections import deque


class Stack:

    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self, val):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


s = Stack()
s.push(5)
print(s.peek())
