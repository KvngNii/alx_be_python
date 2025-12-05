class BankAccount:
    """
    A class to represent a bank account with basic banking operations.
    
    Attributes:
        account_balance (float): The current balance of the account
    """
    
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount with an optional initial balance.
        
        Parameters:
            initial_balance (float): Starting balance for the account (default: 0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Parameters:
            amount (float): The amount to deposit
        """
        self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        
        Parameters:
            amount (float): The amount to withdraw
        
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
