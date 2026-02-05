class BankAccount:
    def __init__(self, owner, initial_balance=0):
        """
        Initialize a bank account.
        
        Args:
            owner: name of the account owner
            initial_balance: initial balance
        """
        self.owner = owner
        self.__balance = max(0, initial_balance)  # Private attribute
        self.__transaction_history = []
        
        if initial_balance > 0:
            self.__transaction_history.append(
                f"Account opened with amount {initial_balance} USD"
            )
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount: deposit amount
        """
        if amount <= 0:
            print("Error: amount must be positive")
            return False
        
        self.__balance += amount
        self.__transaction_history.append(f"Deposit: +{amount} USD")
        print(f"Account topped up by {amount} USD. New balance: {self.__balance} USD")
        return True
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
            amount: withdrawal amount
        """
        if amount <= 0:
            print("Error: amount must be positive")
            return False
        
        if amount > self.__balance:
            print(f"Error: insufficient funds (balance: {self.__balance} USD)")
            return False
        
        self.__balance -= amount
        self.__transaction_history.append(f"Withdrawal: -{amount} USD")
        print(f"Withdrawal of {amount} USD completed. New balance: {self.__balance} USD")
        return True
    
    def get_balance(self):
        """
        Public method to view account balance.
        
        Returns:
            current balance
        """
        return self.__balance
    
    def get_transaction_history(self):
        """
        Returns transaction history.
        
        Returns:
            list of operations
        """
        return self.__transaction_history.copy()
    
    def show_info(self):
        """Display account information"""
        print(f"Account Owner: {self.owner}")
        print(f"Balance: {self.__balance} USD")
        print(f"Number of operations: {len(self.__transaction_history)}")
    
    def __str__(self):
        return f"Account {self.owner}: {self.__balance} USD"


if __name__ == "__main__":
    print("BANK ACCOUNT - ENCAPSULATION DEMONSTRATION")
    
    # Create account
    account = BankAccount("Ivan Petrenko", 1000)
    
    print("\n1. ACCOUNT INFORMATION:")
    account.show_info()
    print(f"Current balance: {account.get_balance()} USD")
    
    print("\n2. ACCOUNT OPERATIONS:")
    
    account.deposit(500)
    account.withdraw(200)
    account.deposit(300)
    account.withdraw(100)
    account.withdraw(5000)  # error
    account.deposit(-50)     # error
    
    print("\n3. FINAL INFORMATION:")
    account.show_info()
    print(f"Balance via get_balance(): {account.get_balance()} USD")
    print(f"Representation: {account}")
    
    print("\n4. TRANSACTION HISTORY:")
    history = account.get_transaction_history()
    for i, operation in enumerate(history, 1):
        print(f"  {i}. {operation}")
    
    print("\n5. ENCAPSULATION DEMONSTRATION:")
    print("Attempt to access __balance directly:")
    try:
        account.__balance = -1000
        print("It seems to work, but this is not the real private attribute!")
    except AttributeError as e:
        print(f"  Error: {e}")
    
    print(f"\nActual balance is still: {account.get_balance()} USD")
    print("Encapsulation protected data from direct modification!")
    
    print("\n6. INTERACTION WITH MULTIPLE ACCOUNTS:")
    
    account1 = BankAccount("Maria Sidorenko", 2000)
    account2 = BankAccount("Peter Kovalenko", 1500)
    account3 = BankAccount("Anna Melnichenko", 3000)
    
    accounts = [account1, account2, account3]
    
    for acc in accounts:
        print(f"  {acc}")
    
    print(f"\nTotal amount in all accounts: {sum(acc.get_balance() for acc in accounts)} USD")
