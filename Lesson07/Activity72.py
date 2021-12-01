import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

def infomation_products():
    mycursor.execute("SELECT products.productCode, productName ,SUM(quantityOrdered * priceEach) AS totalPrice FROM product_orders_plusplus.products JOIN product_orders_plusplus.orderdetails ON products.productCode = orderdetails.productCode GROUP BY productCode ORDER BY totalPrice ASC;")

    myresult = mycursor.fetchall()

    for x in myresult:
        productCode = x[0]
        productName = x[1]
        totalPrice = x[2]
        print("productCode: %s, productName: %s, totalPrice: %s" % (productCode, productName, totalPrice))


print(infomation_products())