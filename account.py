from datetime import datetime

class Transaction:
    def __init__(self,amount,narration,transaction_type,date_time=None):
        self.amount=amount
        self.narration=narration
        self.transaction_type=transaction_type
        self.date_time=date_time or datetime.now()
    def __str__(self):
        return f"{self.date_time} | {self.transaction_type.upper()} |{self.narration} |{self.amount} "    





class Account:
    def __init__(self, name,account_number):
        self.name= name
        self.__account_number=account_number
        self.__balance = 0
        self.transactions = []
        self.loan_balance = 0
        self.loan_transactions = []
        self.closed = False
        self.is_frozen=False
    
    def get_account_number(self):
        return self.__account_number
    
    def get_name(self):
        return self.name
    
    def get_transactions(self):
         print(len(self.transactions))
         return "\n".join(str(t) for t in self.transactions)
    
    def get_balance(self):
        self.__balance=0
        for transaction in self.transactions:
            if transaction.transaction_type in ["deposit" , "transfer_from"]:
               self.__balance+=transaction.amount
            elif transaction.transaction_type in ["withdraw","transfer"]:
                 self.__balance-=transaction.amount
        return self.__balance 

    
    def deposit(self,amount):
        if self.is_frozen or self.closed:
            return("Inactive account")
        if amount > 0:
            transaction=Transaction(amount,"Made a deposit","deposit")
            self.transactions.append(transaction)
            return f"Deposited {amount} successfully. New balance: {self.get_balance()}"
        else:
            return "Deposit amount must be more than 0."
    
    def withdraw(self,amount):
         if self.is_frozen or self.closed:
            return("Inactive account.")
         if amount > 0 and amount < self.__balance:
             transaction=Transaction(amount,"Made a withdraw",transaction_type="withdraw")
             self.transactions.append(transaction)
             return f"Withdrew {amount} successfully. New balance: {self.get_balance()}"
         else:
           return "Account cannot be overdrawn."

    def transfer(self, amount, recipient):
     if self.closed or self.is_frozen:
        return 'Inactive account'
     if amount > 0 and amount <= self.get_balance():
        self.transactions.append(Transaction(amount, "Made a transfer", transaction_type="transfer"))
        recipient.transactions.append(Transaction(amount, "Got a deposit", transaction_type="transfer_from"))
        return f"Transferred {amount} to {recipient.get_name()}. Your new balance is: {self.get_balance()}"
     else:
        return "Transfer failed: insufficient funds or invalid amount."     
     
    
    def calculate_loan_limit(self):
        total_deposits=sum(t.amount for t in self.transactions if t.transaction_type is "deposit")
        return total_deposits//3

    def get_loan(self, amount):
        if self.is_frozen or self.closed:
            return "Inactive account"
        if self.loan_balance>0:
            return "You already have a loan"
        
        loan_limit=self.calculate_loan_limit()
        if amount > 0 and amount <= loan_limit:
            self.transactions.append(Transaction(amount,"Loan application","deposit"))
            self.loan_balance += amount
            return f"Loan of {amount} approved. New balance: {self.get_balance()}"
        else:
            return "Loan amount exceeds your limit."
     
    def repay_loan(self, amount):
     if self.is_frozen or self.closed:
        return "Inactive account"
     if self.loan_balance == 0:
        return "You don't have an outstanding loan"
     if amount <= 0:
        return "Repayment amount must be positive"
     if amount >= self.loan_balance:
        excess = amount - self.loan_balance
        self.loan_balance = 0
        if excess >= 0:
             self.transactions.append(Transaction(excess, "Excess after loan repayment", "deposit"))
        return f"Loan fully repaid. Extra {excess} added to your account. Your balance is {self.get_balance()}"
     else:
        self.loan_balance -= amount
        self.transactions.append(Transaction(amount, "Partial loan repayment", "withdraw"))
        return f"Loan partially repaid. Remaining loan balance: {self.loan_balance} and balance is {self.get_balance()}" 
   
    def account_details(self):
        print(f" Account owner is {self.name} and balance is {self.get_balance()}.")
    
    def change_account_owner(self,owner):
        self.name = owner
        print (f"Account owner changed to {self.name}")
        
    def account_statement(self):
        print(f" Hello ,Statement for account: {self.__account_number} - {self.name}")
        for i,transaction in enumerate(self.transactions):
            print(f"Transaction {i+1} :{transaction}")

    def interest(self):
        if self.closed or self.is_frozen:
            return "Account is not active."
        interest = self.get_balance() * 0.04
        self.transactions.append(Transaction(interest, "monthly interest ", "deposit"))
        return f"Interest of {interest:.2f} applied. New balance is {self.get_balance():.2f}"


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
        self.loan = 0
        print("Account has been closed and all data reset.")


account1=Account("Queen",2345)
account2=Account("Beauty",234)

print(account1.deposit(500))
print(account1.withdraw(100))
print(account1.transfer(50,account2))
print(account1.get_loan(100))
print(account1.account_statement())
print(account1.repay_loan(50))
print(account1.account_details())
print(account1.change_account_owner("Carine"))
print(account1.interest())
print(account1.get_transactions())
print(account2.get_transactions())

