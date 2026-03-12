from sqlite3 import connect

c = connect('shopping.db')
cursor = c.cursor()

def AddProduct(name, category_id, price, image):
    cursor.execute("insert into Product(name, category_id, price, image) values(?, ?, ?, ?)", (name, category_id, price, image))
    c.commit()
    return "bajarildi"

def ReadProduct(category_id):
    cursor.execute("select * from product where category_id=?", (category_id,))
    malumot = cursor.fetchall()
    return malumot


def AddCategory(name):
    cursor.execute("insert into Category(name) values(?);", (name,))
    c.commit()
    return 'bajarildi'

def ReadCategory():
    cursor.execute("select name from category;")
    malumotlar = cursor.fetchall()
    return malumotlar




def AddUsers(user_id, fullname):
    cursor.execute("insert into users(user_id, full_name) values(?, ?)", (user_id, fullname))
    c.commit()
    return "bajarildi"

def ReadUser(user_id):
    cursor.execute("select * from users where user_id = ?", (user_id, ))
    malumot = cursor.fetchone()
    return malumot

def AdsUsers():
    cursor.execute("select user_id from users")
    malumotlar = cursor.fetchall()
    return malumotlar


# cursor = c.cursor()
# cursor.execute("""
#                create table Users(
#                    ID INTEGER PRIMARY KEY NOT NULL,
#                    USER_ID INTEGER UNIQUE NOT NULL,
#                    FULL_NAME TEXT NOT NULL
#                );               
#                """)

# cursor.execute("""
#                create table Category(
#                     ID INTEGER PRIMARY KEY NOT NULL,
#                     NAME TEXT NOT NULL
#                );               
#                """)

# cursor.execute("""
#                create table Product(
#                     ID INTEGER PRIMARY KEY NOT NULL,
#                     category_id int not null,
#                     name text not null,
#                     price real not null,
#                     image text not null
#                );               
#                """)

# c.commit()
# print("bajarildi")