age = 24;
height = 6.10;

print(type(age));
print(type(height));

#2. Ek string number `"25"` ko int me convert karo aur usme `5` add karke result print karo.

num = "25";
result = int(num) + 5;

print(result);

#3. is_raining = True variable banao aur type() se check karo kaunsa data type hai.

is_raining = True;
result = type(is_raining);
print(result);

#4. Ek integer ko string me convert karo aur us string ko kisi doosre string ke sath jodo (concatenate) karke print karo.

num = 24;
result = str(num);
name = "saif";

print(result+name);

#5. Do alag variables banao — ek int aur ek float — unko add karke result ka type print karo (dekho kya hota hai).

num = 10;
weight = 8.5;

sum = num + weight;
print(type(sum));