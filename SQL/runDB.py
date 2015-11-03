import sqlite3

conn = sqlite3.connect('test.db')
 
c = conn.cursor()

# c.execute("CREATE TABLE plot (ID int, unix real, datestamp text, keyword text, value real)")


c.execute("INSERT INTO plot VALUES (3, 13659952261.123, '2013-05-14 10:11:04', 'Python', 12.00)")
c.execute("INSERT INTO plot VALUES (3, 13659952261.123, '2013-05-14 10:11:04', 'Python', 12.00)")
c.execute("INSERT INTO plot VALUES (3, 13659952261.123, '2013-05-14 10:11:04', 'Python', 12.00)")
c.execute("INSERT INTO plot VALUES (3, 13659952261.123, '2013-05-14 10:11:04', 'Python', 12.00)")
c.execute("INSERT INTO plot VALUES (3, 13659952261.123, '2013-05-14 10:11:04', 'Python', 12.00)")
conn.commit()
conn.close()


