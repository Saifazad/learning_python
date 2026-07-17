#1. 1 se 10 tak numbers print karo while loop use karke.

count = 0;
while count < 10:
    print(count)
    count+=1
     
#2. Ek while loop banao jo count = 0 se start ho aur jab tak count 20 se kam hai, count me 2 add karta rahe aur print kare.

count = 0;
while count < 100:
      print(count)
      if count < 20:
           count+=2
      else:
           count+=1

#3. User se number lene ka loop banao jo tab tak chale jab tak user 0 input na kare (input() function use karo).

while True:
     user = input("enter '0' to exit: ")
     if user == "0":
        break           
#4. while True: use karke ek loop banao jisme 1 se 100 tak numbers print ho, lekin jaise hi 50 aaye break ho jaye.

counts = 0;
while counts < 100:
     print("counts",counts)
     counts+= 1
     if counts == 50:
          break

#5. Ek counter while loop se factorial calculate karo kisi bhi number ka (jaise 5 ka factorial = 5×4×3×2×1).

usernum = int(input("enter Number"))
   
fact = 1
while usernum > 0:
      print(usernum)
      fact = usernum * fact 
      usernum = usernum - 1

print(fact)

