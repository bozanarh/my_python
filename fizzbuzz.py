#!/bin/python

w = ""
for x in range(1,100):
    if x % 3 == 0:
        w = "Fizz"
    elif x % 5 == 0:
        w = "Buzz"
    if x % 3 == 0 and x % 5 == 0:
        w = "FizzBuzz"
    if w != "":
        print str(x) + " " +  w
    w = ""
