import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

def infomation_oder():
    mycursor.execute("SELECT orderDate, requiredDate, `Status`, (quantityOrdered * priceEach) AS price FROM product_orders_plusplus.orderdetails JOIN product_orders_plusplus.orders ON orderdetails.orderNumber = orders.orderNumber WHERE orderDate LIKE '2003-03-%';")
    myresult = mycursor.fetchall()

    for x in myresult:
        orderDate = x[0]
        requiredDate = x[1]
        status = x[2]
        price = x[3]
        print("orderDate: %s, requiredDate: %s, status: %s, price: %s" % (orderDate, requiredDate, status, price))


def products_cancelled():
    mycursor.execute("SELECT productName FROM product_orders_plusplus.orderdetails JOIN product_orders_plusplus.orders ON orderdetails.orderNumber = orders.orderNumber JOIN product_orders_plusplus.products ON orderdetails.productCode = products.productCode WHERE `status` = 'Cancelled';")
    myresult = mycursor.fetchall()
    
    print(myresult)

print(products_cancelled())