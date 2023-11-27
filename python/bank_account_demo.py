from bank_account import BankAccount

account = BankAccount("000123", 10000)
print(account)

account.deposit(10000)
account.withdraw(2930)
account.get_balance()
print(account)


