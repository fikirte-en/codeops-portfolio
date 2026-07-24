class BankAccount:
    def __init__(self,owner, account_number,balance=0):
        self.owner = owner 
        self.account = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit failed: amount must be positive.")
            return
        self._balance += amount
        print(f"Deposited {amount:.2f} ETB. New balance: {self._balance:.2f} ETB")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal failed: amount must be positive.")
            return
        if amount > self._balance:
            print(f"Withdrawal failed: insufficient funds. Current balance: {self._balance:.2f} ETB")
            return
        self._balance -= amount
        print(f"Withdrew {amount:.2f} ETB. New balance: {self._balance:.2f} ETB")
    
    def statement(self):
     return f"Owner: {self.owner}, Account: {self.account}, Balance: {self._balance:.2f} ETB"

class SavingAccount(BankAccount):
    def __init__(self, owner, account_number, balance=0, rate=0.0):
        super().__init__(owner, account_number, balance)
        self.rate = rate
     
    def add_interest(self):
       self.deposit(self._balance*self.rate)

    def statement(self):
     return f"Savings Account — Owner: {self.owner}, Balance: {self._balance:.2f} ETB, Rate: {self.rate}"

class CurrentBalance(BankAccount):
   def __init__(self, owner, account_number, balance=0,overdraft = 0):
       super().__init__(owner, account_number, balance)
       self.overdraft = overdraft
   def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal failed: amount must be positive.")
            return
        if amount > self._balance + self.overdraft:
            print("Withdrawal failed: exceeds overdraft limit.")
            return
        self._balance -= amount
        print(f"Withdrew {amount:.2f} ETB. New balance: {self._balance:.2f} ETB")
    
   def statement(self):
     return(f"Current Balance - Owner: {self.owner}, Account: {self.account}, Balance: {self._balance:.2f} ETB, overdraftlimit: {self.overdraft} ")
   

accounts = [BankAccount("fikir","1000oi",700),
            SavingAccount("aster","2999ou",50,0.5),
            CurrentBalance("zion","45667kj",60,90)
            
            ]
for acc in accounts:
    print(acc.statement())
