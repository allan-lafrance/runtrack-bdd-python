import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="LaPlateforme"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT nom, capacite FROM salles")
result = mycursor.fetchall()

for x in result:
  print(x)
