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

  list = []

  for x in myresult:
    list.append(x)

  return list

def display():
  list = getCounterByMaker()
  for x in list:
    maker = x[0]
    quantity = x[1]
    print(f"Maker: {maker}, Quantity: {quantity}")

class Counter:
  def __init__(self, maker, quantity):
    self.maker = maker
    self.quantity = quantity
    
display()