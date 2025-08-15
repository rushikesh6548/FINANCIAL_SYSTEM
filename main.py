#### 

## functions of my app:


## 1 . User to create an account ! 
## 2 . Users to get a loan! 
## 3 . Users can see theri amoritization schedule 
## 4.  Users can prepayment and then see their amorization schedule!

## this py file should be calling like the main menu thing ! 
import textwrap
from users import User
from database_conn import Database

class Menu:
    def __init__(self):
        self.db = Database()
        self.start()

    def start(self):
        x= int(input(("HELLO USER ! WELCOME ! \n"
              "WHAT DO YOU WANT TO DO ? \n"
              "TYPE 1 TO CREATE A NEW ACCOUNT!\n"
              "TYPE 2 TO LOGIN IN CASE OF AN EXISTING USER\n")))
        
        if x == 1 :
            print('Creation of new acc started')
            self.create_new_user()
        elif x == 2 :
            self.login()

    def after_login(self):
        ## 
        user_inp = str(input("WHAT BANKING FEATURES DO YOU WANT TO AVAIL?\n"
                             "TYPE 1 TO CHECK YOUR BALANCE"))
        
        

    


    def create_new_user(self):
        print("NEW USER CREATION PORTAL!\n")
        first_name = str(input("KINDLY ENTER YOUR FIRST NAME :\n")).strip()
        last_name = str(input("KINDLY ENTER YOUR LAST NAME :\n")).strip()
        password = str(input("PLEASE ENTER A PASSWORD TO SET\n")).strip()

        user= User(first_name=first_name,last_name=last_name,password=password)
        result= self.db.create_user(user = user)
        print(result)
        if result == 1:
            print("USER CREATED SUCCESSFULLY! NOW YOU WILL BE REDIRECTED TO LOGIN ! ")
            self.start()
        else : 
            self.create_new_user()

    def login(self):
        ### LOGIN WILL FIRST CHECK IF USER IS ENTERING USERNAME AND PASSWORD CORRECT ! 
        fname = str(input("ENTER YOUR FIRST NAME \n "))
        lname  = str(input("ENTER YOUR LAST NAME \n "))

        password = str(input("ENTER YOUR PASSWORD"))

        user =  User(first_name=fname,last_name=lname,password=password)
        result = self.db.check_correct_user(user=user)
        if result == 1 :
            print("WELCOME HUMAN ! LOGGED IN SUCCESSFULLY ! ")
            self.after_login()
        else :
            user_response = str(input("USERNAME OR PASSWORD DOES NOT MATCH ! SELECT 1 TO TRY AND LOGIN AGAIN OR SELECT 2 TO CREATE NEW ACCOUNT"))
            if user_response == 1 :
                self.after_login()
            else :
                self.create_new_user()







t = Menu()    


