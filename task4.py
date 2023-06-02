class Account:

    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
        
class SavingsAccount(Account):

    def __init__(self,title,balance,interest_rate):
        super().__init__(title, balance)
        self.interest_rate = interest_rate

account = Account("Ashish", 5000)
print(account.title)
print(account.balance)

savings_account = SavingsAccount("Ashish", 5000, 5)
print(savings_account.title)
print(savings_account.balance)
print(savings_account.interest_rate)
