# OOP Advanced - Inheritance

Inheritance ka matlab hai — ek class dusri class ki properties aur methods "inherit" (le) sakti hai, bina unko dobara likhe. Jo class properties deti hai use Parent class kehte hain, jo leti hai use Child class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):          # Dog, Animal se inherit kar raha hai
    def bark(self):
        print(f"{self.name} is barking")

d = Dog("Tommy")
d.eat()          # Animal wala method use ho gaya - Animal is eating
d.bark()          # Dog ka apna method

# Child class me apna __init__ (super() use karke)
class Animal2:
    def __init__(self, name):
        self.name = name

class Dog2(Animal2):
    def __init__(self, name, breed):
        super().__init__(name)      # parent ka __init__ call kiya
        self.breed = breed

    def show(self):
        print(f"{self.name} is a {self.breed}")

d2 = Dog2("Tommy", "Labrador")
d2.show()          # Tommy is a Labrador
```

**Key points:**
- `class Child(Parent):` — isse inheritance hota hai
- Child class parent ke saare methods/attributes use kar sakta hai
- Child apne khud ke extra methods bhi add kar sakta hai
- `super()` se parent class ke functions ko call karte hain (jaise __init__)
- Real-life example: Vehicle parent ho sakta hai, Car, Bike uske children

**Practice Questions:**

1. Ek parent class Vehicle banao jisme brand attribute aur start() method ho. Ek child class Car banao jo isse inherit kare aur apna khud ka method honk() add kare.
2. Parent class Person banao jisme name, age ho. Child class Employee banao jo isse inherit kare aur apna extra attribute salary add kare — super() use karke.
3. Parent class Shape banao jisme method area() ho (jo abhi kuch na kare). Child classes Circle aur Square banao jo apna-apna area() define karein.
4. Ek child class banao jo parent ka method override kare (same naam ka method likho child me, dekho parent wala chalta hai ya child wala).
5. Animal parent class banao,