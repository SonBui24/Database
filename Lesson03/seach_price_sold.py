import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE price > 10000000 AND sold >= 30;")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)