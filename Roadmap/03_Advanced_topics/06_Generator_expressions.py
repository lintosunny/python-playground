# Concise way to create a generator using a single line of code
# Geneator function is a function that contains 'yield' statement and retuns a generator object
# syntax like list comprehension but use parentheses () instead of square brackets []
# generator provides a convinient way to implement the iterator protocol

gen_exp = (x ** 2 for x in range(10) if x % 2 == 0)  # can create without yield
for x in gen_exp:  # but not share the whole power of yield
    print(x)  #-> 0 4 16 36 64

# return can output a value and yield can output a list of values
def my_gen():
    for x in range(5):
        yield x
        
for i in my_gen():
    print(i)  #-> 0 1 2 3 4

# use less memory, especially for large sequences
# create the generator without creating the entire sequence in memory at once
