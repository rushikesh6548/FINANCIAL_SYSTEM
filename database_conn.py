import pyodbc

import datetime 



class Database:
    def __init__(self):
        ## should be connecting to the database ! 
        try : 
            conn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=192.168.10.12,1433;"  # or "DESKTOP-GQFUIC4"
            "Database=BankApp;"
            "Trusted_Connection=yes;"
            )
            self.conn = conn
            self.cursor = conn.cursor()
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            self.conn = None
            self.cursor = None


    def create_user(self,user ):
        ## WE will be creating the user inside our database! 
        query = 'INSERT INTO users (fname , lname , pwd,BALANCE) VALUES (?,?,?,0)'
        try:    
            ## check if user already exists or not ! 
            user_exists = self.conn.execute("SELECT 1 from users where fname = ? and lname = ?", (user.fname,user.lname)).fetchall()
            
            if len(user_exists) == 0 :
                
                self.cursor.execute(query, (user.fname,user.lname,user.pwd))
                self.cursor.commit()
                
                return 1

            else : 
                print("USERNAME ALREADY TAKEN ! KINDLY ENTER A NEW USERNAME! WE WILL START THE USER CREATION PROCESS AGAIN ! ")
                
                return 0

        except pyodbc.Error as e:
            print(e)


    def check_correct_user(self,user  ):
        try:
            user_correct= self.conn.execute("SELECT 1 from users where fname = ? and lname = ? and pwd = ?",(user.fname , user.lname,user.pwd )).fetchall()
            print(user_correct)
            if len(user_correct) == 0 :
                return 0 
            else:
                return 1 

        except pyodbc.Error as e:
            print(e)

    def get_user_balance(self,user):
        try:
            balance = self.conn.execute("SELECT BALANCE FROM USERS WHERE FNAME =  ? and LNAME = ? ", (user.fname, user.lname)).fetchone()
            return balance
        
        except pyodbc.Error as e:
            print(e)    
        
    def depo_money_db(self,amt,user):
        try:
            self.conn.execute("UPDATE USERS SET BALANCE = BALANCE + ? WHERE fname = ? and lname = ? ", (amt,user.fname , user.lname))
            self.conn.commit()
            
            return 1 
        except pyodbc.Error as e:
            print(e)
            return 0
        

    def get_user_all_details(self,user):
        try:
            all_details = self.conn.execute("SELECT * FROM Users where fname = ? and lname = ?",(user.fname , user.lname)).fetchall()
            return all_details
        except pyodbc.Error as e:
            print(e)


    def update_user_details(self, user, age, income,obligation):
        try:
            self.conn.execute("UPDATE Users SET age = ?, income = ? , obligations = ? WHERE fname = ? and lname = ?", 
                              (age, income,obligation , user.fname, user.lname))
            self.conn.commit()
            print("User details updated successfully.")
        except pyodbc.Error as e:
            print(f"Error updating user details: {e}")