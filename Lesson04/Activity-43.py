import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

def getStatisticByMaker():
    mycursor.execute("SELECT maker, SUM(sold) as 'sold', SUM(sold * price) as 'totalMoney' FROM store_cms_plusplus.laptop GROUP BY maker;")

    myresult = mycursor.fetchall()

    return myresult

print(getStatisticByMaker())