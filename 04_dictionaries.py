# Dictionaries
# When you make an instance that's a dictionary sitting underneath the cover.

class Spam:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def foo(self):
        pass
        
s = Spam(2, 3)

print(s.__dict__)
# {'x': 2, 'y': 3}

print(Spam.__dict__)
# mappingproxy({'__module__': 'builtins', '__init__': <function Spam.__init__ at 0x7f06620dc620>, 'foo': <function Spam.foo at 0x7f06620dc6a8>, '__dict__': <attribute '__dict__' of 'Spam' objects>, '__weakref__': <attribute '__weakref__' of 'Spam' objects>, '__doc__': None})
