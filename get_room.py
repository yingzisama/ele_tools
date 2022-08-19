# coding:gbk
import requests
import json

def login(now_host):
    url = now_host+'/login'
    if now_host == 'http://showmetest3.elelive.cn:10009' :
        data = {
        'smsCode':'1234',
        'userCode':'Fish'
        }
    elif now_host == 'http://showmetest5.elelive.cn:10009' :
        data = {
        'smsCode':'1234',
        'userCode':'Fish'
        }
    else:
        data = {
        'smsCode':'1234',
        'userCode':'admin'
    }
    res = requests.post(url,data=data)
    cookies = res.cookies
    cookie = requests.utils.dict_from_cookiejar(cookies)
    (key, value), = cookie.items()
    new_cookie = key + '=' + value
    return new_cookie

def get_liveCode(now_host,cookie,userid):
    url = now_host+'/live/playing/list'
    data = {
        "page": 1,
        "size": 10,
        "roomId": "",
        "userId": userid,
        "nickname": "",
        "signed": "",
        "associationId": "",
        "rank": "",
        "regionType": ""
    }
    header = {
        'Host': now_host.replace('http://',''),
        'Referer': now_host + 'router/livevideo/playing',
        'Cookie': cookie,
    }
    try:
        res = requests.post(url,json=data,headers=header)
        res_text = res.text
        res_json = json.loads(res_text)['items'][0]['liveCode']
        return res_json
    except:
        print('直播间未开播')

def come_liveroom(live_code,userid,anchor):
    url = 'http://account03.svc.elelive.cn/studio/chatroom/testMemberOnJoin'

    header = {
        'Content-Type': 'application/json',
        'Host': 'studio03.svc.elelive.cn',
        'Origin': 'http://studio03.svc.elelive.cn',
        'uid': userid,
    }
    data = {
        "groupId": anchor+'_'+live_code,
	    "userId": userid
    }
    res = requests.post(url,json=data,headers=header)
    print(res.text)




if __name__=='__main__':
    host = 'http://showmetest3.elelive.cn:10009'
    cookie = login(host)
    anchor = '10003673'
    live_code = get_liveCode(host,cookie,anchor)
    # 粉丝团观众
    # Test00027563,
    # 普通观众
    uids = ['Test12230591','Test12230582','10002775','10002998','10010911','10012100','10008801','10010026','10003554','10003183','10005298','10009618','10004722','10000194','10000000','10008962','10008443','10003025','10003804','10007143','10010384','10007094','10004986','10010550']
    # uids = ['10002775']
    for uid in uids:
        come_liveroom(live_code,uid,anchor)