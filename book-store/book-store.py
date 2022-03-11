import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="kjuhstlncp",
  database="book-store"
)

mycursor = mydb.cursor()

# Register
def checkUserName(userName):
  mycursor.execute("SELECT COUNT(*) FROM `book-store`.user WHERE name = '" + userName + "';") #check user name
  check_userName = mycursor.fetchall()
  if check_userName == 1:
    return False
  else:
    return True

def checkPhone(phone):    
  mycursor.execute("SELECT COUNT(*) FROM `book-store`.user WHERE name = '" + phone + "';") #check phone
  check_phone = mycursor.fetchall()
  if check_phone == 1:
    return False
  else:
    return True


def register(userName, phone, password, email):
  sql = "INSERT INTO `book-store`.user (name, phone, password, email) VALUE (%s, %s, %s, %s)"
  value = (userName, phone, password, email)
  mycursor.execute(sql, value)
  mydb.commit()


# Login
def login(userName, password):
  try:
    mycursor.execute("SELECT `password` FROM `book-store`.user WHERE  `name` = '" + userName + "';")
    x = mycursor.fetchall()
    check_password = x[0][0]
    if password == check_password:
      print("Đăng nhập thành công!")
    else:
      print("Sai mật khẩu!")
  except:
    print("Tài khoản không tồn tại!")

# Home page

def type():
  mycursor.execute("SELECT * FROM `book-store`.type")
  myresult = mycursor.fetchall()
  mylist = []
  for x in myresult:
    mylist.append(x[1])
  print(mylist)


def tab_type(type_id):        # default display
  mycursor.execute("SELECT title, price, main_image FROM `book-store`.books WHERE type_id = '" + type_id + "';")
  myresult = mycursor.fetchall()
  for x in myresult:
    title = x[0]
    price = x[1]
    main_image = x[2]
    print("title: %s, price: %s, main_image: %s" % (title, price, main_image))

def price_ASC(type_id):     # sort by price ascending
  mycursor.execute("SELECT title, price, main_image FROM `book-store`.books WHERE type_id = '" + type_id + "' ORDER BY price ASC;")
  myresult = mycursor.fetchall()
  for x in myresult:
    title = x[0]
    price = x[1]
    main_image = x[2]
    print("title: %s, price: %s, main_image: %s" % (title, price, main_image))

def price_DESC(type_id):    # sort by price descending
  mycursor.execute("SELECT title, price, main_image FROM `book-store`.books WHERE type_id = '" + type_id + "' ORDER BY price DESC;")
  myresult = mycursor.fetchall()
  for x in myresult:
    title = x[0]
    price = x[1]
    main_image = x[2]
    print("title: %s, price: %s, main_image: %s" % (title, price, main_image))

# User page 1
def info(user_id):
  mycursor.execute("SELECT phone, email FROM `book-store`.user WHERE user_id = '" + user_id + "';")
  myresult = mycursor.fetchall()
  for x in myresult:
    phone = x[0]
    email = x[1]
    print("phone: %s, email: %s" % (phone, email))

def change_password(user_id, new_password):
  try:
    mycursor.execute("UPDATE `book-store`.user SET `password` = '" + new_password + "' WHERE user_id = '" + user_id + "';")
    mydb.commit()
    print("Đổi mật khẩu thành công!")
  except:
    print("Đổi mật khẩu thất bại!")

# User page 2
def posted_books(user_id):
  mycursor.execute("SELECT title, published_year, price, upload_times, main_image FROM `book-store`.books WHERE user_id = '" + user_id + "';")
  myresult = mycursor.fetchall()
  for x in myresult:
    title = x[0]
    published_year = x[1]
    price = x[2]
    upload_times = x[3]
    main_image = x[4]
    print("title: %s, published_year: %s, price: %s, upload_times: %s, main_image: %s" % (title, published_year, price, upload_times, main_image))

def edit_book(book_id, price, published_year, main_image, descripton_image):
  sql = "UPDATE `book-store`.books SET "
  if price != None:
    sql += "price = '" + price + "', "
  if published_year != None:
    sql += "published_year = '" + published_year + "', "
  if main_image != None:
    sql += "main_image = '" + main_image + "', "
  if descripton_image != None:
    sql += "descripton_image = '" + descripton_image + "', "
  sql += "last_update = CURRENT_TIMESTAMP WHERE book_id = '" + book_id + "';"
  mycursor.execute(sql)
  mydb.commit()

# User page 3
def like_book(user_id, book_id):
  mycursor.execute("SELECT COUNT(*) FROM `book-store`.user_liked_book WHERE user_id = '" + user_id + "' AND book_id = '" + book_id + "';")
  check_like = mycursor.fetchall()
  if check_like[0][0] == 0:
    sql = "INSERT INTO `book-store`.user_liked_book (user_id, book_id) VALUES (%s, %s)"
    values = (user_id, book_id)
    mycursor.execute(sql, values)
    mydb.commit()
  else:
    mycursor.execute("UPDATE `book-store`.user_liked_book SET liked = '1' WHERE user_id = '" + user_id +"' AND book_id = '" + book_id + "';")
    mydb.commit()


def unlike_book(user_id, book_id):
  sql = "UPDATE `book-store`.user_liked_book SET liked = '0' WHERE user_id = '" + user_id +"' AND book_id = '" + book_id + "';"
  mycursor.execute(sql)
  mydb.commit()

def user_like_book(user_id):
  mycursor.execute("SELECT title, published_year, main_image, price, phone FROM `book-store`.user_liked_book LEFT JOIN `book-store`.books ON user_liked_book.book_id = books.book_id JOIN `book-store`.user ON books.user_id = user.user_id WHERE user_liked_book.user_id = '" + user_id + "' AND liked = '1';")
  myresult = mycursor.fetchall()
  for x in myresult:
    title = x[0]
    published_year = x[1]
    main_image = x[2]
    price = x[3]
    phone = x[4]
    print("title: %s, published_year: %s, main_image: %s, price: %s, phone: %s" % (title, published_year, main_image, price, phone))

#Detail page
def detail_book(id_book):
  sql = "SELECT main_image, description_image, title, published_year, description, author, price, type, category, contact_info"