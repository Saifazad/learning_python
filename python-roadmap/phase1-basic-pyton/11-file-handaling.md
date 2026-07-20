# File Handling

File handling se hum computer ki files ko Python code se read, write, ya update kar sakte hain — jaise koi text file me data save karna ya usse padhna.

```python
# File me likhna (write mode)
with open("data.txt", "w") as f:
    f.write("Hello Python")

# File se padhna (read mode)
with open("data.txt", "r") as f:
    content = f.read()
    print(content)

# Line by line padhna
with open("data.txt", "r") as f:
    for line in f:
        print(line)

# Append mode - purana data safe rehta hai
with open("data.txt", "a") as f:
    f.write("\nNew line added")
```

**File modes:**
- `"r"` → read — file padhne ke liye (agar file na ho to error)
- `"w"` → write — nayi file banata hai ya purani ko overwrite kar deta hai
- `"a"` → append — end me naya data add karta hai, purana data delete nahi hota
- `"r+"` → read aur write dono

**with kyun use karte hain:**
```python
# with ke bina (manual close karna padta hai)
f = open("data.txt", "r")
content = f.read()
f.close()          # ye bhoolna easy hai

# with ke sath (automatically close ho jaata hai)
with open("data.txt", "r") as f:
    content = f.read()
# yahan file already close ho chuki hai
```

**Key points:**
- `with open(...) as f:` best practice hai — file automatically close ho jaati hai, bhoolne ka risk nahi
- `"w"` mode purani file ka data delete kar deta hai — careful rehna
- `"a"` mode purane data ko safe rakhte hue naya data add karta hai
- `.read()` — poori file ek string me deta hai
- `.readlines()` — har line ek list item ke form me deta hai
- File agar exist nahi karti aur "w" ya "a" mode use kiya, to Python naye se bana deta hai

**Practice Questions:**

1. Ek file notes.txt banao aur usme apna naam aur ek sentence likho ("w" mode se).
2. Wahi file "r" mode se open karke uska content print karo.
3. Us file me "a" mode se ek aur line add karo, phir dobara padh ke check karo ki dono lines hain ya nahi.
4. Ek file banao jisme 5 alag lines ho (numbers likh do 1 se 5 tak, har line pe ek number), phir usse for line in f: use karke sab lines print karo.
5. Ek function banao save_name(name) jo har call pe diya gaya naam ek file me naye line pe add kare (append mode use karke) — 3 baar alag naam se call karke check karo.