import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1",
                             user="root",
                             password="",
                             database="addressbook")

try:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()