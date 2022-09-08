import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mynewpassword",
  database="mydbs"
)

print(mydb) 

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydbs")

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")