import pyodbc

import datetime 



class Database:
    def __init__(self):
        ## should be connecting to the database ! 
        conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=192.168.10.12,1433;"  # or "DESKTOP-GQFUIC4"
        "Database=BankApp;"
        "Trusted_Connection=yes;"
        )

    