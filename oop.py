l = list()
print(type(l)) # Eveything in python is an object

class Atm:
    # Function Vs Method
    # Method is a function inside a class
    def __init__(self): # Constructor
        self.pin = ""
        self.balance = 0
        self.menu()

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

