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

class Dog:
    '''one of the objects to be returned'''

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"

class DogFactory:
    '''concrete factory'''
    
    def get_pet(self):
        '''returns dog object'''
        return Dog()

    
    def get_food(self):
        '''returns dog food object'''
        return "Dog Food!"

class PetStore:
    '''petstore houses our abstract factory'''

    def __init__(self, pet_factory=None):
        '''pet_factory is our abstract factory'''
        self._pet_factory = pet_factory

    def show_pet(self):
        '''utility method to display dtails of the objects returned'''
        
        pet= self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("It's food is '{}'".format(pet_food))

#create a concrete factory
factory = DogFactory()

#create a pet store housing our abstract factory
shop = PetStore()

#invoke the utility methos to show details of our pet
shop.show_pet()