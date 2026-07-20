# Lists

List ek ordered collection hai jisme multiple values ek sath store kar sakte ho — aur ye mutable hoti hai, matlab banane ke baad bhi change kar sakte ho (add, remove, update).

```python
fruits = ["apple", "mango", "banana"]

print(fruits[0])          # apple (indexing 0 se start hoti hai)
print(fruits[-1])         # banana (negative index = last se count)

# Adding aur removing elements
fruits.append("orange")       # end me add karta hai
fruits.insert(1, "grapes")    # specific position pe add karta hai
fruits.remove("banana")       # value ke basis pe remove karta hai
fruits.pop()                  # last element remove karta hai (return bhi karta hai)

# Updating elements
fruits[0] = "kiwi"         # index 0 ki value change ho gayi

# Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])        # [20, 30, 40] - index 1 se 3 tak
print(numbers[:3])         # [10, 20, 30] - shuru se index 2 tak
print(numbers[2:])         # [30, 40, 50] - index 2 se end tak

# Useful methods
print(len(fruits))          # list ki length
fruits.sort()                # ascending order me sort
fruits.reverse()             # order ulta karta hai
print("apple" in fruits)     # check karta hai element list me hai ya nahi

# List me loop
for fruit in fruits:
    print(fruit)
```

**Key points:**
- Index 0 se start hoti hai, -1 se last element milta hai
- List mutable hoti hai — items add/remove/change kar sakte ho
- `append()` end me add karta hai, `insert()` specific position pe
- Slicing `[start:end]` — end exclusive hota hai
- List me alag-alag types ki values bhi ek sath rakh sakte ho (int, str, bool sab)

**Practice Questions:**

1. 5 numbers ki ek list banao aur uska sum aur average nikalo.
2. Ek list of 5 fruits banao, usme ek naya fruit append() se add karo, aur ek fruit remove() se hatao.
3. Ek list [10, 20, 30, 40, 50] lo aur slicing use karke sirf beech ke 3 numbers print karo.
4. Ek list of numbers ko sort() se ascending order me arrange karo, phir reverse() se descending karo.
5. Ek list banao aur for loop se check karo ki usme koi bhi number 50 se bada hai ya nahi (agar hai to print karo).