# BUILT IN FUNCTIONS
#
# map() is python's built in func
"""
For each elem of the list apply the function
Here is how to use it:
"""

def fahrenheit(t):
    return (9.0/5) *t +32

map(fahrenheit, [0, 10, 40])

"""
Better way to use it is with lambda expressions
"""

map(lambda t : (9.0/5) * t +32, [0, 10, 40])

"""
Next example, give me inverted number of this:
"""

a = [1,2,3]
map(lambda x : x * -1, a)

##############

# Reduce
"""
Takes first two elems and applys function on them
then appys func on the result and next first elem, etc
until there is only one elem
"""

max_find = lambda a,b : a if (a > b) else b
max_find(12, 45)

reduce(max_find, [34, 67, 23, 45, 67, 11])

##############

# Filter
"""
Applys filter function to each element on the list
and returnes only those results that were true
Here is example how to filter only even numbers:
"""
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

lst = range(10)
filter( is_even, lst)

# Better way is through lambda expressons:
filter(lambda num: num % 2 == 0, lst)

# Give me all numbers greater than 3:
filter(lambda num: num > 3, lst)


"""
zip - if you give him 2 lists, it will make new list of
tuples - pairs of each elem:
"""
>>> x = [1, 2, 3]
>>> y = [5, 6, 7]
>>> zip(x,y)
[(1, 5), (2, 6), (3, 7)]
>>> 


"""
Another example of zip():
"""
>>> a = [ 1, 2, 3, 4, 5]
>>> b = [ 2, 2, 10, 1, 1]
>>> map(lambda pair: max(pair), zip(a,b))
[2, 2, 10, 4, 5]
>>> 

"""
If you give dictionaries to the zip instead of lists,
then you will get back only keys
"""
>>> d1 = {'a':1, 'b':2}
>>> d2 = {'c':3, 'd':4}
>>> zip(d1, d2)
[('a', 'c'), ('b', 'd')]
>>> 

"""
To zip values instead of keys, do this:
"""
>>> zip(d2, d1.itervalues())
[('c', 1), ('d', 2)]
>>>



"""
enumerate - give you a tuple for each elem where 
first elem is postion and second is value
"""
>>> l = ['a', 'b', 'c','d']
>>> for (cnt, val) in enumerate(l):
...     print str(cnt) + ": " + val
... 
0: a
1: b
2: c
3: d


"""
all() - if all elements in the iterable are true, return true
any() - if at least one elem is the iterabel is true, return true

"""
l = [ True, False, True]
all(l) # will return False

any(l) # will retur True


