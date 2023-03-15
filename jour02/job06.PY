import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="LaPlateforme"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT SUM(capacite) FROM salles")

result = mycursor.fetchone()[0]
print("La somme des capacités des salles est de", result)