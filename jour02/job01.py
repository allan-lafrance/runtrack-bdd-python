import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="LaPlateforme"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM etudiants")

for x in mycursor:
  print(x)