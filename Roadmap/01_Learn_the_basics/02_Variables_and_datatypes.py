# variable name can contain a-z, A-z, 0-9, and an underscore. But can't start with 0-9
# Python is dynamically typed. No need to enter data type
#  1. Python implicit type conversion -> automatically converts one data type to other
x = 1 + 4.5  # -> output data type float
#  2. Explicit type conversion
x = int(9.6)  # -> output data type integer

# camel case: LintoSunny ->
# pascal case: lintoSunny -> class names
# snake case: linto_sunny -> functions, variable names

n = 300  # n is assigned the value of 300
x, y, z = "Red", "Orange", "Green"
a = b = c = 300  # a = 300, b = 300, and c = 300

print(x, y, z)  # output variables

type(n)  # <class 'int'>
m = n
print(m)  # output: 300, multiple references to a single object
id(m)  # memory location of value stored


# Global variables
# can be used inside and outside the function

x = "abc"
def myfunc():
    print(x)

def myfunc():
    global x
    x = "abc"
    print(x)


# Data types
# Text: str
# Numeric: int, float, complex
# Sequence: list, tuple, range
# Mapping: dict
# Set: set, frozenset
# Boolean: bool
# Binary: bytes, bytearray, memoryview
# None: NoneType
