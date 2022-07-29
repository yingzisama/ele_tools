# coding:gbk
import requests

def httpget():
    url='http://showmetest-2011.elelive.cn/studio-service/ee/payroom/order'
    data = {
        'anchorId':'Test00011590',
    }
    herder = {
        'uid':'Test00011882',
        'accessToken':'e1fa1dd9ff1d4508be4533db30ce8d48',
        'deviceId':'23DED64A716848B78413F16709EE9F51'
    }
    res = requests.post(url,json=data,headers=herder)
    print(res.text)

if __name__ == '__main__':
    httpget()