# Regular expression is powerful language for matching text patterns.
# Python "re" module gives RegEx support.
# match = re.search(pat, str)
# used by string searching algorithm for "find" or "find all", or for input validation

import re
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)  # 'r' designated raw string
if match:
    print('found', match.group())  # found word:cat
else:
    print('did not found')

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)  # [('alice', 'google.com'), ('bob', 'abc.com')]
