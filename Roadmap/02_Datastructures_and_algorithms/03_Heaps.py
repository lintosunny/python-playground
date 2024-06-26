# A tree-based data structure in which the value of a parent node is ordered in a certain way with respect to the value of its child node(s). 
# A heap can be either a min heap (the value of a parent node is less than or equal to the value of its children) or 
# a max heap (the value of a parent node is greater than or equal to the value of its children).

# Python’s heap is a min-heap, its first element always has the lowest value.

# Priority Queue
# elements priority and insertion order that together determine the ultimate position within the queue
# first element of a heap always has the smallest (min-heap) or highest (max-heap)


from collections import deque
from heapq import heappop, heappush
from itertools import count


class IterableMixin:
    def __len__(self):
        return len(self._elements)
        
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()
            

class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()
        
    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)  # counter will rank according to insertion if all other same
        heappush(self._elements, element)
        
    def dequeue(self):
        return heappop(self._elements)[-1]
        
        
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")

messages.dequeue()
