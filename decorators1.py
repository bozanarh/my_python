# locals() - built in function; returns dict of all local vars
# globals() - built in function; returns dict of all gloabl vars

def test1():
    print locals()
    print globals()

def hello(name="Michael"):
    print "Hello " + name

greet = hello
print "greet="
print greet
print greet()
print hello()
del hello
print "greet after deleting hello: "
print greet()

# Functions within functions

