#LEGB scope resolution rule in Python:-
#LEGB stands for Local, Enclosed, Global and Built-in scopes
# This plays an important role in Python coding


#Built in scope
from math import pi

#Global variable
pi="Global"

def foo():
    #local
    pi = "Local"
    def foobar():
        #enclosed
        pi="Local - 2"
        print(pi)
    foobar()

foo()
print(pi)

#Built in scope is given the last priority, followed by global, enclosed and local variables in a block of code
