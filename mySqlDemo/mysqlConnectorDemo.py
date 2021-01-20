import traceback

import mysql.connector


def create():
    try:
        mydb = mysql.connector.connect(
            host="localhost",  # 数据库主机地址
            user="root",  # 数据库用户名
            passwd="root",  # 数据库密码
            database="demo"
        )
        mycursor = mydb.cursor()
        mycursor.execute('''
        create table example (
        	id varchar(64) not null primary key,
        	emp_key varchar(64) null,
        	emp_val varchar(64) null
        )
        ''')
        mycursor.execute("SHOW TABLES")
        for x in mycursor:
            print(x)
    except:
        print(traceback.format_exc())


def selectAll():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="demo"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM example")
        # fetchall() 获取所有记录
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
    except:
        print(traceback.format_exc())


def insert(id, emp_key, emp_val):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="demo"
        )
        mycursor = mydb.cursor()
        sql = "insert into example value('%s', '%s', '%s')" % (id, emp_key, emp_val)
        mycursor.execute(sql)
        mydb.commit()
    except:
        print(traceback.format_exc())


def update(emp_key, emp_val):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="demo"
        )
        mycursor = mydb.cursor()
        sql = "update example set emp_val = '%s' where emp_key = '%s'" % (emp_val, emp_key)
        mycursor.execute(sql)
        mydb.commit()
    except:
        print(traceback.format_exc())


def delete(id):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="demo"
        )
        mycursor = mydb.cursor()
        sql = "delete from example where id = '%s'" % id
        mycursor.execute(sql)
        mydb.commit()
    except:
        print(traceback.format_exc())


if __name__ == '__main__':
    create()
    insert('1', '11', '111')
    update('11', '1')
    delete('1')
    selectAll()
