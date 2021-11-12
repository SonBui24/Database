import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

def sold_update(id, sold_update):
    sql = "UPDATE store_cms_plusplus.laptop SET sold = " + sold_update + ", last_updated_timestamp = CURRENT_TIMESTAMP WHERE id = " + id + ";"
    mycursor.execute(sql)

    mydb.commit()

sold_update("8", "50")