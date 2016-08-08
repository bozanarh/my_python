#!/bin/python
"""
This is an example of iterator implementation
where we iterate in reverse order - zrange
or over every third element - drange
"""


"""Here in this example we create separate obj for
iterator and separate for iterable. If you use the same object
for both (see below, example of zranege), object
will be consumed only once.
What does it mean?
It means if you write:
y = trange(5)
list(y)
list(y)
you will get the same results, but if you write:
y = zrange(20)
list(y)
list(y)
in this case second call will print an empty list
"""
# iterating over every second elem
class trange(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return trange_iter(self.n)

class trange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            i = self.i
            self.i = i + 3
            return i
        else:
            raise StopIteration()
        

# iterating in reverse order
class zrange(object):
    def __init__(self, n):
        self.i = n
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i > 0:
            i = self.i
            self.i = self.i - 1
            return i
        else:
            raise StopIteration()

if __name__ == '__main__':
    print "Iterating in reverse order:"
    for i in zrange(5):
        print i        

    print "\nIterating over every scond elem:"
    for j in trange(20):
        print j

    print "getting list from my every 3rd iterator:"
    l = list(trange(30))
    print l
    l = trange(20)
    print list(l)
    print list(l)
    l = zrange(10)
    print list(l)
    print list(l)
    
