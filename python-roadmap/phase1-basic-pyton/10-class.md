# Classes (Basic)

Class ek blueprint hai kisi cheez ka — jaise ek template jisse hum real cheezein (objects) bana sakte hain. Jab class se koi cheez banti hai, use "object" kehte hain.

```python
class Student:
    def __init__(self, name, age):     # constructor
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old")

# Object banana (class se)
s1 = Student("Aman", 20)
s2 = Student("Priya", 22)

s1.introduce()      # My name is Aman, I am 20 years old
s2.introduce()       # My name is Priya, I am 22 years old

print(s1.name)      # Aman
print(s2.name)       # Priya (har object ka apna alag data hota hai)
```

**self kya hai:**
`self` ek reference hai us particular object ka jispe method call ho raha hai — matlab "ye wala object". Jab `s1.introduce()` call hota hai, Python peeche se `self` ko `s1` bana deta hai, isliye `self.name` uss object (s1) ka hi naam deta hai.

Java/JavaScript/C++ me isko `this` kehte hain — concept bilkul same hai, bas Python me `self` ko manually har method ka pehla parameter likhna padta hai.

**Key points:**
- Class = blueprint/design, Object = uska real instance
- `__init__` constructor hai, object create hote hi automatically chalta hai
- `self` hamesha pehla parameter hota hai class ke functions (methods) me — current object ko refer karta hai
- Object ke attributes ko `object.attribute` se access karte hain (jaise `s1.name`)
- Ek class se multiple, independent objects ban sakte hain — har object ka apna alag data hota hai
- `self` = Python ka `this` (Java/JS/C++ ke equivalent)

**Practice Questions:**

1. Ek class Car banao jisme brand aur model attributes ho, aur ek method show_details() ho jo dono print kare. Uska ek object banake test karo.
2. Class Rectangle banao jisme length aur width ho, aur ek method area() ho jo area calculate karke return kare.
3. Class Person banao jisme name aur age ho, aur ek method is_adult() ho jo True/False return kare (age >= 18 check karke).
4. Ek hi class ke 3 alag objects banao (jaise 3 alag Students) aur for loop se sabke naam print karo (unhe pehle ek list me daal ke).
5. Class BankAccount banao jisme balance ho, ek method deposit(amount) ho jo balance badhaye, aur ek method show_balance() ho.