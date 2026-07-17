# while loop

while loop tab tak chalta rehta hai jab tak uski condition True rehti hai. for loop se fark ye hai ki yahan pehle se pata nahi hota kitni baar loop chalega — condition ke depend karta hai.

```python
count = 0

while count < 5:
    print(count)
    count += 1        # yeh important hai, warna infinite loop ban jayega

# break aur continue while me bhi kaam karte hain
count = 0
while count < 10:
    if count == 5:
        break
    print(count)
    count += 1

# Controlled infinite loop
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == "exit":
        break
```

**Key points:**
- Condition hamesha check hoti hai loop shuru hone se pehle — agar shuru se hi False hai to loop ek baar bhi nahi chalega
- Sabse common mistake: counter variable (`count += 1`) update karna bhool jana → infinite loop
- `while True:` + `break` ka combo tab use hota hai jab tak koi specific condition (jaise user input) na mile
- `for` loop use karo jab pata ho kitni baar chalana hai; `while` use karo jab condition-based hona

**Practice Questions:**

1. 1 se 10 tak numbers print karo while loop use karke.
2. Ek while loop banao jo count = 0 se start ho aur jab tak count 20 se kam hai, count me 2 add karta rahe aur print kare.
3. User se number lene ka loop banao jo tab tak chale jab tak user 0 input na kare (input() function use karo).
4. while True: use karke ek loop banao jisme 1 se 100 tak numbers print ho, lekin jaise hi 50 aaye break ho jaye.
5. Ek counter while loop se factorial calculate karo kisi bhi number ka (jaise 5 ka factorial = 5×4×3×2×1).