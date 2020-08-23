
def log(func):
    def inner(*args, **kwargs):
        print("hi")
        return func(*args, **kwargs)
    return inner

def log1(fun, *dargs, **dkwargs):
    def log(func):
        def inner(*args, **kwargs):
            print(str(len(dargs)))
            return func(*args, **kwargs) + fun(*dargs)
        return inner
    return log

@log
def add(x,y):
    return x + y

@log1(add, 1,2)
def sub(x,y):
    return x - y

# print(add(1,2))
print(sub(10,2))