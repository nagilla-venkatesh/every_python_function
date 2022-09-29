# Filter
# filter() is a built-in function that takes two arguments: a function and an iterable.

def filter_function(x):
    return x % 2 == 0

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = filter(lambda x: x % 2 == 0, lst)
evens_2 = filter(filter_function, lst)

print(evens)
print(evens_2)

print(list(evens))
print(list(evens_2))
