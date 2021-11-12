import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

"""
def seach_maker():
    maker = input("Nhập maker: ")

    mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE maker LIKE" + "'%" + maker + "%';")

    myresult = mycursor.fetchall()

    for x in myresult:
        id = x[0]
        name = x[1]
        maker = x[3]
        type = x[4]
        ram = x[5]
        cpu = x[6]
        ssd = x[7]
        hdd = x[8]
        price = x[9]
        card = x[10]
        screen_resolution = x[11]
        screen_size = x[12]
        sold = x[13]
        print("id: %s, name: %s, maker: %s, type: %s, ram: %s, cpu: %s, ssd: %s, hdd: %s, price: %s, card: %s, screen_resolution: %s, screen_size: %s, sold: %s" % \
            (id, name, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold))

def seach_type():
    type = input("Nhập type: ")

    mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE type LIKE" + "'%" + type + "%';")

    myresult = mycursor.fetchall()

    for x in myresult:
        id = x[0]
        name = x[1]
        maker = x[3]
        type = x[4]
        ram = x[5]
        cpu = x[6]
        ssd = x[7]
        hdd = x[8]
        price = x[9]
        card = x[10]
        screen_resolution = x[11]
        screen_size = x[12]
        sold = x[13]
        print("id: %s, name: %s, maker: %s, type: %s, ram: %s, cpu: %s, ssd: %s, hdd: %s, price: %s, card: %s, screen_resolution: %s, screen_size: %s, sold: %s" % \
            (id, name, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold))

def seach_screen_resolution():
    screen_resolution = input("Nhập screen resolustion: ")

    mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE screen_resolution LIKE" + "'%" + screen_resolution + "%';")

    myresult = mycursor.fetchall()

    for x in myresult:
        id = x[0]
        name = x[1]
        maker = x[3]
        type = x[4]
        ram = x[5]
        cpu = x[6]
        ssd = x[7]
        hdd = x[8]
        price = x[9]
        card = x[10]
        screen_resolution = x[11]
        screen_size = x[12]
        sold = x[13]
        print("id: %s, name: %s, maker: %s, type: %s, ram: %s, cpu: %s, ssd: %s, hdd: %s, price: %s, card: %s, screen_resolution: %s, screen_size: %s, sold: %s" % \
            (id, name, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold))

def seach_price_and_sold():
    mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE price > 10000000 AND sold >= 30;")

    myresult = mycursor.fetchall()

    for x in myresult:
        id = x[0]
        name = x[1]
        maker = x[3]
        type = x[4]
        ram = x[5]
        cpu = x[6]
        ssd = x[7]
        hdd = x[8]
        price = x[9]
        card = x[10]
        screen_resolution = x[11]
        screen_size = x[12]
        sold = x[13]
        print("id: %s, name: %s, maker: %s, type: %s, ram: %s, cpu: %s, ssd: %s, hdd: %s, price: %s, card: %s, screen_resolution: %s, screen_size: %s, sold: %s" % \
            (id, name, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold))

def seach_price_x_to_y():
    lowest_price = input("Giá từ: ")
    highest_price = input("Đến: ")

    mycursor.execute("SELECT * FROM store_cms_plusplus.laptop WHERE price BETWEEN " + lowest_price + " AND " + highest_price + ";")

    myresult = mycursor.fetchall()

    for x in myresult:
        id = x[0]
        name = x[1]
        maker = x[3]
        type = x[4]
        ram = x[5]
        cpu = x[6]
        ssd = x[7]
        hdd = x[8]
        price = x[9]
        card = x[10]
        screen_resolution = x[11]
        screen_size = x[12]
        sold = x[13]
        print("id: %s, name: %s, maker: %s, type: %s, ram: %s, cpu: %s, ssd: %s, hdd: %s, price: %s, card: %s, screen_resolution: %s, screen_size: %s, sold: %s" % \
            (id, name, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold))
"""

def seach_laptop(maker, type, screen_resolution, fromPrice, toPrice, sold):
    sql = "SELECT * FROM store_cms_plusplus.laptop WHERE true"
    if maker != None:
        sql += " AND maker LIKE '%" + maker + "%'"
    if type != None:
        sql += " AND type LIKE '%" + type + "%'"
    if screen_resolution != None:
        sql += " AND screen_resolution LIKE '%" + screen_resolution + "%'"
    if fromPrice != None:
        sql += " AND price >= " + fromPrice
    if toPrice != None:
        sql += " AND price <= " + toPrice
    if sold != None:
        sql += " AND sold LIKE '%" + sold + "%'"

    print(sql)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        id = x[0]
        name = x[1]
        maker = x[3]
        type = x[4]
        ram = x[5]
        cpu = x[6]
        ssd = x[7]
        hdd = x[8]
        price = x[9]
        card = x[10]
        screen_resolution = x[11]
        screen_size = x[12]
        sold = x[13]
        print("id: %s, name: %s, maker: %s, type: %s, ram: %s, cpu: %s, ssd: %s, hdd: %s, price: %s, card: %s, screen_resolution: %s, screen_size: %s, sold: %s" %
            (id, name, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold))
seach_laptop(None, None, None, None, None, None)