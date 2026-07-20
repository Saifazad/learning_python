# Exception Handling

Jab code chalte waqt koi error (exception) aata hai, to normally program crash ho jaata hai. Exception handling se hum us error ko "catch" karke handle kar sakte hain, taaki program crash na ho aur graceful tarike se aage badhe.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")

# else aur finally
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result:", result)      # sirf tab chalega jab error NAHI aaya
finally:
    print("Execution complete.")   # ye HAMESHA chalega, error aaye ya na aaye

# Multiple exceptions ek sath handle karna
try:
    pass
except (ValueError, TypeError):
    print("Value ya type me problem hai")
```

**Common exceptions jo aksar milte hain:**
- `ZeroDivisionError` → kisi number ko 0 se divide karne pe
- `ValueError` → galat type ki value di (jaise "abc" ko int() me convert karna)
- `TypeError` → galat data type ke sath operation (jaise str + int)
- `FileNotFoundError` → file exist nahi karti
- `KeyError` → dictionary me key exist nahi karti
- `IndexError` → list me wo index exist nahi karta

**Key points:**
- `try` → risky code jahan error aa sakta hai
- `except` → jab error aata hai to ye block chalta hai
- `else` → sirf tab chalta hai jab try block me koi error na aaya ho
- `finally` → hamesha chalta hai, chahe error aaye ya na aaye (jaise file close karna, cleanup)
- Specific exception (ZeroDivisionError) use karna better hai generic except: se, kyunki pata chalta hai exact kya galat hua
- Ek try ke sath multiple except block ho sakte hain, alag-alag error types ke liye

**Practice Questions:**

1. User se ek number lo aur usse 10 ko divide karo — ZeroDivisionError handle karo.
2. User se ek number input lo (int() use karke) — agar user text likh de (jaise "abc"), ValueError handle karo.
3. Ek list [1, 2, 3] banao aur try/except use karke ek aisa index access karo jo exist nahi karta — IndexError handle karo.
4. Ek dictionary banao aur ek aisi key access karo jo exist nahi karti — KeyError handle karo.
5. Ek function banao safe_divide(a, b) jo try/except/else/finally sab use kare — divide kare, error handle kare, aur end me hamesha "Operation complete" print kare.