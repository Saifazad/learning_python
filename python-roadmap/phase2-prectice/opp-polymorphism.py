class Animal():
    def __init__(self):
        pass

class Dog(Animal):
    def sound(self):
        print("dog barking")

class Cat(Animal):
    def sound(self):
        print("cat sound")

class elephant(Animal):
    def sound(self):
        print("animal sound")


def soundTest(obj):
    obj.sound()
  
        
c = Cat();

soundTest(c)

