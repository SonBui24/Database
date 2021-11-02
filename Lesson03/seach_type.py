import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

type = input("Nhập type: ")

mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE type LIKE" + "'%" + type + "%';")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)