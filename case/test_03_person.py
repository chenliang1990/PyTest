import requests
import os, sys
sys.path.append(os.getcwd())
from utils.dbtools import query
from utils.filetools import write_file,read_file

def test_01_xgtx():
    u = "http://192.144.148.91:2333/updateuserheadpic"
    d = {"ximg":"123.jpg"}
    h = {"Content-Type":"application/json","token":read_file("user_token.txt")}
    res = requests.post(url=u, json=d, headers=h)

    assert res.status_code == 200
    assert res.json()["status"] == 200

    sql = "select * from t_user where username='{}' and headpic='{}'".format("huang300k",d["ximg"])
    assert len(query(sql)) != 0