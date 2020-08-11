import requests
import os, sys
sys.path.append(os.getcwd())
from utils.exceltools import read_excel

#测试轮播图接口
def test_01_lbt():
    r = read_excel("data\\测谈网接口测试用例.xlsx","Sheet1")
    #1.构造请求
    res = requests.get(r[0][2])
    #2.断言结果
    assert res.status_code == r[0][6]
    assert res.json()["status"] == r[0][7]

def test_02_question():
    r = read_excel("data\\测谈网接口测试用例.xlsx","Sheet1")
    res = requests.get(r[1][2])
    assert res.status_code == r[1][6]
    assert res.json()["status"] == r[1][7]