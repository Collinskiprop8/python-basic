import _sqlite3
conn=_sqlite3.connect('emobilis.db')
print("opened db succesfully")

conn.execute("INSERT INTO STUDENTS(ID,NAME,AGE,SCHOOL) VALUES (1,'Collins',18,'eMobilis')")
conn.execute("INSERT INTO STUDENTS(ID,NAME,AGE,SCHOOL) VALUES (2,'Metah',17,'MKU')")
conn.execute("INSERT INTO STUDENTS(ID,NAME,AGE,SCHOOL) VALUES (3,'Edwin',27,'eMobilis')")
conn.execute("INSERT INTO STUDENTS(ID,NAME,AGE,SCHOOL) VALUES (5,'George',28,'KCA')")
conn.execute("INSERT INTO STUDENTS(ID,NAME,AGE,SCHOOL) VALUES (6,'Faith',20,'JKUAT')")
conn.execute("INSERT INTO STUDENTS(ID,NAME,AGE,SCHOOL) VALUES (7,'Kerry',19,'eMobilis')")

conn.commit()
print("records added successfull")
conn.close()
