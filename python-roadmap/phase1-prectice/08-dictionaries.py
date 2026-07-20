#1. Apni khud ki details (name, age, city, hobby) ka ek dictionary banao aur sab print karo.

me = {"name" : "saif", "age": 24, "city": "delhi", "hobby" : "playing cricket"};
print (me)

#2. Us dictionary me ek naya key-value pair add karo (jaise "course": "Python"), aur ek existing value update karo.

me["course"] = "python"
print(me)

#3. .get() use karke ek aisi key check karo jo dictionary me hai nahi — default value ke sath print karo.

x = me.get("year", "N/A")
print(x);

y = me.get("name");
print(y)

#4. Ek dictionary banao jisme 3 students ke naam aur unke marks ho (jaise {"Aman": 85, "Priya": 90}), aur .items() use karke sabko print karo.
#5. Ek dictionary me se ek key del ya .pop() se remove karo aur updated dictionary print karo.

students = {"Aman": 85, "Priya": 90}

print(students.items());
print(students.pop("Aman"))
print(students)