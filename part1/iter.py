# Iterator 
# iter() 

class Iterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if self.start <= self.end:
            num = self.start
            self.start += 1
            return num
        raise StopIteration
    

def example():
    custom_obj = Iterator(1, 10)
    obj_iter = iter(custom_obj)
    print(next(obj_iter))
    for num in obj_iter:
        print(num)
        

example()