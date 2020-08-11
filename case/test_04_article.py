# #练习：
# 使用pytest实现一个提交文章的case， 断言要有数据库、两个码判断
# - ps：tags： 测试1234
import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file,read_file

def test_01_articleNew():
    u = "http://192.144.148.91:2333/article/new"
    d = {"title":"如何学习测试","content":"测试222内容","tags":"测试1234","brief":"测试介绍","ximg":"sss.jpg"}
    h = {"Content-Type":"application/json","token":read_file("user_token.txt")}
    res = requests.post(url=u, json=d, headers=h)
    
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "select * from t_article where id='{}'".format(res.json()["data"]["articleid"])
    assert len(query(sql)) != 0

    