#!/bin/python

#from abc import abstractmethod, ABCMeta
import abc

class Base(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def api1(self):
        pass

    @abc.abstractmethod
    def api2(self):
        pass

class Derived(Base):
    def api1(self):
        print "In Derived::api1"

    def api2(self):
        print "In Derived::api2"

class Derived2(Base):
    def api3(self):
        print "In Derived2:api3"

if __name__ == "__main__":
    d = Derived()
    d.api1()
    d.api2()
    try:
        d2 = Derived2()
        d2.api1()
    except Exception, e:
        print "got expected exception: " + str(e)

