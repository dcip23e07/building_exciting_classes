## Banking System App (Introduction)
  In a bank we have Employees and Employers(Managers), Some of which can have access
to the bank Software while some wont have.
  The bank will also have customers such that they have accounts with the bank.
Having accounts with the bank will mean that every transaction will be recorded.

## classes That can be required (You can do things your way or rename them):
### -- Bank Manager ( can log into the bank system and performs all actions on bank system)
    - attributes: 
      firstname
      lastname
      date of birth
      age # should be calculated from date of birth and should not be settable
      date of employment (cannot be changed)
      address
      salary
      job
      department
      sex
      status: Active, Deactivated, Suspended
    - can create a new bank Profile for customer
    - can upate a bank Profile for customer
    - can create a new account for customer
    - can withdraw from customer account
    - can deposit money to customer account
    - can deacivate a bank teller
    - can suspend a bank teller

 
 ### -- Bank Teller (can log into the bank system and perform limited actions on bank system)
    - attributes: 
      firstname
      lastname
      date of birth 
      age # should be calculated from date of birth and should not be settable
      date of employment (cannot be changed)
      address
      salary
      job
      department
      status: Active, Deactivated, Suspended
    - can create a new bank Profile for customer
    - can upate a bank Profile for customer
    - can create a new account for customer
    - can withdraw from customer account
    - can deposit money to customer account

###  -- Other Bank Employee (cannot log into the bank system and cannot perform any actions on bank system)
    - attributes: 
      firstname
      lastname
      date of birth
      age # should be calculated from date of birth and should not be settable
      date of employment (cannot be changed)
      address
      salary
      job
      department
      sex
      status: Active, Deactivated, Suspended
    - cannot perform any operation


### -- Bank Customer
    - attributes: 
      firstname
      lastname
      date of birth
      age # should be calculated from date of birth and should not be settable
      date registered (cannot be changed)
      address
      security number (cannot be changed)


### -- Bank Account
    - attributes: 
      amount
      account_number
      date opened (cannot be changed)
      owner_name
      opened_by # employee who opened it
      currency
      type SAVINGS, CURRENT
      status: Active, Deactivated, Suspended
    - can show current balance
    - can reduce amount (withdrawal)
    - can increase amount (deposit)
    - can be closed


### -- Transaction Record 
    - attributes: 
      creator_name (employee who created the transaction) (cannot be changed)
      creation_date (cannot be changed)
      creation_time (cannot be changed)
      transaction_type (Deposit or Withdrawal) (cannot be changed)
      amount (cannot be changed)
      customer_name (cannot be changed)
    - can search data by amount, customer_name or creator name
    - can show transaction of the last n days.

### Files Included:
- `data/accounts.json`  holds information about customer accounts.
  Use this to read and write information about customer accounts

- `data/customers.json` holds information about customer's bank profile.
  Use this to read and write information about customer's bank profile

- `data/transactions.json` holds information about bank transactions made(withdrawal, deposit).
  Use this to read and write information about transaction records

- `data/staffs.json` holds information about staffs working in the bank.
  Use this to read and write information about bank staffs

- `main.py` which is the script file thatwill run all your functionality

- `actions.py` helps in deciding which action is chosen
and what should be done

-`json_functionalities.py` contain methods for reading , writing and adding to json files.

- `solution.py` can hold your solution to the class

-- feel free to edit all files as you want.

### Bank system (what it should do):
1. should greet the user with a login request
2. if the user is not a bank manager or bank teller then, login should not be possible
3. if the user details is wrong, the user should get a prompt on whats wrong.
 - if the password is wrong, then the user should be told.
 - if the username is not found then the user should be prompted aswell.
4. on successful logged in, allow the employee perform any of the following.
  - create a new bank profile for customer
  - update bank profile for customer
  - create a new account for customer (only if they have a bank profile)
  (if they do not have a bank profile, create one before creating an account.
  - withdraw from account.
  - deposit to account

Build a dynamic CLI App that should allow you run the Bank System Above
  - it should have an argument called system  (this is not optional), allowed options is (argparse, sys_argv)
    -- if the user picks argparse, your cli app should run using argparse library
    -- if the user picks sys_argv, your cli app should run using sys.argv
  - it should take in a login argument (this is not optional) called mode
  - login should have options or flags for username and password
  - if username and password is supplied when runng the app, it should log the user in.
  - if not it should ask for username and password, then login the user.
  
  Other things should follow according to the bank system.