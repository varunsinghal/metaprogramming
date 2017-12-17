# Why decorators?

# Debugging
# Debugging with print - only proper way.
# Problem - sucks!! because of code repetition.
# Decorators - wrapper around an existing function

# Benefits of debugging using decorator
# Debugging code is isolated to single location
# This makes it easy to change (or to disable)
# User of a decorator doesn't worry about it
# Limitations - does not work with @classmethod and @staticmethod

from functools import wraps


def debug(func):
    # func is function to be wrapped
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


@debug
def add(x, y):
    return x + y

@debug
def sub(x, y):
    return x - y

@debug
def mul(x, y):
    return x * y

@debug
def div(x, y):
    return x / y


print(add(3, 4))
# add
# 7
