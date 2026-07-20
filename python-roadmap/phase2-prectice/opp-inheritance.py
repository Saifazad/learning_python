class Animal:
    def __init__(self, name):
        self.name = name
    
    def eating(self):
        print(f"the dog is eating which name is {self.name}")


class Dog(Animal):
    def barking(self):
        print(f"dog is barking which name is {self.name}");


d = Dog("Tommy")
d.eating()
d.barking()

        
    