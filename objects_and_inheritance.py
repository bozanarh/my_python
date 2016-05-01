#!/bin/python

"""
"""
class MyBaseClass(object):
    classVar1 = 5

    @staticmethod
    def myClassStaticMethod():
        MyBaseClass.classVar1 +=2
        print MyBaseClass.classVar1

    def __init__(self):
        print "ctor"

    def myMethod(self):
        print "Hello"


class MyDerivedClass(MyBaseClass):

    def myMethod(self):
        print "Guten Tag"

    def myOtherMethod(self):
        print "Wie geht's?"

if __name__ == "__main__":
    MyBaseClass.myClassStaticMethod()
    c = MyBaseClass()
    c.myMethod()

    MyDerivedClass.myClassStaticMethod()
    d = MyDerivedClass()
    d.myMethod()
    d.myOtherMethod()


