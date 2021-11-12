import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="store_cms_plusplus"
)

mycursor = mydb.cursor()

def insert_laptop(name, url, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold):
    sql = "INSERT INTO store_cms_plusplus.laptop (name, url, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name, url, maker, type, ram, cpu, ssd, hdd, price, card, screen_resolution, screen_size, sold)
    
    mycursor.execute(sql, val)

    mydb.commit()

insert_laptop('Laptop ASUS ROG Zephyrus S GX531GM-ES004T (15.6" FHD/i7-8750H/16GB/512GB SSD/GTX 1060/Win10/2.1 kg)', 
'https://phongvu.vn/may-tinh-xach-tay-laptop-asus-rog-zephyrus-gx531gm-es004t-i7-8750h-s19010009.html', 
'ASUS', 
'ROG', 
'8GB', 
'Intel Core i7', 
'512GB',
'1TB', 
'22000000',
'NVIDIA GeForce GTX 1050 3GB GDDR5',
'1920x1080',
'15.6',
'30')

