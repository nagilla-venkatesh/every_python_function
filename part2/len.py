# Length
# len() returns the length of an object

class custom_list:
    def __init__(self, *args):
        self.list = list(args)
    def __len__(self):
        return 5
    
c = custom_list()
print(len(c))

x = [1, 2, 3, 4, 5]
print(len(x))

y = "Hello World"
print(len(y))

items = {"a": 1, "b": 2, "c": 3}
print(len(items))

s = set([1, 2, 3, 4, 5])
print(len(s))