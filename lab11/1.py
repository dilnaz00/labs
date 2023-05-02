import psycopg2

conn=psycopg2.connect(database="postgres",
                      host="localhost",
                      user="postgres",
                      password="82342121",
                      port="5432"
                    )
cursor=conn.cursor()
t=input()
def pattern(t):
 cursor.execute(f"SELECT * FROM phonebook WHERE name LIKE '{t.capitalize()}%' ")
 for row in cursor:
   print(row)
pattern(t)


conn.commit()