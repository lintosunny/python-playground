# Write two functions, isOdd() and isEven(), with a single numeric parameter named number. 
# The isOdd() function returns True if number is odd and False if number is even. 
# The isEven() function returns the True if number is even and False if number is odd. 
# Both functions return False for numbers with fractional parts, such as 3.14 or -4.5. 
# Zero is considered an even number.

def isOdd(number):
    if number == 0:
        return False
    else:
        return number % 2 != 0

def isEven(number):
    if number == 0:
        return True
    else:
        return number % 2 == 0
