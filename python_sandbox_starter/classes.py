# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
    def __init__(self, name):
        self.name = name


brad = User('Brad Man')

print(brad.name)


class Customer(User):
    def __init__(self, name):
        self.name = name