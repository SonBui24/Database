import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

maker = input("Nhập maker: ")

mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE maker LIKE" + "'%" + maker + "%';")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)