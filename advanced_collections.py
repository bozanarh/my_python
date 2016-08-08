#!/bin/python

from collections import Counter

""" 
Counter is used to count elements in the collections
Result is a dictionary
"""

s = 'fdgdghjdfhjdhfjdhjhjfhdjh'
print Counter(s)
l = [1,1,1,2,2,2,1,1,3,4,4,5,7]
print Counter(l)

str = "How many times each word word word shows up in this sentence sentence"
words = str.split()
c = Counter(words)
print c

# show me 2 most common words
print c.most_common(2)

"""
other methods that are used:
clear()
list()
set() - convert it to set
c.items()...
you can also use string indexing
"""


"""
defaultdict
"""

"""
Dictionary comprehansion:
"""
{ x : x**2 for x in range(5)}

# if you do not want keys to be generated:
{ k: v**2 for k,v in zip(['a', 'b'], range(2))}

