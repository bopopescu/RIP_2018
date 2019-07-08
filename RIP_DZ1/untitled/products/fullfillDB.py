import MySQLdb as sql


def connect():
    return sql.Connect(
        host='localhost',
        port=3306,
        user='alex',
        passwd='1234',
        db='my_db',
        charset='utf8mb4'
    )


connection = connect()
curs = connection.cursor()
i = 100
for i in range(100,101):
    str1 = 'Филадельфия'
    str2 = 'uploads/products/1.jpg'
    curs.execute("""INSERT INTO products_product (id,name,picture) values (%s,%s,%s)""", (i, str1, str2))
    i += 1

connection.commit()
connection.close()

