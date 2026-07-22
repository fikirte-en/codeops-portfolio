from abc import ABC, abstractmethod



class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 1000
        return cls._instance


class SMSAlert:
    def update(self, message):
        print(f"[TeleBirr SMS] {message}")


class AuditLog:
    def update(self, message):
        print(f"[Log] {message}")



class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account = account_number
        self._balance = balance
        self._observers = []

    @property
    def balance(self):
        return self._balance

    def subscribe(self, observer):
        self._observers.append(observer)

    def _notify(self, message):
        for observer in self._observers:
            observer.update(message)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit failed: amount must be positive.")
            return
        self._balance += amount
        print(f"Deposited {amount:.2f} ETB. New balance: {self._balance:.2f} ETB")
        self._notify(f"{self.owner} deposited {amount:.2f} ETB")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal failed: amount must be positive.")
            return
        if amount > self._balance:
            print(f"Withdrawal failed: insufficient funds. Current balance: {self._balance:.2f} ETB")
            return
        self._balance -= amount
        print(f"Withdrew {amount:.2f} ETB. New balance: {self._balance:.2f} ETB")
        self._notify(f"{self.owner} withdrew {amount:.2f} ETB")
        if self._balance < 100:
            self._notify(f"LOW BALANCE warning for {self.owner}: {self._balance:.2f} ETB remaining")

    def statement(self):
        return f"Owner: {self.owner}, Account: {self.account}, Balance: {self._balance:.2f} ETB"


class SavingAccount(BankAccount):
    def __init__(self, owner, account_number, balance=0):
        super().__init__(owner, account_number, balance)
        self.rate = BankConfig().interest_rate  
    def add_interest(self):
        interest = self._balance * self.rate
        self.deposit(interest)

    def statement(self):
        return f"Savings Account — Owner: {self.owner}, Balance: {self._balance:.2f} ETB, Rate: {self.rate}"


class CurrentAccount(BankAccount):
    def __init__(self, owner, account_number, balance=0):
        super().__init__(owner, account_number, balance)
        self.overdraft = BankConfig().overdraft_limit   

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal failed: amount must be positive.")
            return
        if amount > self._balance + self.overdraft:
            print("Withdrawal failed: exceeds overdraft limit.")
            return
        self._balance -= amount
        print(f"Withdrew {amount:.2f} ETB. New balance: {self._balance:.2f} ETB")
        self._notify(f"{self.owner} withdrew {amount:.2f} ETB")

    def statement(self):
        return f"Current Account — Owner: {self.owner}, Balance: {self._balance:.2f} ETB, Overdraft limit: {self.overdraft}"



class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance=0):
        if kind == "savings":
            return SavingAccount(owner, number, balance)
        if kind == "current":
            return CurrentAccount(owner, number, balance)
        raise ValueError(f"Unknown account kind: {kind}")



if __name__ == "__main__":
    acc1 = AccountFactory.create("savings", "Fikir", "1001", 500)
    acc2 = AccountFactory.create("current", "Demelash", "2001", 200)

    acc1.subscribe(SMSAlert())
    acc1.subscribe(AuditLog())
    acc2.subscribe(AuditLog())

    acc1.add_interest()
    acc2.withdraw(900)     
    acc1.withdraw(450)     

    accounts = [acc1, acc2]
    for acc in accounts:
        print(acc.statement())

    print(BankConfig() is BankConfig())   