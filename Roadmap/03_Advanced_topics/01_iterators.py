# Iterator is an object that contains a countable number of values.
# Iterator is an object which implements iterator protocol, consist of __iter__() and __next__()
# List, tuples, dictionary, and sets are iterable. They have built-in iter() object


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))  # apple
print(next(myit))  # banana
print(next(myit))  # cherry

mystr = "banana"
for x in mystr:
  print(x)  # b, a, n, a, n, a

# Create an iterator
class PowTwo:
    """class to implement an iterator
    of powers of two"""
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


numbers(PowTwo)
i = iter(numbers)
print(next(i))  # 1
print(next(i))  # 2
print(next(i))  # 4
print(next(i))  # 8
print(next(i))  # raises StopIteration exception


# Infinite iterators
from itertools import count 
infinite_iterator = count(1)  # starts at 1 and increment by 1
for i in range(5):
    print(next(infinite_iterator))
