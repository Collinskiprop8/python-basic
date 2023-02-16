import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened db succesfully")
conn.execute("CREATE TABLE CARS"""
             "(PRICE INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "YEAR OF PRODUCTION INT NOT NULL,"
             "BRAND TEXT NOT NULL) ")

print("Table created successfully")
conn.close()
