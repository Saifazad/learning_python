# Dictionaries

Dictionary ek collection hai jisme data key-value pairs me store hota hai — list ki tarah index (0,1,2) se nahi, balki apne diye hue "key" se value access hoti hai. Fast lookup ke liye best hai.

```python
student = {"name": "Aman", "age": 20, "city": "Delhi"}

print(student["name"])          # Aman
print(student["age"])           # 20

# Adding aur updating values
student["age"] = 21              # existing key update
student["course"] = "Python"     # naya key-value add ho gaya

# Removing values
del student["city"]              # key ke sath value bhi remove
student.pop("course")            # ye bhi remove karta hai, value return karta hai

# Safe access with .get()
print(student.get("name"))              # Aman
print(student.get("marks", "N/A"))      # N/A (key nahi hai, default value milegi)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

for key in student.keys():
    print(key)

for value in student.values():
    print(value)
```

**Key points:**
- Key hamesha unique honi chahiye — same key dobara use karoge to purani value overwrite ho jayegi
- `dict["key"]` se access karoge aur key exist nahi karti to error aayega
- `.get("key")` safe tarika hai — error nahi deta, agar nahi mile to None ya default value deta hai
- `.items()`, `.keys()`, `.values()` — teeno loop ke liye useful hain
- Dictionary bhi mutable hoti hai (change kar sakte ho)
- Note: dictionary ek data type hai; "object" ek general concept hai jo Classes topic me clear hoga

**Practice Questions:**

1. Apni khud ki details (name, age, city, hobby) ka ek dictionary banao aur sab print karo.
2. Us dictionary me ek naya key-value pair add karo (jaise "course": "Python"), aur ek existing value update karo.
3. .get() use karke ek aisi key check karo jo dictionary me hai nahi — default value ke sath print karo.
4. Ek dictionary banao jisme 3 students ke naam aur unke marks ho (jaise {"Aman": 85, "Priya": 90}), aur .items() use karke sabko print karo.
5. Ek dictionary me se ek key del ya .pop() se remove karo aur updated dictionary print karo.