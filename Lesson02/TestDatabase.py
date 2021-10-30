import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="database_4"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student;")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
