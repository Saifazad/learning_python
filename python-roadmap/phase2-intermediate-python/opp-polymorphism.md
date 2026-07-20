# Parent Class
class Animal:
    def make_sound(self):
        pass # Yeh bas ek placeholder hai

# Child Class 1
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof! 🐶"

# Child Class 2
class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow! 🐱"

# --- Polymorphism in Action ---

# Ek common function banate hain jo kisi bhi animal ka sound print kar sake
def animal_sound_test(animal_object):
    print(animal_object.make_sound())

# Alag-alag objects banate hain
my_dog = Dog()
my_cat = Cat()

# Ek hi function ko alag objects pass kar rahe hain
animal_sound_test(my_dog)  # Output: Woof! Woof! 🐶
animal_sound_test(my_cat)  # Output: Meow! Meow! 🐱