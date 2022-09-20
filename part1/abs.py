# Absolute value
# abs() returns the absolute value of a number

class ImplementationAbs:
    def __init__(self, string):
        self.string = string

    def __abs__(self):
        return self.string.lower()

custom_obj = ImplementationAbs("Hello World")

x = abs(-7.25)
y = abs(-500.97)
z = abs(custom_obj)

print(x)
print(y)
print(z)
