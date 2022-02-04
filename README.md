# ATM-Interface
The program works on the basis of there being an already exiting database with the bank which contains usernames and linked balances
and pins in some cases. 
Methods:
1) ATM: This method accepts a list of strings which contains all the data. It contains the main logic of the program which includes verifying a usernames existence in the database, and the 
main menu seen by the user.
2) User: This method checks if the entered username exists in the database.
3) Card: This method authenticates the pin with the username, and allows the user to create a new pin if he/she hasn't set a pin already.
4) Acccount: This method allows the user to check his/her account balance and carry out transactions like deposits and withdrawals. This method also allows the user to change his/her existing 
pin
