class Dog:
    '''Simple Dog class'''

    def __init__(self, name):
        self._name = name
    
    def speak(self):
        return "Woof!"
    
def get_pet(pet="dog"):
    
    '''the factory method'''

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

class Cat:
    '''Simple Cat class'''

    def __init__(self, name):
        self._name = name
    
    def speak(self):
        return "Meow!"
    
d = get_pet('dog')
print(d.speak())

c = get_pet('cat')
print(c.speak())
