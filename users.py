## creating user class ! 



import datetime



class User:
    def __init__(self, first_name , last_name,password):
        self.fname  = first_name
        self.lname = last_name
        self.pwd = password

    def __str__(self):
        return f'USERNAME : {self.fname + self.lname}'