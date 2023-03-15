import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="LaPlateforme"
)

cursor = mydb.cursor()

query = "SELECT SUM(superficie) FROM etage"

cursor.execute(query)

result = cursor.fetchone()[0]
print("La superficie de La Plateforme est de", result, "m2")

mydb.close()