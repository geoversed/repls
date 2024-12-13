
class Account:
  def __init__(self, number, password, balance):
    self.__accountNumber = number
    self.__password = password
    self.__balance = balance

  def getNumber(self):
    """This method returns the account number of this account"""
    print(self.__accountNumber)

  def checkPassword(self, password: str) -> bool:
    """This method should check if a given password == the password for this account"""
    return self.__password == password

  def getBalance(self):
    """This method should return the balance of this account"""
    print(self.__balance)

  def setBalance(self, newBalance: int | float):
    """This method should change the balance of this account to a specified new value"""
    self.__balance = newBalance


class Bank:
  """
  A new bank is defined with a list of bank accounts and a value that keep track of 
  the account number of the most recently added account.
  """
  def __init__(self):
    self.__accounts: list = []
    self.__latestAccount = -1

  def login(self):
    """
    This method should ask the user to give their account number and password,
    returning the account number if they match, or returning -1 if not
    """
    acc_num = input("Enter your account number here -> ")
    password = input("Enter your password -> ")
    if acc_num not in self.__accounts:
      return -1
    
      
    
    pass  #  no instances created yet

  def deposit(self, number):
    """
    This method should ask the user how much money they want to deposit into 
    their account, and correctly update the balance of their account
    """
    pass #  no instances created yet

  def withdraw(self, number):
    """
    This method should ask the user how much money they wanbt to withdraw from
    account, and correctly update the balance of their account
    """
    pass  # no instances created yet

  def checkBalance(self, number):
    """
    This method should display a message telling 
    the user how much money is in their account 
    """
    pass  # no instances created yet
    
  def addAccount(self):
    """
    This method should create a new account with an account number 1 larger
    than the account number or the last account created, a password given
    by the use, and a balance of 0. The account should be added to the bank's
    list of accounts.
    """
    pass  # no instances created yet


def main():
  bank = Bank()
  loggedIn, quitting = False, False
  while not loggedIn and not quitting:
    response = input("You got an account? (y/n/quit) ")

    if "y" in response.lower():
      account = bank.login()
      loggedIn = account != -1

    elif "n" in response.lower():
      bank.addAccount()

    quitting = response == "quit"

  
  while not quitting:
    option = input(
      """
      Press 1 to check your balance
      Press 2 to deposit money
      Press 3 to withdraw money
      Press 4 to exist
      """
    )
    match option:
      
      case "1":
        bank.checkBalance(account)
      
      case "2":
        bank.deposit(account)

      case "3":
        bank.withdraw(account)

      case "4":
        quitting = True

      case _:
        print("Invalid option selected!!")


if __name__ == '__main__':
  main()
