import datetime

class ATM:
     def __init__(self, account_number, pin, balance=0):
         """
         Initializes an ATM object with account details.

         Args:
             account_number (str): The account number.
             pin (str): The PIN associated with the account.
             balance (float): Initial account balance (default: 0).
         """
         self.account_number = account_number
         self.pin = pin
         self.balance = balance
         self.transaction_history = [] # List to store transaction details

     def check_pin(self, entered_pin):
         """
         Verifies if the entered PIN matches the account's PIN.

         Args:
             entered_pin (str): The PIN entered by the user.

         Returns:
             bool: True if the PIN is correct, False otherwise.
         """
         return entered_pin == self.pin

     def get_balance(self):
         """
         Returns the current account balance.

         Returns:
             float: The account balance.
         """
         return self.balance

     def withdraw(self, amount):
         """
         Withdraws cash from the account if sufficient balance is available.

         Args:
             amount (float): The amount to withdraw.

         Returns:
             bool: True if withdrawal is successful, False otherwise.
         """
         if amount > 0 and amount <= self.balance:
             self.balance -= amount
             self.transaction_history.append(
                 f"{datetime.datetime.now()} - Withdrawal: ${amount}"
             )
             return True
         else:
             return False

     def deposit(self, amount):
         """
         Deposits cash into the account.

         Args:
             amount (float): The amount to deposit.
         """
         if amount > 0:
             self.balance += amount
             self.transaction_history.append(
                 f"{datetime.datetime.now()} - Deposit: ${amount}"
             )
             return True
         else:
             return False

     def change_pin(self, new_pin):
         """
         Changes the account's PIN.

         Args:
             new_pin (str): The new PIN to set.
         """
         self.pin = new_pin
         self.transaction_history.append(
             f"{datetime.datetime.now()} - PIN changed successfully."
         )

     def get_transaction_history(self):
         """
         Returns the transaction history for the account.

         Returns:
             list: A list of transaction details.
         """
         return self.transaction_history


 # --- ATM Machine Simulation ---
def atm_simulation(accounts):
     """
     Simulates the ATM machine operations.

     Args:
         accounts (dict): A dictionary containing account information.
     """
     account_number = input("Enter account number: ")

     if account_number not in accounts:
         print("Invalid account number.")
         return

     account = accounts[account_number] # Get the ATM object for the account

     # PIN Verification
     for attempt in range(3):
         entered_pin = input("Enter PIN: ")
         if account.check_pin(entered_pin):
             print("PIN verified.")
             break
         else:
             print("Incorrect PIN. Try again.")
     else:
         print("Too many incorrect PIN attempts. Account locked.")
         return

     while True:
         print("\nATM Menu:")
         print("1. Account Balance Inquiry")
         print("2. Cash Withdrawal")
         print("3. Cash Deposit")
         print("4. PIN Change")
         print("5. Transaction History")
         print("6. Exit")

         choice = input("Enter your choice (1-6): ")

         if choice == "1":
             print(f"Account balance: ${account.get_balance()}")
         elif choice == "2":
             amount = float(input("Enter withdrawal amount: $"))
             if account.withdraw(amount):
                 print("Withdrawal successful.")
                 print(f"New balance: ${account.get_balance()}")
             else:
                 print("Insufficient balance or invalid amount.")
         elif choice == "3":
             amount = float(input("Enter deposit amount: $"))
             if account.deposit(amount):
                 print("Deposit successful.")
                 print(f"New balance: ${account.get_balance()}")
             else:
                 print("Invalid deposit amount.")
         elif choice == "4":
             new_pin = input("Enter new PIN: ")
             account.change_pin(new_pin)
             print("PIN changed successfully.")
         elif choice == "5":
             history = account.get_transaction_history()
             if history:
                 print("\nTransaction History:")
                 for transaction in history:
                     print(transaction)
             else:
                 print("No transaction history found.")
         elif choice == "6":
             print("Exiting ATM. Thank you!")
             break
         else:
             print("Invalid choice. Please enter a number between 1 and 6.")


 # --- Example Usage ---
if __name__ == "__main__":
     # Create some sample accounts
     accounts = {
         "1234567890": ATM("1234567890", "1234", 1000),
         "9876543210": ATM("9876543210", "5678", 500)
     }

     atm_simulation(accounts)
