class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Init SchoolMember:', self.name)

    def tell(self):
        print('Name:', self.name, 'Age:', self.age)

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Init Teacher:', self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Salary:', self.name)
        print('Salary:', self.salary)


t = Teacher('Darren', 26, 9000)
t.tell()