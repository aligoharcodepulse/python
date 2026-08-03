l = list()
print(type(l)) # Eveything in python is an object

class Atm:
    # Function Vs Method
    # Method is a function inside a class
    # Jo Object bnta hai wo hii self hai
    # Through self we can access one method from another method inside the same class
    def __init__(self): # Constructor (Magic Method)
        self.pin = ""
        self.balance = 0
        self.menu()
        print(id(self))

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
print(id(obj))




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


