import mysql.connector
from getpass import getpass

try:
    mydatabase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = getpass("Enter your password: ")
    )
    mycursor = mydatabase.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database created successfully")
except mysql.connector.Error as err:
    print(f"Failed to connect: {err}")