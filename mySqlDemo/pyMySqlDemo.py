import traceback

import pymysql


def selectAll():
    try:
        # ip, user, password, database
        db = pymysql.connect("localhost", "root", "root", "demo")
        cursor = db.cursor()
        cursor.execute("select * from example")
        index = cursor.rowcount
        print("影响数 - %s" % index)
        res = cursor.fetchall()
        print("id - emp_key - emp_val")
        for i in range(len(res)):
            print("[%s] %s - %s - %s" % (i + 1, res[i][0], res[i][1], res[i][2]))
    except:
        print(traceback.format_exc())
    finally:
        db.close()


def selectOne():
    try:
        db = pymysql.connect("localhost", "root", "root", "demo")
        cursor = db.cursor()
        cursor.execute("select * from example")
        res = cursor.fetchone()
        print("%s - %s - %s" % (res[0], res[1], res[2]))
    except:
        print(traceback.format_exc())
    finally:
        db.close()


def update(emp_key, emp_val):
    if emp_key.strip() == '' or emp_val.strip() == '':
        print("参数错误")
        return

    try:
        db = pymysql.connect("localhost", "root", "root", "demo")
        cursor = db.cursor()
        sql = "update example set emp_val = '%s' where emp_key = '%s'" % (emp_val, emp_key)
        print("sql = %s" % sql)
        cursor.execute(sql)
        index = cursor.rowcount
        print("影响数 - %s" % index)
        # 提交
        db.commit()
    except:
        # 回滚
        db.rollback()
        print(traceback.format_exc())
    finally:
        db.close()


def delete(emp_key):
    if emp_key.strip() == '':
        print("参数错误")
        return

    try:
        db = pymysql.connect("localhost", "root", "root", "demo")
        cursor = db.cursor()
        sql = "delete from example where emp_key = '%s'" % emp_key
        print("sql = %s" % sql)
        cursor.execute(sql)
        index = cursor.rowcount
        print("影响数 - %s" % index)
        # 提交
        db.commit()
    except:
        # 回滚
        db.rollback()
        print(traceback.format_exc())
    finally:
        db.close()


if __name__ == '__main__':
    selectOne()
    update('1', '111')
    delete('1')
    selectAll()
