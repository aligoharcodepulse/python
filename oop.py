l = list()
print(type(l)) # Eveything in python is an object

class Atm:
    # Function Vs Method
    # Method is a function inside a class
    # Jo Object bnta hai wo hii self hai
    # Through self we can access one method from another method inside the same class

    # Static/Class Variable
    __counter = 1

    def __init__(self): # Constructor (Magic Method)
        # Instance Variable
        self.pin = ""
        self.balance = 0

        self.sno = Atm.__counter
        Atm.__counter += 1
        print(self.sno)
        self.menu()
        print(id(self))

    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
            print("Counter Updated")
        else:
            print("Not Allowed")
        

    def menu(self):
        user_input = input("""
        How would you like to proceed?
        1. Enter 1 to Create Pin
        2. Enter 2 to Deposit
        3. Enter 3 to Withdraw
        4. Enter 4 to Check Balance
        5. ENter 5 to Exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.current_balance()
        else:
            print("bye")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin created successfully")
        self.menu()

    def deposit(self):
        temp = input("Enter Pin: ")
        if temp == self.pin:
            amount = int(input("Enter Amount: "))
            self.balance = self.balance + amount
            print("Deposit Successful")

        else:
            print("Invalid Pin")
        self.menu()


    def withdraw(self):
        temp = input("Enter Pin: ")
        if temp == self.pin:
            amount = int(input("Enter Amount: "))
            if amount  <= self.balance:
                self.balance -= amount
                print("Withdraw Successful")
            else:
                print("Insufficient Balance")

        else:
            print("Invalid Pin")
        self.menu()


    def current_balance(self):
        temp = input("Enter Pin: ")
        if temp == self.pin:
            print("Current Balance: ", self.balance)
        else:
            print("Invalid Pin")
        self.menu()


obj = Atm()
obj1 = Atm()
obj2 = Atm()
# print(id(obj))




class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    # Other Magic Methods
    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        temp_num = self.num * other.den + self.den * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

    def __sub__(self, other):
        temp_num = self.num * other.den - self.den * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num, temp_den)

    def __truediv__(self, other):
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num, temp_den)

obj = Fraction(4,5)
obj1 = Fraction(3,5)
print(obj, obj1)
print(obj + obj1)
print(obj - obj1)
print(obj * obj1)
print(obj / obj1)



# Encapsulation
# Nothing in python is completely private
# below variables can be accessed through _Atm__balance
class Atm:
    # Function Vs Method
    # Method is a function inside a class
    # Jo Object bnta hai wo hii self hai
    # Through self we can access one method from another method inside the same class
    def __init__(self): # Constructor (Magic Method)
        self.__pin = "" # Instance Variable
        self.__balance = 0
        self.menu()
        print(id(self))

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin)  == str:
            self.__pin = new_pin
            print("Pin Changed")
        else:
            print("Not Allowed")
        

    def menu(self):
        user_input = input("""
        How would you like to proceed?
        1. Enter 1 to Create Pin
        2. Enter 2 to Deposit
        3. Enter 3 to Withdraw
        4. Enter 4 to Check Balance
        5. ENter 5 to Exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.current_balance()
        else:
            print("bye")

    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin created successfully")
        self.menu()

    def deposit(self):
        temp = input("Enter Pin: ")
        if temp == self.__pin:
            amount = int(input("Enter Amount: "))
            self.__balance = self.__balance + amount
            print("Deposit Successful")

        else:
            print("Invalid Pin")
        self.menu()


    def withdraw(self):
        temp = input("Enter Pin: ")
        if temp == self.__pin:
            amount = int(input("Enter Amount: "))
            if amount  <= self.__balance:
                self.__balance -= amount
                print("Withdraw Successful")
            else:
                print("Insufficient Balance")

        else:
            print("Invalid Pin")
        self.menu()


    def current_balance(self):
        temp = input("Enter Pin: ")
        if temp == self.__pin:
            print("Current Balance: ", self.__balance)
        else:
            print("Invalid Pin")
        self.menu()


obj = Atm() # obj is reference variable
print(obj.get_pin())
obj.set_pin(5678)
print(obj.get_pin())


# Pass by Reference
# Class Objects are mutable
# If you pass the object..changes may occur in that
class Customer:
    def __init__(self, name):
       self.name = name

    def intro(self):
        print("I'm", self.name)

def greet(customer): # Aliasing
    print(id(customer))
    customer.name = "Ahmad"
    print(customer.name)
    print(id(customer))

obj = Customer("Ali")
print(id(obj))
greet(obj)
print(obj.name)

obj1 = Customer("Ahmad")
obj2 = Customer("Ali")
l = [obj1, obj2] # Collection of Objects

for i in l:
    i.intro()



# Aggregation
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pincode, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pincode, new_state)

class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pincode, new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state

addr = Address("Peshawar", "24420", "Pakistan")
cust = Customer("Ali", "Male", addr)

print(cust.name, cust.gender, cust.address.city)
cust.edit_profile("Ahmad", "Charsadda", 24421, "KP")
print(cust.name, cust.gender, cust.address.city, cust.address.pincode)



# Inheritence
class User:
    def login(self):
        print("Login")

    def register(self):
        print("Register")

class Student(User):
    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")

stu1 = Student()
stu1.register()
stu1.login()
stu1.enroll()
stu1.review()


class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera

    def buy(self):
        print("Buying Phone")

class SmartPhone(Phone):
    def buy(self): # Method Overriding -> Polymorphism
        print("Buying Smart Phone")
    

s1 = SmartPhone(10000, "Apple", "2 Pixel")
# print(s1.__brand) error can't access private
s1.buy()


# Polymorphism
# Method Overriding, Method Overloading, and Operator Overloading
class A:
    def __init__(self):
        self.var1 = 100

    def display1(self, var1):
        print("Class A: ", self.var1)

class B(A):
    def display2(self, var1):
        print("Class B: ", self.var1)

obj = B()
obj.display1(200)


# Example
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Cunstructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Phone):

    def buy(self):
        print("Buying a Smart Phone")
        super().buy()

s = SmartPhone(20000,"Aplle", 13)
s.buy()


# Example
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Cunstructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside Smart Phone Cunstructor")

s = SmartPhone(20000,"Samsung", 12, "Android", 2)
print(s.os)
print(s.brand)


# Example
class Parent:
    def __init__(self):
        self.num = 100

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 200

    def show(self):
        print(self.num)
        print(self.var)

son = Child()
son.show()


# Multi-level Inheritence
class Product:
    def review(self):
        print("Product Customer Review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside Phone Cunstructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(2000, "Apple", 13)
p = Phone(1000, "Samsung", 11)

s.buy()
s.review()
p.review()


# Another Example
class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        return 30

    def m2(self):
        return 40

class C(B):
    def m2(self):
        return 20

obj1 = A()
obj2 = B()
obj3 = C()
print(obj1.m1() + obj3.m1() + obj3.m2())


# Hierarchal Inheritence
class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside Phone Cunstructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

    def return_phone(self):
        print("Returning a Phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

s = SmartPhone(2000,"Apple", 13)
s.buy()
f = FeaturePhone(1000,"Apple", 12)
s.return_phone()


# Multiple Inheritence
class Product:
    def review(self):
        print("Product Customer Review")

    def buy(self):
        print("Buying a Product")

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone Cunstructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Product, Phone):
    pass

s = SmartPhone(2000,"Apple", 13)
s.buy() # MRO (Method Resolution Order)
s.review()



