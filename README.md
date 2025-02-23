# OctaNet-Internship

****ATM Machine Simulation using Python****

**# Functions to Include:**
   **Account balance inquiry* 
   
   **Cash withdrawal*
   
   **Cash deposit*    
   
   **PIN change*
   
   **Transaction history*

Sample Accounts to use, this are in the code if you want to change you can change:

**1.**   

 *Account no. - 1234567890*
 
  *PIN -* 1234 
 
  *Available Money -* 1000      


**2.**       
  
  *Account no. - 9876543210*
   
  *PIN -* 5678 
  
  *Available Money -* 500


**Here are some key points from the above ATM simulation code:
**


*Class-Based Approach:*

> The code defines an ATM class to encapsulate account details and operations.

> Encapsulation of Account Details:

> Each account has attributes: *account_number, pin, balance, and transaction_history.*

> Every deposit, withdrawal, and PIN change is recorded with a timestamp.


*Security Measures:*

PIN verification allows only 3 attempts before locking the account.

User-Friendly ATM Menu:

Provides options to access various banking operations.
Error Handling:

Prevents overdrawing from the account.
Ensures deposits are positive values.
Ensures only valid menu choices are accepted.
Dictionary-Based Account Management:

A dictionary (accounts) stores multiple ATM objects for different account holders.
Simulation of an ATM Machine:

Uses a loop to interact with the user until they exit.



         
