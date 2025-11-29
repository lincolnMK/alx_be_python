class BankAccount:
    def __init__(self, account_balance ):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
                
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")