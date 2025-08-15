import pyodbc

def get_connection():
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=192.168.10.12,1433;"  # or "DESKTOP-GQFUIC4"
        "Database=BankApp;"
        "Trusted_Connection=yes;"
    )
    return conn


conn = get_connection()
cursor = conn.cursor()
# cursor.execute("SELECT name FROM sys.databases;")
# for row in cursor.fetchall():
#     print(row[0])


res = cursor.execute('select * from users ').fetchall()
print(res)
