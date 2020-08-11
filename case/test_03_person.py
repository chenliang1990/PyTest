import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file,read_file
from utils.exceltools import read_excel

def test_01_xgtx():
    r = read_excel("data\\测谈网接口测试用例.xlsx","Sheet1")
    u = r[3][2]
    d = eval(r[3][3])
    # h = {"Content-Type":"application/json","token":read_file("user_token.txt")}
    h = eval(r[3][4])
    res = requests.post(url=u, json=d, headers=h)
    assert res.status_code == r[3][6]
    assert res.json()["status"] == r[3][7]

    sql = "select * from t_user where username='{}' and headpic='{}'".format("huang300k",d["ximg"])
    assert len(query(sql)) != 0