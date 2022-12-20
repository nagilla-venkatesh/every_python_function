# Hash 
# hash() returns the hash value of an object if it has one. Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, as is the case for 1 and 1.0).

key = "randomstring"
print(hash(key))

num_hash = hash((1, 2))
print(num_hash)
