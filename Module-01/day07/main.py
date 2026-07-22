from bank import AccountFactory, AccountRegistry, BankAccount, SavingAccount, CurrentAccount, SMSAlert, AuditLog, BankConfig
class AccountRegistry:
    def __init__(self):
        self._accounts = {}   

    def add(self, account):
        self._accounts[account.account] = account
        account.history = []   

    def find(self, account_number):
        return self._accounts.get(account_number)   
    def list_all(self):

        return [self._accounts[num] for num in sorted(self._accounts)]
    
class BankAccount:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account = account_number
        self._balance = balance
        self._observers = []
        self.history = []   
   

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit failed: amount must be positive.")
            return
        self._balance += amount
        self.history.append(("deposit", amount))   # push onto the stack
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
        self.history.append(("withdraw", amount))   # push onto the stack
        print(f"Withdrew {amount:.2f} ETB. New balance: {self._balance:.2f} ETB")
        self._notify(f"{self.owner} withdrew {amount:.2f} ETB")

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
if __name__ == "__main__":
    registry = AccountRegistry()

    acc1 = AccountFactory.create("savings", "Fikir", "1001", 500)
    acc2 = AccountFactory.create("current", "Demelash", "2001", 200)

    registry.add(acc1)
    registry.add(acc2)

    acc1.deposit(100)
    acc1.withdraw(50)

    found = registry.find("1001")
    print(found.statement())

    found.undo_last()   
    print(found.statement())

    for acc in registry.list_all():
        print(acc.statement())