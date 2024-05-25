from random import randint

class tempBank:
    b_name = "Own Bank Ltd."
    b_balance = 500000
    loan_amount = 0
    loan_permit = True
    shortage = False
    bank_user = {}
    bank_admin = {}

    @classmethod
    def find_user(cls, email):
        for user_id, user_info in cls.bank_user.items():
            if user_info["email"] == email:
                return user_id
        return None

    @classmethod
    def find_admin(cls, email):
        for admin_id, admin_info in cls.bank_admin.items():
            if admin_info["email"] == email:
                return admin_id
        return None

    @classmethod
    def transfer_amount(cls, sender_id, receiver_id, amount):
        sender = cls.bank_user.get(sender_id)
        receiver = cls.bank_user.get(receiver_id)
        if sender and receiver:
            if sender["balance"] >= amount:
                sender["balance"] -= amount
                receiver["balance"] += amount
                sender["history"].append(f"Balance transfer to {receiver['name']}: {amount}")
                receiver["history"].append(f"Balance receive from {sender['name']}: {amount}")
                print(f"Transfer successfully to {receiver['name']}!")
            else:
                print("Insufficient balance")
        else:
            print("Account not found")

class User(tempBank):
    def __init__(self, name, email, address, account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.account_id = str(randint(100, 999))
        self.loan_times = 0
        super().bank_user[self.account_id] = {"name": self.name, "email": self.email, "address": self.address, "account_type": self.account_type, "balance": self.balance, "history": [], "loan_times": 0}
        print("----------------")
        print("Bank Account Created Successfully!!")
        print(f"Welcome Back, {self.name} to {self.b_name}")
        print("We offer for you ")
        print("----------------")
    
    def deposit(self, amount):
        self.balance += amount
        super().bank_user[self.account_id]["balance"] = self.balance
        super().bank_user[self.account_id]["history"].append(f"Deposit: {amount}")
        print("----------------")
        print(f"You have deposited successfully {amount} Tk.")
        print("----------------")
    
    def withdraw(self, amount):
        print("----------------")
        if self.balance < amount:
            print("Withdrawal limit crossed")
        elif super().shortage:
            print(f"Oops! sorry now bank is shortage. So, {self.name} now can't withdraw.")
        else:
            self.balance -= amount
            super().bank_user[self.account_id]["balance"] = self.balance
            super().bank_user[self.account_id]["history"].append(f"Withdraw: {amount}")
            print(f"Successfully withdrew {amount} Tk.")
        print("----------------")

    def check_balance(self):
        print("----------------")
        print(f"You have: {super().bank_user[self.account_id]['balance']} Tk.")
        print("----------------")

    def history(self):
        print("----------------")
        print(f"{self.name} Payment History: ")
        for hist in super().bank_user[self.account_id]["history"]:
            print(hist)
        print("----------------")
    
    def get_loan(self, amount):
        print("----------------")
        if super().b_balance < amount:
            print("Insufficient bank balance")
        elif super().shortage:
            print(f"Oops! sorry now bank is shortage. So, {self.name} now can't get a loan.")
        elif not super().loan_permit:
            print("Bank loan unavailable!!")
        elif self.loan_times >= 2:
            print(f"Sorry {self.name}, you can't take a loan more than 2 times")
        else:
            super().b_balance -= amount
            super().loan_amount += amount
            self.balance += amount
            self.loan_times += 1
            super().bank_user[self.account_id]["balance"] = self.balance
            super().bank_user[self.account_id]["loan_times"] = self.loan_times
            super().bank_user[self.account_id]["history"].append(f"Get loan: {amount}")
            print(f"You've taken {amount} Tk.")
        print("----------------")

    def balance_transfer(self, amount, account_to):
        print("----------------")
        if self.balance < amount:
            print("Insufficient balance")
        elif super().shortage:
            print(f"Oops! sorry now bank is shortage. So, {self.name} now can't transfer balance.")
        elif account_to not in super().bank_user:
            print("Account not found")
        else:
            tempBank.transfer_amount(self.account_id, account_to, amount)
        print("----------------") 

    def user_action_instruction(self):
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Check")
        print("4. History")
        print("5. Get loan")
        print("6. Balance Transfer")
        print("7. Back")

class Admin(tempBank):
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.account_id = str(randint(100, 999))
        super().bank_admin[self.account_id] = {"name": self.name, "email": email, "account_id": self.account_id}
        print("----------------...")
        print("Admin account created successfully!")
        print("----------------...")
    
    def admin_action_instruction(self):
        print("1. Delete user account")
        print("2. See all user accounts")
        print("3. Check total available bank balance")
        print("4. Check the total loan amount")
        print("5. Turn on/off loan feature")
        print("6. Back")
    
    def delete_user_account(self, account_id):
        print(".......................")
        if account_id in super().bank_user:
            del super().bank_user[account_id]
            print(f"Provided account deleted successfully. Account ID: {account_id}")
        else:
            print("Account ID not found!")
        print(".......................")

    def see_all_users(self):
        print(".......................")
        for key, value in tempBank.bank_user.items():
            print(f"Account ID: {key}, Account Info: {value}")
        print(".......................")

    def b_balance_check(self):
        print("----------------....")
        print(f"Available bank balance is: {self.b_balance}")
        print("----------------....")

    def bank_loan_check(self):
        print("----------------....")
        print(f"Total loan amount: {self.loan_amount}")
        print("----------------....")

    def bank_loan_feature(self, on_off_option):
        print("..................")
        tempBank.loan_permit = True if on_off_option == 1 else False
        print(f"Bank loan feature successfully {'ON' if tempBank.loan_permit else 'OFF'}")
        print("..................")

def admin_login():
    while True:
        print("Please Login First")
        email = input("Please Enter Your Email: ")
        if tempBank.find_admin(email):
            admin_menu()
            return
        else:
            print("Email Not Exist")
            return

def admin_menu():
    while True:
        print("Welcome To Admin Dashboard")
        print("1. Create New Admin")
        print("2. Remove User")
        print("3. View Admins")
        print("4. View Users")
        print("5. Bank Stock")
        print("6. Loan Balance")
        print("7. Set Loan Status")
        print("8. Exit")
        
        option = int(input("Please Insert An Option: "))
        
        if option == 1:
            admin_name = input("Type Admin Name: ").lower()
            admin_email = input("Type Admin Email: ").lower()
            if tempBank.find_admin(admin_email):
                print("Sorry, this email already exists")
            else:
                new_admin = Admin(admin_name, admin_email)
                print("Admin account created successfully.")
        elif option == 2:
            user_email = input("Type User Email: ")
            user_id = tempBank.find_user(user_email)
            if user_id:
                Admin("temp", "temp").delete_user_account(user_id)
            else:
                print("User not found")
        elif option == 3:
            for admin_id, admin_info in tempBank.bank_admin.items():
                print(f"Admin Name: {admin_info['name']}\tAdmin Email: {admin_info['email']}")
        elif option == 4:
            for user_id, user_info in tempBank.bank_user.items():
                print(f"User Name: {user_info['name']}\tUser Email: {user_info['email']}")
        elif option == 5:
            Admin("temp", "temp").b_balance_check()
        elif option == 6:
            Admin("temp", "temp").bank_loan_check()
        elif option == 7:
            print("Loan Status\n1. On\n2. Off")
            status = int(input("Type 1 or 2: "))
            Admin("temp", "temp").bank_loan_feature(status)
        elif option == 8:
            print("Exiting...")
            return
        else:
            print("Invalid Input")

def user_menu(client):
    while True:
        print(f"Welcome To {tempBank.b_name}")
        client.user_action_instruction()
        option = int(input("Please Insert An Option: "))

        if option == 1:
            amount = int(input("Enter Deposit Amount: "))
            client.deposit(amount)
        elif option == 2:
            amount = int(input("Enter Withdraw Amount: "))
            client.withdraw(amount)
        elif option == 3:
            client.check_balance()
        elif option == 4:
            client.history()
        elif option == 5:
            amount = int(input("Enter Loan Amount: "))
            client.get_loan(amount)
        elif option == 6:
            amount = int(input("Enter Transfer Amount: "))
            receiver_account = input("Enter Receiver's Account ID: ")
            client.balance_transfer(amount, receiver_account)
        elif option == 7:
            print("Exiting...")
            return
        else:
            print("Invalid Input")

def main():
    
    default_admin_name = "nahid"
    default_admin_email = "nahidusha@gmail.com"
    default_admin = Admin(default_admin_name, default_admin_email)

    while True:
        print(f"Welcome to {tempBank.b_name}")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        option = int(input("Enter Options: "))
        if option == 1:
            print("The default admin gmail is = nahidusha@gmail.com")
            admin_login()
        elif option == 2:
            name = input("Input your name: ")
            email = input("Input your email: ")
            address = input("Input your address: ")
            print("1. Savings")
            print("2. Current")
            account_type = int(input("Select account type: "))
            account_type = "Savings" if account_type == 1 else "Current"
            user = User(name, email, address, account_type)
            user_menu(user)
        elif option == 3:
            break
        else:
            print("Invalid Option")

if __name__ == "__main__":
    main()
