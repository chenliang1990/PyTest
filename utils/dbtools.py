# 导入pymysql:为了连接mysql数据库
import pymysql

def query(sql):
    """
        查询mysql数据库：只能用造select，不能delete update insert
    """
    # 连接数据库 固定的，只需要变参数
    db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    cur = db.cursor()    # 获取游标：查询窗口
    try:
        cur.execute(sql)     # 使用游标来执行sql语句
        res = cur.fetchall() # 获取执行的结果
        db.close() #使用完之后关闭数据库，不能一直连着
        return res
    except Exception as e:
        db.close()
        return "sql语句错误! ",e

# sql = "select * from t_user where id=272"
# r = query(sql)
# print(r)

def commit(sql):
    """
        增加/删除/修改方法：delete update insert不要传select
    """
    db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    # db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="lux")
    cur = db.cursor()    # 获取游标：查询窗口
    try:
        cur.execute(sql)     # 使用游标来执行sql语句
        db.commit()          # 提交修改(事务)
        db.close()
        return True
    except Exception as e:
        db.close()
        return "sql语句错误! ",e

# sql = "update t_user set username='zyhf1' where id=272"
# commit(sql)
# sql = "select * from t_user where id in (272, 273)"
# r = query(sql)   # ( (id, username, password...) , (id2, username2, passsword2,......))
# print(r)
# print(r[0][1])