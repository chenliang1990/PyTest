import requests
import os, sys
sys.path.append(os.getcwd())

#测试轮播图接口
def test_01_lbt():
    #1.构造请求
    u = "http://192.144.148.91:2333/get_title_img"
    res = requests.get(u)
    #2.断言结果
    assert res.status_code == 200
    assert res.json()["status"] == 200