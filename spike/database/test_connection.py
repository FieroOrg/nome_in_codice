import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="nic",
  password="nic",
  database="nome-in-codice"
)

print(mydb)