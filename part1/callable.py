# Callable 
# callable() is a built-in function that returns True if the object passed as an argument appears callable, and False if not.

class Class:
    pass

def func():
    print("I am a function")
    
def func2():
    def inner():
        pass
    return inner

func3 = lambda x: x + 1
not_func = "hello"

print(callable(Class))
print(callable(func))
print(callable(func2()))
print(callable(func3))
print(callable(not_func))