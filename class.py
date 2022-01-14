Class Dog:
'''Simple Dog class'''

    def init_(self, name):
        self._name = name
    
    def speak(self):
        return "Woof!"
    
def get_pet(pet="dog"):
    
    '''the factory method'''

    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

Class Cat:
'''Simple Cat class'''

    def init_(self, name):
        self._name = name
    
    def speak(self):
        return "Meow!"
    
d = get_pet('dog')
print(d.speak())
