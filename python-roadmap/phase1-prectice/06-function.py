#1.Ek function banao square(number) jo kisi number ka square return kare.
def sqr(num):
    return num * num

print(sqr(10))

#2. Ek function banao is_even(number) jo check kare number even hai ya odd, aur True/False return kare.
def is_even(num):
     if num % 2 == 0:
          return True
     else:
          return False

print(is_even(3))

#3. Ek function banao greet(name, greeting="Good Morning") jisme default parameter ho — bina second argument ke aur uske saath, dono tarah se call karo.


def greet(name , greeting = "Good Morning"):
     print(f"{greeting}, {name}!")

greet("saif")

#4. Ek function banao calculate(a, b, operation) jo operation ke basis pe (jaise "add", "subtract") result return kare.

def calculate(a, b , opration):
     if opration == "add":
          return a + b
     elif opration == "sub":
          return a - b
     elif opration == "mul":
          return a * b
     elif opration == "devide":
          return a/b
     
print(calculate(2,3,"add"))

#5. Ek function banao jo *args use karke kisi bhi count ke numbers ka average nikaale.

def avr(*count):
     return sum(count) / len(count)

print(avr(1,2,3,4,5,6,7))
