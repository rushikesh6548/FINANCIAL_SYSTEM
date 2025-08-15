#### 

## functions of my app:


## 1 . User to create an account ! 
## 2 . Users to get a loan! 
## 3 . Users can see theri amoritization schedule 
## 4.  Users can prepayment and then see their amorization schedule!

## this py file should be calling like the main menu thing ! 
import textwrap
from users import User
class Menu:
    def __init__(self):
        self.start()

    def start(self):
        x= int(input(("HELLO USER ! WELCOME ! \n"
              "WHAT DO YOU WANT TO DO ? \n"
              "TYPE 1 TO CREATE A NEW ACCOUNT!\n")))
        
        if x == 1 :
            print('Creation of new acc started')
            self.create_new_user()


    def create_new_user(self):
        print("NEW USER CREATION PORTAL!\n")
        first_name = str(input("KINDLY ENTER YOUR FIRST NAME :\n"))
        last_name = str(input("KINDLY ENTER YOUR LAST NAME :\n"))
        password = str(input("PLEASE ENTER A PASSWORD TO SET"))

        user= User(first_name=first_name,last_name=last_name,password=password)
        ## storting this user inside our database ! 
        
        ## creation of a user object :









t = Menu()    


