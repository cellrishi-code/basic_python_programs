class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
               hello how you want to do with atm machine ?
               1.enter 1 to create a pin
               2. enter 2 to despoit the amount
               3.enter 3 to withdraw the amount 
               4. enter 4 to cheak the balance
               5. enter 5 to exit the atm machine
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.despoit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.see_balance()
        else:
            print("exit , bye")

    def create_pin(self):
        self.pin = input("enter the pin as ")
        print("pin created successffully")

    def despoit(self):
        temp = input("enter the pin of the atm")
        if temp == self.pin:
            amount = int(input("enter the amont which you want to despoist"))
            self.balance = self.balance + amount
            print("amount has been added succesfully")
        else:
            print("invalid pin of the atm")

    def withdraw(self):
        temp = input("Enter the ATM PIN: ")

        if temp == self.pin:
            amount = int(input("Enter the amount you want to withdraw: "))

            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Amount has been withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid ATM PIN.")

    def see_balance(self):
        temp = input("enter the pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin of the atm")
            
            
            
            
            
sbi = Atm()
            
    
                 
             
            
            
        
        



    