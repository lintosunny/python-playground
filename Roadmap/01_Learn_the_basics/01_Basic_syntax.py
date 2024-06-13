# Python syntax defines a set of rules that are used to create a Python program.

# Python identifier is a name used to identify a variable, class, module, or other object.
# starts with a letter A-Z or a-z or (_) followed by zero or more letters, underscores and digits
# Manpower != manpower. ie, python is case sensitive
# class name starts with uppercase, all other with lowercase.
# private identifier: _example
# strongly private identifier: __example
# language defined special name: example__

# Reserved words: and, as, assert, break, class, continue, def, del, elif, ...

# Python lines and indendation
# In Python, all continous lines with same number of spaces would form a block.
if true:
    print("True")
else:
    print("False")

# Multi-line statements
total = item_one + \
        item_two + \
        item_three

days = ['M', 'T', 'W', 
        'T', 'F']

# comments
x = 50  # this is single line comment

'''
this  is a 
multi-line comment
'''

raw_input("\n\nPress the enter key to exit.")  # "\n\n" is used to create two new lines
