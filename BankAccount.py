# # Object Oriented Programming Challenge
# For this challenge, create a bank account class that has two attributes:
# 
# * owner
# * balance
# 
# and two methods:
# 
# * deposit
# * withdraw
# 
# As an added requirement, withdrawals may not exceed the available balance.
# 
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"Account owner: {self.owner} \nBalance: ${self.balance}"
    
    def deposit(self,dep_amount):
        self.balance += dep_amount
        print(f"Deposit Accepted \n${dep_amount} has been added to your account")
    def withdraw(self,with_amount):
        if self.balance >= with_amount:
            self.balance -= with_amount
            print(f"Withdrawal Accepted \n${with_amount} has been taken from your account")
        else:
            print("Insuficient Funds!")

#############################################################################

# 1. Instantiate the class
acct1 = Account('Daniel',250)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

