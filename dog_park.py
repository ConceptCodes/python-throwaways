class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pets = []

    def __str__(self):
        return '{} {}'.format(self.name,self.pets)

    '__repr__' == '__str__'

    def add_pet(self, dog):
        self.pets.append(dog)


class Dog:
    def __init__(self, name, weight, owner):
        self.name = name
        self.weight = weight
        self.owner = owner

    def bark(self):
        print('{} is barking!'.format(self.name))

    def __str__(self):
        return self.name




x = Owner('josh',34)
x.add_pet(Dog(name='fito',weight=23.4,owner=x))
print(x)
