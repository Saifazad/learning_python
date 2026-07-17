# Functions

Function ek reusable block of code hota hai jo ek specific kaam karta hai. Isse code baar-baar likhna nahi padta — ek baar define karo, jitni baar chaho use karo.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Aman"))       # Hello, Aman!
print(greet("Priya"))      # Hello, Priya!

# Default parameters
def greet2(name, msg="Hello"):
    return f"{msg}, {name}!"

print(greet2("Aman"))              # Hello, Aman!
print(greet2("Aman", "Hi"))        # Hi, Aman!

# Multiple parameters aur return
def add(a, b):
    return a + b

result = add(5, 3)
print(result)          # 8

# Function bina return ke
def show_message():
    print("Welcome to Python!")

show_message()

# *args - multiple values lene ke liye
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))       # 10
```

**Key points:**
- `def` keyword se function define hota hai
- `return` value wapas bhejta hai; agar return nahi likha to function `None` return karta hai
- Parameters (function define karte waqt) aur arguments (function call karte waqt) me fark hota hai
- Default parameter value tab use hoti hai jab argument pass na kiya jaye
- Function ka naam meaningful rakho — kya kaam karta hai wo pata chalna chahiye

**Practice Questions:**

1. Ek function banao square(number) jo kisi number ka square return kare.
2. Ek function banao is_even(number) jo check kare number even hai ya odd, aur True/False return kare.
3. Ek function banao greet(name, greeting="Good Morning") jisme default parameter ho — bina second argument ke aur uske saath, dono tarah se call karo.
4. Ek function banao calculate(a, b, operation) jo operation ke basis pe (jaise "add", "subtract") result return kare.
5. Ek function banao jo *args use karke kisi bhi count ke numbers ka average nikaale.