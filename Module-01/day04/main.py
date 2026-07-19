class BankAccount:
    def __init__(self,owner, account_number,balance=0):
        self.owner = owner 
        self.account = account_number
        self.__balance = balance

    @property
    def balance(self):
        """Read-only access to the balance."""
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit failed: amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount:.2f} ETB. New balance: {self.__balance:.2f} ETB")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal failed: amount must be positive.")
            return
        if amount > self.__balance:
            print(f"Withdrawal failed: insufficient funds. Current balance: {self.__balance:.2f} ETB")
            return
        self.__balance -= amount
        print(f"Withdrew {amount:.2f} ETB. New balance: {self.__balance:.2f} ETB")



acc1 = BankAccount("Fikir", "1001", 500)
acc2 = BankAccount("Demelash", "1002", 1000)

acc1.deposit(200)
acc1.withdraw(100)
acc1.withdraw(10000)   
acc1.deposit(-50)      

print(f"{acc1.owner}'s balance: {acc1.balance:.2f} ETB")

acc2.withdraw(300)
print(f"{acc2.owner}'s balance: {acc2.balance:.2f} ETB")
 