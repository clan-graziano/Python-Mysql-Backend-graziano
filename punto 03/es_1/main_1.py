'Creazione di un database MySQL con Python'

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="password123"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)