class BankAccount:
    def __init__(self, account_number, account_holder_name, account_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance
    def deposit(self, amount):
        self.__account_balance += amount
    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds")
    def display_balance(self):
        print("Account balance: {self.__account_balance}")
# Create an instance of the BankAccount class
account = BankAccount("1234567890", "John Doe", 1000)
# Test the deposit and withdrawal functionality
account.deposit(500)
account.withdraw(300)
account.display_balance()