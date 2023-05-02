import psycopg2

conn=psycopg2.connect(database="postgres",
                      host="localhost",
                      user="postgres",
                      password="82342121",
                      port="5432"
                    )
cursor=conn.cursor()
t=input()
# cursor.execute("delete from phonebook where id=13")
def inserting(t):
  phone=input()
  cursor.execute("Select * from phonebook ")
  res=cursor.fetchall()
  i=0
  while i!=len(res):
    global exist
    if t==res[i][1].strip():
      exist =False
      cursor.execute(f"Update phonebook  set phone ='{phone}' where name='{t}' ")
      break
      i+=1
    else:
      i+=1
      exist = True
      
  if exist==True: 
      cursor.execute(f"Insert INTO phonebook (id,name,phone) VALUES( '{len(res)+3 }','{t}', '{phone}'  )")
  print('end')
inserting(t)
conn.commit()