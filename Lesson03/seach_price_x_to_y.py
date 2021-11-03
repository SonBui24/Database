import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

lowest_price = input("Giá từ: ")
highest_price = input("Đến: ")

mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE price BETWEEN " + lowest_price + " AND " + highest_price + ";")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)