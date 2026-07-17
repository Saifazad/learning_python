# 1. Ek variable `number` banao, check karo ki wo positive hai, negative hai, ya zero.

num = 10;
if(num >= 0):
    print("positive")
else:
    print("negative")    

#2. Ek variable `age` lekar check karo — agar 18 se zyada hai to "Voting allowed" print karo, warna "Not allowed".  

age = 18;
if(age >= 18):
    print("vote allow")
else:
    print("not allow")

#3. Do numbers lo aur if/elif/else use karke bada number kaunsa hai wo print karo.    

num1, num2 = 9,5;
if(num1 > num2):
    print(num1)
elif(num2 > num1):
    print(num2)
    
#4. `marks` variable banao aur grade decide karo (A: 90+, B: 75-89, C: 50-74, Fail: 50 se kam) — elif use karke.

marks = 10;
if(marks >= 90):
    print("A")
elif(marks >= 75 and marks < 90):
    print("B")
elif(marks >= 50 and marks < 75):
    print("C")
else:
    print("Fail");

#5. `age` aur `has_ticket` (True/False) do variables banao — and operator use karke check karo ki movie dekhne ki entry milegi ya nahi.

age2 = 20
has_ticket = True

if(age2 >= 18 and has_ticket == True):
    print("Entry allow")
else:
    print("Not allow")
