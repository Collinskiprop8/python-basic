import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened db succesfully")

conn.execute("INSERT INTO STUDENTS(PRICE,NAME,YEAR,BRAND) VALUES (1,'Collins',18,'eMobilis')")
