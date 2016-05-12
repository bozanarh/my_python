#!/bin/python

def my_decorator1(func):
    def decorator_wrapper():
        print "Do somethign before"
        func()
        print "Do something after"
    return decorator_wrapper

"""
Note here that we annotate function that needs decorator

Note that this annotation is equivalent to writing this code:
    f = func_needs_decorator
    d = my_decorator1(f)
    d()

so you can use either annotation or write it manually
"""
@my_decorator1
def func_needs_decorator():
    print "Hello world"

def main():
    func_needs_decorator();
    ""'
    f = func_needs_decorator
    d = my_decorator1(f)
    d()
    """

main()

