# A Python program terminates as soon as it encounters an error. 
# In Python, an error can be a syntax error or an exception.
# By using an exception program don't crash and we know what happened
# raise -> to stop your program by raising an exception if a condition occurs.
# assert -> debugging during development


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)  # excecute if no errors raised
    finally:
        print("executing finally clause")  # exceuted regardless there is error or not

# divide(2, 1) -> result is 2.0
#                 executing finally clause
#divide(2, 0) -> division by zero!
#                executing finally clause
#divide("2", "1") -> executing finally clause

      
# Some common errors are:
# 1.Syntax error
# 2.ZeroDivisionError
# 3.IndexError
# ...
