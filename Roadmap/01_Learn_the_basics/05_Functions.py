# Function is a reusable block of code that executes a certain functionality when it is called.

# creating a function
def my_function():
    pass  # if function is empty, it returns error. pass is a placeholder to avoid error

my_function()  # calling function

# Arbitary arguments, *args
def youngest_kid(*kids):  # if no. of arguments unknown, add * before parameter
    print("Youngest child is " + kids[2])

yougest_kid("A", "B", "C")  # -> returns C

# Arbitary arguments, **kwargs
def last_name(**kids):  # if no. of keyword arguments unknown, add ** before parameter
    print("last name is " + kid["lname"])

last_name(fname = "Linto", lname = "Sunny")  # -> last name is sunny



# buit-in functions
# zip() -> iterate over several iterables in parallel, producing tuples with an item from each one
for item in zip([1, 2], ["A", "B"]):
    print item

'''output
(1, 'A')
(2, 'B')
'''

# enumerate() -> returns an enumarated object
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))  # -> [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))  # -> [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# enumerate equivalent to
def enumerate (iterable, start=0):
    n = start
    for element in iterable:
        yield n, element  # using yield to return a list of values from function
        n += 1
