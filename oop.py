class BankAccount(object):
  def withdraw(self):
    pass
  def deposit(self):
    pass
'''Inheritance; savings class is a class within a parent class'''
'''it inherits features of the main class, BankAccount class'''
class SavingsAccount(BankAccount):
    '''encapsulation; methods of withdraw and deposit are only used within the savings class. they are not visible to other classes'''
  def __init__(self):
    self.balance = 500

  def deposit(self, amount):
    if (amount < 0):
      return "Invalid deposit amount"
    else:
      self.balance =self.balance + amount
      return self.balance

  def withdraw(self, amount):
    if ( 500< amount < 0):
      return "Invalid withdraw amount"
    elif (amount >= self.balance ):
      return "Cannot withdraw beyond the current account balance"
    elif (self.balance - amount <= 500):
      return "Cannot withdraw beyond the minimum account balance"
    else:
      self.balance = self.balance - amount
      return self.balance

class CurrentAccount(BankAccount):
  def __init__(self):
    self.balance = 0
  def deposit(self, amount):
    if (amount < 0):
      return "Invalid deposit amount"
    else:
      self.balance = self.balance + amount
      return self.balance

  def withdraw(self, amount):
    if (amount < 0):
      return "Invalid withdraw amount"
    elif (amount >= self.balance ):
      return "Cannot withdraw beyond the current account balance"
    else:
      self.balance = self.balance - amount
      return self.balance
