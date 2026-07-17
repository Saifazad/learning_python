# if / else

if/else ka use tab hota hai jab kisi condition ke basis pe decide karna ho ki kaunsa code chalega. Agar condition True hai to if wala block chalega, warna else wala.

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")

# Multiple conditions ke liye elif
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Logical operators
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")

if age < 18 or not has_id:
    print("Entry denied")
```

**Key points:**
- Indentation (spacing) bahut important hai — Python isi se block identify karta hai
- `elif` = "else if", jitne chahiye utne use kar sakte ho
- `and`, `or`, `not` — logical operators multiple conditions check karne ke liye
- `else` optional hai, zaroori nahi hamesha likhna
- Comparison operators: `==`, `!=`, `>`, `<`, `>=`, `<=`

**Practice Questions:**

1. Ek variable `number` banao, check karo ki wo positive hai, negative hai, ya zero.
2. Ek variable `age` lekar check karo — agar 18 se zyada hai to "Voting allowed" print karo, warna "Not allowed".
3. Do numbers lo aur if/elif/else use karke bada number kaunsa hai wo print karo.
4. `marks` variable banao aur grade decide karo (A: 90+, B: 75-89, C: 50-74, Fail: 50 se kam) — elif use karke.
5. `age` aur `has_ticket` (True/False) do variables banao — and operator use karke check karo ki movie dekhne ki entry milegi ya nahi.