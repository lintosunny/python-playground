# Abstract data type
# Linear data structure that stores items in a FIFO manner.
# Front: position elements where removed
# Rear: position elements get added
# Enqueue: Adds an item to the queue. 
# Dequeue: Removes an item from the queue
# Overflow condition: if the queue is full
# Underflow condition: if the queue is empty



# Implement a Queue in Python
# 1. list
queue = []

queue.append('a')  # ['a']
queue.append('b')  # ['a', 'b']
queue.append('c')  # ['a', 'b', 'c']
queue.pop(0)  # ['b', 'c']
queue.pop(0)  # ['c']
queue.pop(0)  # []


# 2. collections.deque
from collections import 
q = deque()

queue.append('a')  # ['a']
queue.append('b')  # ['a', 'b']
queue.append('c')  # ['a', 'b', 'c']
queue.popleft()  # ['b', 'c']
queue.popleft()  # ['c']
queue.popleft()  # []


# 3. queue.Queue
from queue import Queue 
q = Queue(maxsize = 2)  # default, maxsize = 0 ie, infinite queue

q.put('a')
q.put('b')
q.full()  # False
q.get()
q.get()
q.empty()  # True
