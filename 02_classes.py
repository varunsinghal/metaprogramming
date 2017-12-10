
# Classes
# Variable defined at class level is class variable.

class Spam:
    a = 1

    def __init__(self, b):
        self.b = b

    def imethod(self):
        pass

    @classmethod
    def cmethod(cls):
        pass

    @staticmethod
    def smethod():
        pass


# class variable
Spam.a

s = Spam(2)
# instance variable
print(s.b)

# Different method types

# instance method
s.imethod()

# execution at class level
Spam.cmethod()

# function put inside a class
Spam.smethod()
