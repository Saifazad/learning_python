#1. 1 se 10 tak ke saare numbers print karo for loop se.
# for i in range(1,11):
#     print(i)

#2. 1 se 50 tak ke saare even numbers print karo.

for i in range(2,51):
    isPrime = True
    for num in range(2, i):
     if i % num == 0:
        isPrime = False
        break
    if isPrime:
        print(i)

# pnum = int(input("Enter a number"))

# if pnum < 2:
#    print("Not a prime number")
# else:
#       if(pnum % 2) == 0:
#          print("Not a prime number")
#       else:
#        print("Prime Number")

#3. Ek list of 5 fruits banao aur for loop se saare fruits print karo
fruits = ["apple", "mango", "banana", "orange", "pineapple"]
for i in fruits:
   print(i);       

#4. 1 se 20 tak loop chalao, jaise hi number 15 aaye break kar do.

for i in range(0,20):
   if i >= 15:
      break
   print(i)

#5. 1 se 10 tak loop chalao, lekin 5 ko continue se skip karo aur baaki sab print karo.

for i in range(1,11):
   if(i == 5):
      continue
   print(i)

#6. enumerate() use karke apni fruits list ke index aur naam dono print karo.
for index, fruit in enumerate(fruits):
   print(index, fruit) 