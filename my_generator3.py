# What this code prints out?
def getVal2(max):
     print "getVal2 - point1"
     for i in range(max):
         print "getVal2() - point3: {}".format(i)
         yield i


def getVal1(n):
     print "getVal1() - point1"
     yield n
     print "getVal1() before ret"
     yield getVal2(n)
     print "getVal1() after ret"


if __name__ == "__main__":
     print "main - point1"
     o = getVal1(5)
     print "main - point2"
     print o.next()
     print "main - point3"
     for v in o:
         for q in v:
             print q
