class Person:
    def __init__(self, name="Steve", age=14):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} y.o."
