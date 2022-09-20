# Any 
# any() returns True if any element of the iterable is true. If the iterable is empty, it will return False.

a = [1, 0, 1, 2, 3]
print(any(a))

b = [True, True, 1, 2]
print(any(b))

c = ["", "a", "b"]
print(any(c))

d = [[0,0], [0,0], [0,0]]
print(any(d))

e = [[], [1], True]
print(any(e))
