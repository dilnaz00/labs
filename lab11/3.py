
data = [(12, 'Aliya', '87023981276'), (13, 'Dan', '87789127359'), (14, 'Val', '87778126349')]

import psycopg2

def check(object):
    list = []
    cnt = -1
    for i in object:
        cnt += 1
        if not i[1].isdigit():
            del object[cnt]
    return object

def insert_list(object):
    connection = None
    try:
        connection = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="82342121",
                                    host="localhost",
                                    port="5432",
                                    database="postgres")

        # Создайте курсор для выполнения операций с базой данных
        cur = connection.cursor()
        cur.execute('call insert_list(%s, %s, %s)', object)
        connection.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if connection is not None:
            connection.close()
            
insert_list(data)