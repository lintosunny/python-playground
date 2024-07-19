# Python module is a python script file that can contain variables, functions, and classes.
# It is file name appended with .py
# Module refer to a file containing Python statements and definitions
# A file containing Python code, for ex: 'example.py', is a module
# Package is a collection of modules that are organized in a directory hierarchy

# OS module
#     mkdir(): create new directory
#     chdir(): change current directory
#     getcwd(): get current working directory
#     rmdir(): removes directory
#     listdir(): list of all files in a directory

# random module
#     random.random(): random float between 0.0 to 1.0
#     random.randint(): random integers between specified integers
#     random.randrange(): random element using start, step, and stop
#     random.choice(): random element from string, list, or tuple
#     random.shuffle(): randomly reorders elements in a list

# sys module
#     sys.argv(): return list of command line arguments passed to Python script
import sys
print ("My name is {}. I am {} years old".format(sys.argv[1], sys.argv[2]))
# -> C:\python37>python tmp.py Anil 23
# -> My name is Anil. I am 23 years old 
#     sys.exit: end program
#     sys.maxsize: returns largest int variable can take
#     sys.path: returns search path for all Python modules
#     sys.version: version of current python interpreter
#     sys.stdin: all interactive input
#     sys.stdout: output of print() and input()
#     sys.stderr: prompts and error msg goes to stderr

# collections module: provide alterantives to built-in data types

# time module
#     time.time(): returns current system time in ticks
#     time.localtime(): transalates time in ticks in time tuple notation
#     time.asctime(): returns readable format of local time
#     time.ctime(): returns string representation of system's current time
#     time.sleep():  halts current program execution for a specified duration in seconds



# Custom modules
# create __init__.py file in folder to consider a folder as package
# Crate a ex.py file with code, then if you want to use it 
import ex
