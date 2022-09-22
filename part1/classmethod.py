# Class method
# classmethod() is a built-in function that returns a class method for a given function.

class TestClass:
    def regular_method(self):
        print(self)
    
    @classmethod
    def class_method(cls):
        print(cls)
    
    def __str__(self) -> str:
        return "TestClass Instance"
    
t = TestClass()
t.regular_method()
t.class_method()
TestClass.class_method()
