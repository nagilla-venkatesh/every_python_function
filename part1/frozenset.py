# Frozen set
# frozen set is immutable set

# can be used as keys in dictionary

lst = [1, 2, 3]
s = set(lst)

s.add(4)

print(s)

fs = frozenset(lst)
print(fs)

