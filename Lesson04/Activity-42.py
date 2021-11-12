import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

def getCounterByMaker():
    mycursor.execute("SELECT maker, COUNT(*) as 'quantity' FROM store_cms_plusplus.laptop GROUP BY maker ORDER BY quantity DESC;")

    myresult = mycursor.fetchall()

    return myresult

    
print(getCounterByMaker())