import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Password_1234',

)

# prepare a cursor object
cursorObject = dataBase.cursor()

#create Databse
cursorObject.execute("CREATE DATABASE CRM")

print("All Done!")