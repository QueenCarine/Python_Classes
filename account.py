class Account:
    def __init__(self, name):
        self.name= name
        self.balance = 17.0
        self.transactions = []
        self.loan_balance = 0.0
        self.deposits=[]
        self.withdraws=[]
        self.loan_transactions = []
        self.closed = False
        self.is_frozen=False
    
       
    def deposit(self, amount):
        if self.is_frozen or self.closed:
            return("Inactive account")
        if amount > 0:
            self.balance += amount
            self.deposits.append(amount)
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be more than 0.")


    def withdraw(self, amount):
        if self.is_frozen or self.closed:
            return("Inactive account.")
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.withdraws.append(amount)
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Account cannot be overdrawn.")
    
    def transfer(self, amount,account):
        if self.is_frozen or self.closed:
            return("Inactive account")
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Transferred {amount} to {account}. New balance: {self.balance}"
        else:
            return "Invalid transfer amount."
        
    def get_balance(self):
        return f'Your balance is {self.balance}'
    

    def get_loan(self, amount):
        if self.is_frozen or self.closed:
            return("Inactive account")
        if amount > 0 and self.loan_balance == 0:
            self.loan_balance += amount
            self.balance += amount
            print(f"Loan of {amount} approved. New balance: {self.balance}")
        else:
            print("Loan request denied or already has a loan.")

    def repay_loan(self, amount):
        if amount > 0:
            if self.balance >= amount:
                if amount >= self.loan_balance:
                    self.balance -= self.loan_balance
                    print(f"Loan of {self.loan_balance} fully repaid.")
                    self.loan_balance = 0
                else:
                    self.balance -= amount
                    self.loan_balance -= amount
                    print(f"Repaid {amount}. Remaining loan: {self.loan_balance}")
            else:
                print("Insufficient balance to repay loan.")
        else:
            print("Repayment amount must be positive.")

    def account_details(self):
        print(f" Account owner is {self.name} and balance is {self.get_balance()}.")
    
    def change_account_owner(self,owner):
        self.name = owner
        print (f"Account owner changed to {self.name}")
    
    def  account_statement(self):
         total_deposits = 0
         total_withdrawals = 0
         print(f"Hello {self.name}.Here is your account statement.")
         for deposit in self.deposits:
             total_deposits  += deposit
             print(f"Deposits: {total_deposits}")
         for withdraw in self.withdraws:
            total_withdrawals +=withdraw
            print (f"Withdrawals: {total_withdrawals}")
         print(f"Loan balance:{self.loan_balance}")
         print(f"Current balance:{self.get_balance()}")

    def interest(self):
        if self.closed or self.frozen:
            return "Account is not active."
        interest = self.balance * 0.02
        self.balance += interest
        self.deposits.append(interest)
        println( f"Interest of {interest:.2f} applied. New balance is {self.balance:.2f}")


    def account_freeze(self):
         self.account_frozen = True
         print(f"{self.name},your account has been frozen.")

    def account_unfreeze(self):
        self.account_frozen = False
        print( f"{self.name},your account has been unfrozen.")
    
    def set_min_balance(self,amount):
        self.min_balance = amount
        return f"Minimum balance has been set to {self.min_balance}"
    
    def close_account(self):
        self.closed = True
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        print("Account has been closed and all data reset.")




