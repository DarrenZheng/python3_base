class Person:
    def __init__(self, name):
        self.name = name
    def say_name(self):
        print("name is", self.name)


p = Person('Darren')

p.say_name();