import sys
from actions import (
    NewBankProfile,
    UpdateBankProfile,
    NewBankAccount,
    BankDeposit,
    BankWithdrawal
)


class SystemInterface:
    OPERATION_OPTIONS = {
        "1": "Create a new bank profile for customer",
        "2": "Update bank profile for customer",
        "3": "Create a new account for customer",
        "4": "Withdraw from account",
        "5": "deposit to account"
    }
    OPERATION_SELECTION = {
        "1": NewBankProfile,
        "2": UpdateBankProfile,
        "3": NewBankAccount,
        "4": BankDeposit,
        "5": BankWithdrawal
    }
    def login(self, username, password):
        #add your logic
        return True
    def continue_or_exit(self):
        res = input("do you want to continue? (y/n): ").lower()
        if res == "n":
            sys.exit(1)
        return True
    def greet(self):
        print("Welcome to My Bank! \n")
        print("Login to perform an operation")
    def operations(self, username):
        display = f"\nWelcom {username}\n\nSelect \n"
        for x in self.OPERATION_OPTIONS:
            display += f"{x} to {self.OPERATION_OPTIONS[x]} \n"
        print(display)
        choice = input("")
        entity_class = self.OPERATION_SELECTION.get(choice)
        entity_obj = entity_class()
        entity_obj.run()
        
    def run(self):
        self.greet()
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        self.login(username, password)
        keep_running = True
        while keep_running:
            self.operations(username)
            self.continue_or_exit()

if __name__ == "__main__":
    client = SystemInterface()
    client.run()