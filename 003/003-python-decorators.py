#A decorator in Python is ied to add functionality to the existing pice of code
# A decorator uses the concept of passing a function as a parameter to another function

def hello(func):
    print("Hello", end=" ")
    return func

@hello
def greet(name):
    print(f"{name}")

greet("Python Programmer")
