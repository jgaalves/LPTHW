## Animal é-um object(sim, é meio confuso), veja o credito extra
class Animal(object):
    pass

## é um
class Dog(Animal):

    def __init__(self, name):
        # é um
        self.name = name

# é um
class Cat(Animal):
    
    def __init__(self, name):
        ## é um
        self.name = name

## tem um
class Person(object):

    def __init__(self, name):
        ## é um
        self.name = name 

        ## Person tem um pet de algum tipo
        self.pet = None

#é um
class Employee(Person):
    
    def __init__(self, name, salary):
        ##?? hmm o que é essa magica estranha?
        super(Employee, self).__init__(name)
        #??
        self.salary = salary

##tem um
class Fish(object):
    pass

##??
class Salmon(Fish):
    pass

#??
class Halibut(Fish):
    pass


## rover é-um Dog
rover = Dog("Rover")

##??
satan = Cat("Satan")

##??
mary = Person("Mary")

#??
mary.pet = satan

#??
frank = Employee("Frank", 120000)

#??
frank.pet = rover

#??
flipper = Fish()

#??
crouse = Salmon()

#??
harry = Halibut()