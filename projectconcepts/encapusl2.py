class BankAccount:
    def __init__(self):
        self.__balance =0  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount()
acc.deposit(5000)
acc.show_balance()