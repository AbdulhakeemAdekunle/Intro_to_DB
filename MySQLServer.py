import mysql.connector
from getpass import getpass

try: 
    mydatabase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = getpass("Enter your password: "),
    database = alx
)
    mycursor = mydatabase.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database created successfully")

except mysql.connection.Error as e:
    print(e)

mycursor.close()
mydatabase.close()