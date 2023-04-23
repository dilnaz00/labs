   # id SERIAL PRIMARY KEY,
import psycopg2

conn=psycopg2.connect(database="postgres",
                      host="localhost",
                      user="postgres",
                      password="82342121",
                      port="5432"
                    )
cursor=conn.cursor()
print("end")
# создание таблиц
# cursor.execute("CREATE TABLE customers (id INT  PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# ввод имени пользователя, телефона с консоли
# cursor.execute("INSERT INTO  phonebook (id , name, phone ) VALUES (3, 'Ainara' , '87779990027' )")

# обновление таблиц
#cursor.execute("UPDATE  phonebook SET phone='87788456124' WHERE id=3")

# удаление колонки
# cursor.execute("DELETE FROM  phonebook   WHERE name='Dulat'")

# Запрос данных из таблиц
# cursor.execute("SELECT phone from phonebook WHERE id='1' ")

# загрузка данных из csv-файла
# cursor.execute("SELECT *  from phonebook")
# with open('data.csv', 'r') as f:
#     cursor.copy_from(f, 'phonebook', sep=',')
#     cursor.close()
#     conn.commit()
# f.close()
# conn.commit()