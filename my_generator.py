#!/bin/python


def filterLines( fName ):
    with open( fName, "r" ) as f:
        for l in f:
            if not l.startswith("#"):
                yield l

if __name__ == "__main__":
    for l in filterLines("hello.txt"):
        print l,

