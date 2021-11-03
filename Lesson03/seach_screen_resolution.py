import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

screen_resolution = input("Nhập screen resolution: ")

mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE screen_resolution LIKE" + "'%" + screen_resolution + "%';")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)