# containers which are able to store more than one item at the same time
# ordered collection of elements with same datatype
# list and array are same but array can only store one data type unlike list
# eg. NumPy arrays for mathematical calculations

import array as arr
num = arr.array('i', [10,20,30])
print(num)  #-> array('i', [10, 20, 30])

# Basic array operations
# Adding/ changing -> num.append(10), num.extend(10)
# Concatenating -> nums = num + num
# Removing/ deleting -> num.pop(), num.remove()
# Slicing -> num[1:3]
# Looping -> for i in num
