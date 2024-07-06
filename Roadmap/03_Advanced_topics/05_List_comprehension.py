# Concise way to create a list using a single line of code

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  #-> ['apple', 'banana', 'mango']

newlist = [x for x in range(10) if x < 5]
print(newlist)  #-> [0, 1, 2, 3, 4]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)  #-> ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)  #-> ['hello', 'hello', 'hello', 'hello', 'hello']

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  #-> ['apple', 'orange', 'cherry', 'kiwi', 'mango']

newlist = [0 if i % 2 == 0 else i for i in range(10)]
print(newlist)  #-> [0, 1, 0, 3, 0, 5, 0, 7, 0, 9]

s = 'Bye'
newlist = [' ' + char.upper() + ' ' for char in s]
print(newlist)  #-> [' B ', ' Y ', ' E ']

cordinates = [(i, j) for i in range(3) for j in range(2)]
print(cordinates)  #-> [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
