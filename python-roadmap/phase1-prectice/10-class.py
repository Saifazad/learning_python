#Ek class Car banao jisme brand aur model attributes ho, aur ek method show_details() ho jo dono print kare. Uska ek object banake test karo.

class Car:
    def __init__(self, brand , model):
        self.brand = brand
        self.model = model


    def show_details(self):
        print(f"Brand : {self.brand}")
        print(f"Brand : {self.model}")


s1 = Car("maruti", 2023)
s1.show_details();

#2. Class Rectangle banao jisme length aur width ho, aur ek method area() ho jo area calculate karke return kare.

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        result = self.length * self.width
        print(f"Area is : {result}")


s2 = Rectangle(12,12)
s2.area()

#3. Class Person banao jisme name aur age ho, aur ek method is_adult() ho jo True/False return kare (age >= 18 check karke).

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return print(self.age >= 18)
      

s3 = Person("Saif", 25);
s3.is_adult();

#4. Ek hi class ke 3 alag objects banao (jaise 3 alag Students) aur for loop se sabke naam print karo (unhe pehle ek list me daal ke).

class Students():
    def __init__(self, name, section , roll):
        self.name = name
        self.section = section
        self.roll = roll;

    def students_details(self):
        print(f"Name: {self.name} Roll : {self.roll} Class : {self.section}");

obj1 = Students("saif",5, 12)
obj2 = Students("amit", 5, 14)
obj3 = Students("sumit", 5,13)

student_list = [obj1, obj2, obj3];

for student in student_list:
    print(student.name);


#5. Class BankAccount banao jisme balance ho, ek method deposit(amount) ho jo balance badhaye, aur ek method show_balance() ho.

class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"deposit success {amount}")

    def show_balance(self):
        print(self.balance);

account = BankAccount()
account.deposit(1000)
account.deposit(1000)
account.show_balance();


         
     


    


 








        

   