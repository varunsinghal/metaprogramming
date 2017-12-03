# make_addr returns the function, which could be used to execute the code.
# We are making code to get executed by others.

def make_addr(x, y):
    def add():
        return x + y
    return add


x = make_addr(5, 4)
print(x())
