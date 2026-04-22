try:
    import MySQLdb as mysql
except ImportError:
    import pymysql as mysql

db = mysql.connect(host="localhost", user="root", password="Yash@123")
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS gym_db;")
db.commit()
db.close()
print("Database created successfully")
