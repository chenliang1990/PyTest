# #练习：
# 使用pytest实现一个提交文章的case， 断言要有数据库、两个码判断
# - ps：tags： 测试1234
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file,read_file
from utils.exceltools import read_excel
def test_01_articleNew():
    r = read_excel("data\\测谈网接口测试用例.xlsx","Sheet1")
    u = r[4][2]
    d = eval(r[4][3])
    h = eval(r[4][4])
    res = requests.post(url=u, json=d, headers=h)
    
    assert res.status_code == r[4][6]
    assert res.json()["status"] == r[4][7]
    sql = "select * from t_article where id='{}'".format(res.json()["data"]["articleid"])
    assert len(query(sql)) != 0

    