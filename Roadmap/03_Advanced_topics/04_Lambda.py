# Lambda function is a small anonymous function, means function is without a name
# def keyword for the normal function and Lambda keyword for anonymous function
# Can take any number of arguments, but can have only one expression
# syntax -> lambda arguments : expression

x = lambda a : a + 10  # single argument, single expression
print(x(5))  #-> 15


x = lambda a, b : a * b  # multiple argument, single expression
print(x(5, 10))  #-> 50


def myfunc(n):
  return lambda a : a * n
  
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))  #-> 22
print(mytripler(11))  #-> 33


# How to use some example
list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))  #-> ['CAT', 'DOG', 'COW']
list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))  #-> ['dog', 'cow']
from functools import reduce
reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])  #-> 'cat | dog | cow'
