class Person:
    population = 0

    def __init__(self, name):
        Person.population += 1
        self.name = name

    def __del__(self):
        Person.population -= 1
        print("byebye,", self.name)

    def say_hi(self):
        print("hi, i am", self.name)

    def howmany():
        print('we have person:', Person.population)

Person.howmany()

a = Person('abc')
b = Person('cde')

Person.howmany()

del a

Person.howmany()
