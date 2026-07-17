# for loop

for loop tab use hota hai jab kisi sequence (list, string, range) ke har element pe ek-ek karke kaam karna ho, ya jab pata ho kitni baar loop chalana hai.

```python
# range() ke sath
for i in range(5):
    print(i)          # 0, 1, 2, 3, 4

# list ke through
fruits = ["apple", "mango", "banana"]
for fruit in fruits:
    print(fruit)

# string ke through
for letter in "Python":
    print(letter)

# range() ke different tarike
for i in range(2, 8):        # 2 se 7 tak
    print(i)

for i in range(0, 10, 2):     # 0,2,4,6,8
    print(i)

# break aur continue
for i in range(10):
    if i == 5:
        break               # loop yahin ruk jayega
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue             # even numbers skip
    print(i)

# enumerate() - index ke sath value
fruits = ["apple", "mango", "banana"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

**Key points:**
- `range(start, stop, step)` — `stop` exclusive hota hai (wo number include nahi hota)
- `break` → loop poori tarah rok deta hai
- `continue` → sirf current iteration skip karta hai, loop chalta rehta hai
- `enumerate()` se index aur value dono ek sath milte hain

**Practice Questions:**

1. 1 se 10 tak ke saare numbers print karo for loop se.
2. 1 se 50 tak ke saare even numbers print karo.
3. Ek list of 5 fruits banao aur for loop se saare fruits print karo.
4. 1 se 20 tak loop chalao, jaise hi number 15 aaye break kar do.
5. 1 se 10 tak loop chalao, lekin 5 ko continue se skip karo aur baaki sab print karo.
6. enumerate() use karke apni fruits list ke index aur naam dono print karo.