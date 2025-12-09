
    
class Bank:
    def __init__(self):
        self.customers = {}   # {acc_number: {"name":..., "pin":..., "balance":...}}
        self.acc_number = 1000

    def create_account(self):
        name = input("Enter your Name: ")
        pin = input("Set a 4-digit PIN: ")
        
        self.acc_number += 1
        self.customers[self.acc_number] = {"name": name, "pin": pin, "balance": 0}
        
        print(f"\n🎉 Account Created Successfully!")
        print(f"Account Holder : {name}")
        print(f"Account Number : {self.acc_number}")

    def login(self):
        acc = int(input("Enter Account Number: "))
        pin = input("Enter PIN: ")
        
        if acc in self.customers and self.customers[acc]["pin"] == pin:
            print("\nLogin Successful!\n")
            self.menu(acc)
        else:
            print("❌ Invalid Account Number or PIN!")

    def menu(self, acc):
        while True:
            print("\n----- BANK MENU -----")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                print(f"Balance: ₹{self.customers[acc]['balance']}")
            
            elif choice == "2":
                amount = int(input("Enter amount to deposit: ₹"))
                self.customers[acc]["balance"] += amount
                print("Amount Deposited Successfully!")
            
            elif choice == "3":
                amount = int(input("Enter amount to withdraw: ₹"))
                if amount <= self.customers[acc]["balance"]:
                    self.customers[acc]["balance"] -= amount
                    print("Withdrawal Successful!")
                else:
                    print("⚠ Insufficient Balance!")
            
            elif choice == "4":
                print("Logged out successfully!\n")
                break
            
            else:
                print("Invalid choice!")

bank = Bank()

while True:
    print("\n===== WELCOME TO PYTHON BANK =====")
    print("1. Create New Account")
    print("2. Login to Account")
    print("3. Exit")
    user = input("Enter choice: ")

    if user == "1":
        bank.create_account()
    elif user == "2":
        bank.login()
    elif user == "3":
        print("Thank you for using Python Bank 😊")
        break
    else:
        print("Invalid Input!")
                
                        
        