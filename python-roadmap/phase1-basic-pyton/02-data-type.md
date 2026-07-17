# Data Types

Data type batata hai ki variable ke andar kis kism ki value store hai — number, text, ya kuch aur. Python khud detect kar leta hai (dynamic typing), manually batana nahi padta.

```python
age = 20              # int (whole number)
price = 99.5          # float (decimal number)
name = "Aman"         # str (text/string)
is_active = True      # bool (True/False)

print(type(age))       # <class 'int'>
print(type(name))      # <class 'str'>

# Type conversion
x = "10"
y = int(x)              # string se int
print(y + 5)            # 15

z = str(20)              # int se string
```

**Key points:**
- `int` → whole numbers (10, -5, 100)
- `float` → decimal numbers (9.5, -3.2)
- `str` → text, hamesha quotes me (`"hello"` ya `'hello'`)
- `bool` → sirf `True` ya `False` (capital letter zaroori hai)
- `type()` function se koi bhi variable ka type check kar sakte ho
- Type conversion ke liye `int()`, `float()`, `str()` use hote hain

**Practice Questions:**

1. Ek variable me apni age integer me store karo, aur ek variable me apna weight float me store karo. Dono ka `type()` print karke check karo.
2. Ek string number `"25"` ko int me convert karo aur usme `5` add karke result print karo.
3. `is_raining = True` variable banao aur `type()` se check karo kaunsa data type hai.
4. Ek integer ko string me convert karo aur us string ko kisi doosre string ke sath jodo (concatenate) karke print karo.
5. Do alag variables banao — ek int aur ek float — unko add karke result ka type print karo (dekho kya hota hai).