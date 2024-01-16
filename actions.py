from abc import ABC, abstractmethod

class Action(ABC):
    @abstractmethod
    def run(self):
        pass

class NewBankProfile(Action):
    def profile_exists(self, data):
        pass

    def create_profile(self):
        pass
    
    def run(self):
        fname = input("Customer's First Name: ")
        lname = input("Customer's Last Name: ")
        security_no = input("Customer's Last Name: ")
        address = input("Customer's Address: ")
        date_of_birth = input("Customer's Date Of Birth: ")
        data = [fname, lname, security_no, address, date_of_birth]
        if not self.profile_exists(data):
            self.create_profile()
        return True

class UpdateBankProfile(Action):
    def profile_exists(self, data):
        pass

    def create_profile(self):
        address = input("Customer's Address: ")
        date_of_birth = input("Customer's Date Of Birth: ")
    
    def run(self):
        fname = input("Customer's First Name: ")
        lname = input("Customer's Last Name: ")
        security_no = input("Customer's Last Name: ")
        data = [fname, lname, security_no]
        if not self.profile_exists(data):
            self.create_profile()
        return True

class NewBankAccount(Action):
    def profile_exists(self, data):
        pass

    def create_profile(self):
        address = input("Customer's Address: ")
        date_of_birth = input("Customer's Date Of Birth: ")

    def create_bank_account(self, data=[]):
        amount = input("Amount to Deposit: ")
        currency = input("Currency of Deposit: ")
        account_type = input("Account Type: ")
    
    def run(self):
        fname = input("Customer's First Name: ")
        lname = input("Customer's Last Name: ")
        security_no = input("Customer's Security Number: ")
        data = [fname, lname, security_no]
        if not self.profile_exists(data):
            self.create_profile()
        self.create_bank_account()
        return True

class BankDeposit(Action):
    def account_exists(self, data):
        pass

    def deposit(self):
        amount = input("Amount to Deposit: ")
    
    def run(self):
        fname = input("Customer's First Name: ")
        lname = input("Customer's Last Name: ")
        account_no = input("Customer's Account Number: ")
        data = [fname, lname, account_no,]
        if self.account_exists(data):
            self.deposit()
        return True

class BankWithdrawal(Action):
    def account_exists(self, data):
        pass

    def deposit(self):
        amount = input("Amount to Deposit: ")
    
    def run(self):
        fname = input("Customer's First Name: ")
        lname = input("Customer's Last Name: ")
        account_no = input("Customer's Account Number: ")
        data = [fname, lname, account_no,]
        if self.account_exists(data):
            self.deposit()
        return True

    
