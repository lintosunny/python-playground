# Data structure that stores items in a LIFO manner.
# push: adding an object to the top of the stack
# pop: removing the object from the top 
# if stack runs out of memmory, it's called stack overflow



# Implementing stacks
# Avoid list because it can potentially have memory relocation issues
# Use deque if not using threading
# Use LifoQueue if using thrading

# 1. list
myStack = []

myStack.append('a')  # ['a']
myStack.append('b')  # ['a', 'b']
myStack.append('c')  # ['a', 'b', 'c']
myStack.pop()  # ['a', 'b']
myStack.pop()  # ['a']
myStack.pop()  # []
myStack.pop()  # IndexError


# 2. collections.deque
from collections import deque
myStack = deque()

myStack.append('a')  # ['a']
myStack.append('b')  # ['a', 'b']
myStack.append('c')  # ['a', 'b', 'c']
myStack.pop()  # ['a', 'b']
myStack.pop()  # ['a']
myStack.pop()  # []
myStack.pop()  # IndexError

# list vs deque
# The contiguous memory layout is the reason that list might need to take more time to .append() some objects than others.
# deque built upon a doubly linked list. each entry is stored in its own memory block and has a reference to the next.


# 3. queue.LifoQueue
from queue import LifoQueue
myStack = LifoQueue()

myStack.put('a')  # ['a']
myStack.put('b')  # ['a', 'b']
myStack.put('c')  # ['a', 'b', 'c']
myStack  # <queue.LifoQueue object at 0x7f408885e2b0>
myStack.get()  # ['a', 'b']
myStack.get()  # ['a']
myStack.get()  # []
