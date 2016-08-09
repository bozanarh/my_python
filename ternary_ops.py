## Conditional expressions
#
# Long form:
# if x > 0:
#    ret = x
# else:
#    ret = -1
# return ret
#
# This is similar to C++ condition:
# return x > 0 ? x : -1
#
# Here is short form: 
return x if x > 0 else -1


## Here is another one:
# Not widely used:
#
# long form:
# x = "Cao"
# y = "Bozana"
# if x.startswith("Ca"):
#    ret = x
# else:
#    ret = y
# return ret
#
# Here is short form:
x= "Cao"
y = "Bozana"
return (x, y)[x.startswith("Ca")]



