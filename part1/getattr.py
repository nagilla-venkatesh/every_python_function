# Get Attribute
# getattribute() is called every time an attribute is accessed

class MyClass:
    def __init__(self, value):
        self.value = value
        
c = MyClass(10)
print(getattr(c, 'value'))