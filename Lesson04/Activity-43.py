import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

class Statistic:
    def __init__(self, maker, sold, totalMoney):
        self.maker = maker
        self.sold = sold
        self.totalMoney = totalMoney

def getStatisticByMaker():
    mycursor.execute("SELECT maker, SUM(sold) as 'sold', SUM(sold * price) as 'totalMoney' FROM store_cms_plusplus.laptop GROUP BY maker;")

    myresult = mycursor.fetchall()
    list = []
    
    for x in myresult:
        list.append(x)
    
    return list

def display():
    list = getStatisticByMaker()

    for x in list:
        maker = x[0]
        sold = x[1]
        totalMoney = x[2]
        print(f"Maker: {maker}, Sold: {sold}, TotalMoney: {totalMoney}")

display()
