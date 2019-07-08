import pymysql as sql


def connect():
    connection = sql.connect(host='localhost',
                                 user='alex',
                                 password='1234',
                                 db='RIP_lab5_db',
                                 charset='utf8mb4'
                             )

    return connection


cnct = connect()
####
try:
    with cnct.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `bdApp_bottle` (`name`, `liter`) VALUES (%s, %s)"
        cursor.execute(sql, ('vodka', 1))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    cnct.commit()

    with cnct.cursor() as cursor:
        # Read a single record
        sql = "SELECT `name`, `liter` FROM `bdApp_bottle` WHERE `name`=%s"
        cursor.execute(sql, 'vodka')
        result = cursor.fetchone()
        print(result)
finally:
    cnct.close()
####
