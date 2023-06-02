class Account:

    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
    
    def getBalance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        
class SavingsAccount(Account):

    def __init__(self,title,balance,interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

account = Account("Ashish", 5000)
print(account.title)
print(account.balance)
balance = 2000
account.deposit(500)
print(account.getBalance())
savings_account = SavingsAccount("Ashish", 5000, 5)
print(savings_account.title)
print(savings_account.balance)
print(savings_account.interestRate)
