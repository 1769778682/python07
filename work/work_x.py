class Cat(object):
    def __init__(self):
        self.age = 18

    def __str__(self):
        return str(self.age + 1)


tom = Cat()
print(tom)