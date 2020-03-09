#need to learn is-a and has-a to work out if something is a class or object
#use is-a when you talk about objects and classes being related to each other by a class relationship
#use a has-a when you talk about objects and classes that are related only because they reference each other

##Animal is-a object (yes, sort of confusing) look at the extra credit

##1) Python(objects) are instances of classes that contain actual values, rather than just being a blueprint
##The (object) part in parentheses specifies the parent class that you are inheriting from (more on this below.) In Python 3 this is no longer necessary because it is the implicit default.
class Animal(object):

##2) As smalltalk, classes themselves are objects

##Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ##dog has-a name
        self.name = name

##Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##cat has-a name
        self.name = name

##? Person is-a object
class Person(object):
    ## person has-a name
    self.name = name

    ## Person has-a pet of some kind
    self.pet = None

##Employemnt is-a ??
class Employment(person):

    def __init__(self, name, salary):
        ###?? hmm what is this strange magic
        super(Employee, self).__init__(name)
        ##??
        self.salary = salary

##Fish is-a animal
class Fish(object):

##Salmon is-a fish
class Salmon(Fish):

#Halibut is-a Fish
class Halibut(Fish):

##rover is-a Dog
rover = Dog("Rover")

##sata is-a Cat
satan = Cat("Satan")

## Mary is-a person
mary = Person("Mary")

##Satan is-a pet of Mary's
mary.pet = satan

##Frank is-a employee who earns 120000 salary
frank = Employee("Frank", 120000)

##Rovert is a pet of Franks
frank.pet = rover

##Flipper is-a fish
flipper = Fish()

##Crousie is-a salmon
crouse = Salmon()

##Harry is-a Halibut
harry = Halibut()