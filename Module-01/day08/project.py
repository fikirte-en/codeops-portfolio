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
        self.history = []

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
        self.history.append(("deposit", amount))
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
        self.history.append(("withdraw", amount))
        print(f"Withdrew {amount:.2f} ETB. New balance: {self._balance:.2f} ETB")
        self._notify(f"{self.owner} withdrew {amount:.2f} ETB")
        if self._balance < 100:
            self._notify(f"LOW BALANCE warning for {self.owner}: {self._balance:.2f} ETB remaining")

    def undo_last(self):
        if not self.history:
            print("No transactions to undo.")
            return
        action, amount = self.history.pop()
        if action == "deposit":
            self._balance -= amount
            print(f"Undid deposit of {amount:.2f} ETB. Balance: {self._balance:.2f} ETB")
        elif action == "withdraw":
            self._balance += amount
            print(f"Undid withdrawal of {amount:.2f} ETB. Balance: {self._balance:.2f} ETB")

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
        self.history.append(("withdraw", amount))
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


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1



class AccountRegistry:
    def __init__(self):
        self._accounts = {}

    def add(self, account):
        self._accounts[account.account] = account

    def find(self, account_number):
        return self._accounts.get(account_number)

    def list_all(self):
        return [self._accounts[num] for num in sorted(self._accounts)]

  

    def top_by_balance(self, n):
        accounts = self.list_all()
        ranked = sorted(accounts, key=lambda acc: acc.balance, reverse=True)
        return ranked[:n]

    def find_by_number(self, number):
        sorted_numbers = sorted(self._accounts.keys())
        index = binary_search(sorted_numbers, number)
        if index == -1:
            return None
        found_number = sorted_numbers[index]
        return self._accounts[found_number]

    def total_transactions(self, account_number):
        account = self._accounts.get(account_number)
        if account is None:
            return 0
        return self._count_transactions(account.history)

    def _count_transactions(self, history):
        if not history:
            return 0
        return 1 + self._count_transactions(history[1:])


if __name__ == "__main__":
    registry = AccountRegistry()

    acc1 = AccountFactory.create("savings", "Fikir", "1001", 500)
    acc2 = AccountFactory.create("current", "Demelash", "2001", 1500)
    acc3 = AccountFactory.create("savings", "Abel", "3001", 900)

    registry.add(acc1)
    registry.add(acc2)
    registry.add(acc3)

    acc1.subscribe(SMSAlert())
    acc1.subscribe(AuditLog())

    acc1.deposit(100)
    acc1.withdraw(50)
    acc2.deposit(200)

    print("\nTop 2 by balance:")
    for acc in registry.top_by_balance(2):
        print(acc.statement())

    print("\nFind by number (binary search):")
    found = registry.find_by_number("2001")
    print(found.statement() if found else "Not found")

    print("\nTotal transactions for acc1:", registry.total_transactions("1001"))

    print("\nBankConfig is singleton:", BankConfig() is BankConfig())