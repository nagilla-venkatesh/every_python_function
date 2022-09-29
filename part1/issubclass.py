# Is Subclass
# issubclass is a function that checks if a class is a subclass of another class

class A:
    pass

class B:
    pass

class C(A):
    pass

class D(C):
    pass    

class E(A, B):
    pass

print(issubclass(A, A))
print(issubclass(A, B))
print(issubclass(B, A))
print(issubclass(C, A))
print(issubclass(C, B))
print(issubclass(D, A))
print(issubclass(D, B))
print(issubclass(E, A))
print(issubclass(E, B))
