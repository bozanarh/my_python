# What this code prints out?

def getVal2(max):
     print "getVal2 - point1"
     yield max
     print "getVal2 - point2"
     for i in range(max):
         print "getVal2() - point3: {}".format(i)
         yield i


def getVal1(n):
     print "getVal1() before ret"
     ret = getVal2(n)
     print "getVal1() after ret"
     return ret


if __name__ == "__main__":
     for v in getVal1(5):
         print v
