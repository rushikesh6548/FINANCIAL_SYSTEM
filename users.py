## creating user class ! 



import datetime
from database_conn import Database

class User:
    def __init__(self, first_name , last_name,password):
        self.fname  = first_name
        self.lname = last_name
        self.pwd = password
        self.bal = 0 

    def __str__(self):
        return f'USERNAME : {self.fname + self.lname}'