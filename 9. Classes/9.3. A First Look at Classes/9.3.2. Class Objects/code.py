class MyClass:
    """A simple example class"""
    i = 12345
    def __init__(self):
        self.data = []
    def f(self):
        return 'hello world'

x = MyClass()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)