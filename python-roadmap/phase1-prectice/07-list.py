#1. 5 numbers ki ek list banao aur uska sum aur average nikalo.

num = [1,2,3,4,5]

print(sum(num))
print(sum(num)/len(num))

#2. Ek list of 5 fruits banao, usme ek naya fruit append() se add karo, aur ek fruit remove() se hatao.

fruits = ["mango", "orange", "banana", "apple", "pineapple"]

print(fruits)
fruits.append("papaya");
print(fruits)
fruits.remove("mango")
print(fruits)

#4. Ek list of numbers ko sort() se ascending order me arrange karo, phir reverse() se descending karo.

number = [5,3,1,5,2,4,7,8,3]
number.sort()
print(number)

number.reverse()
print(number)

#5. Ek list banao aur for loop se check karo ki usme koi bhi number 50 se bada hai ya nahi (agar hai to print karo).

marks = [40,50,60,10,20,30,70,80];

result = []
for i in marks:
    if i > 50:
        result.append(i)

print(result);        
    
 