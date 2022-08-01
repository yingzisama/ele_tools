# coding:gbk
import streamlit as st
import requests
import json
import random
import re
import time
import pymysql


class Ele_Tools():
    # ��¼��ȡ��Ӫ��̨cookies
    def login(self,now_host):
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

    # ���������uid�����ݻ���
    def uids_deal(self,uids):
        uid_dict = uids.split(",")
        uid = [x.strip() for x in uid_dict]
        while "" in uid:
            uid.remove("")
        return uid

    # ��ȡ�ɿ���uid
    def get_anchor_lists(self, cookie, Test_host, anchor_num, region):
        url_get_anchor_lists = Test_host + '/contract/anchor/list?page=1&size=200&nickname=&userId=&associationId=&contractType=&rank=&regionType={}'.format(region)
        url_liveing = Test_host+ "/live/playing/list"
        header_get_anchor = {
            'Host': Test_host.replace('http://',''),
            'Referer': Test_host + '/main',
            'Cookie': cookie,
        }
        try:
            res_get_anchor_lists = requests.get(url_get_anchor_lists, headers=header_get_anchor)  
            res_get_anchor_lists_json = json.loads(res_get_anchor_lists.text)
            anchor_lists = []
            i = 0
            list_num = list(range(0,199))
            random.shuffle(list_num)
            for num in list_num:
                anchor_id = res_get_anchor_lists_json['items'][num]['userId']
                data = {
                'associationId': "",
                'nickname': "",
                'page': 1,
                'rank': "",
                'regionType': "",
                'roomId': "",
                'signed': "",
                'size': 10,
                'userId': anchor_id,
                }
                res = requests.post(url_liveing,json=data,headers=header_get_anchor)
                res_json = json.loads(res.text)['items']
                if res_json == []:
                    anchor_lists.append(anchor_id)
                i += 1
                if anchor_lists.__len__() == anchor_num:
                    break
            str_anchor = ','.join(anchor_lists)
            return str_anchor
        except Exception as e:
            print(e)

    # ����ģ�⿪��
    def live_premiere(self,Test_host,region,Test_uids):
        # ��������uids��strת��dict
        list_uids = self.uids_deal(Test_uids)

        liveCode_list = []
        # ����dict��ִ�п���&�ص��ӿ�
        for j in range(len(list_uids)):
            print('j:{}'.format(j))
            test_uid = list_uids[j]
            # ���ÿ����ӿڣ���ȡ��Ӧ�ֶ�
            url_start = 'http://'+Test_host+'/studio/startForTest'
            data_start = {
            "channelType": 0,
            "coverId": "",
            "title": "ģ�⿪��ֱ����",
            "userId": test_uid
            }
            header_start = {
                'region': region,
                'uid':test_uid,
                'AppVersion':'4.30.0',
                'Content-Type':'application/json'
            }
            try:
                res_start = requests.post(url_start,json=data_start,headers=header_start)
                if json.loads(res_start.text)['code'] == 0:
                    userId = json.loads(res_start.text)['detail']['user']['userId']
                    liveCode = json.loads(res_start.text)['detail']['liveCode']
                    pushStreamUrl = json.loads(res_start.text)['detail']['pushStreamUrl']
                    pushStreamUrl_re = re.split(r'[?,\s]\s*', pushStreamUrl)[1]
                    streamId = json.loads(res_start.text)['detail']['streamId']
                    st.text(userId+'�����ɹ�')
                    # �����ɹ��󣬵��ûص��ӿ�
                    url_back = 'http://'+Test_host+'/multi/studio/callback'
                    data_back = {
                            "eventType":1,
                            "sign":"98a7d2dadf3475d33264bc9acee2ea4a",
                            "t":1652083093,
                            "appId":34772,
                            "userId":userId,
                            "extraString":liveCode,
                            "streamId":streamId,
                            "streamParam":pushStreamUrl_re,
                            "channelType":0,
                            "sequence":"835091404392722190",
                            "eventTime":1652082493000
                            }
                    header_back = {
                        'Content-Type':'application/json'
                    }
                    res_back = requests.post(url_back,json=data_back,headers=header_back)
                    liveCode_list.append(liveCode)
            except Exception as e:
                st.write('����ʧ�ܣ������˺��Ƿ���ʵ��')

        for i in range(9999):
            time.sleep(30)
            for k in range(len(list_uids)):
                try:
                    test_uid_ack = list_uids[k]
                    liveCode_ack = liveCode_list[k]
                    url = 'http://' + Test_host + '/studio/ack'
                    data = {
                        'liveCode':liveCode_ack,
                    }
                    header = {
                        'uid':test_uid_ack,
                        'Content-Type':'application/x-www-form-urlencoded'
                    }
                    while True:
                        try:
                            res = requests.post(url,data=data,headers=header,timeout=5)
                            break
                        except Exception as e:
                            # st.write('�����ӿ������쳣:'+e)
                            time.sleep(5)
                            # continue
                except Exception as e:
                    print(e)

    # �ر�ֱ����
    def live_close(self,now_host,cookie,userids):
        # ��������uids��strת��dict
        list_uids = self.uids_deal(userids)

        # ����dict��ִ�йز�
        for i in range(len(list_uids)):
            userid = list_uids[i]

            url_close = now_host+'/live/playing/list'
            data_close = {
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
            header_close = {
                'Host': now_host.replace('http://',''),
                'Referer': now_host + 'router/livevideo/playing',
                'Cookie': cookie,
            }
            try:
                res_close = requests.post(url_close,json=data_close,headers=header_close)
                res_text = res_close.text
                res_json_liveCode = json.loads(res_text)['items'][0]['liveCode']
            except:
                print('ֱ����δ����')

            url_forbidden = now_host + '/live/playing/forbidden'
            data_forbidden = {
                'userId':userid,
                'liveCode':res_json_liveCode,
            }
            header_forbidden = {
                'Host': now_host.replace('http://',''),
                'Referer': now_host + '/main',
                'Cookie': cookie,
            }
            try:
                res_forbidden = requests.post(url_forbidden,data=data_forbidden,headers=header_forbidden)
                res_code = json.loads(res_forbidden.text)['code'] 
                if res_code == 0:
                    st.success(userid+' �ز��ɹ�')
                else:
                    st.error(userid+' �ز�ʧ��')
            except:
                st.write(userid + ' �ز��쳣')

    # ʵ����֤
    def real_name_pass(self,now_host,cookie,userids):
        # ��������uids��strת��dict
        list_uids = self.uids_deal(userids)

        # ����dict��ִ�в�ѯ-���
        for i in range(len(list_uids)):
            userId = list_uids[i]
            url_certify = now_host + '/user/certify/list'
            header_certify = {
                    'Host': now_host.replace('http://',''),
                    'Referer': now_host + '/main',
                    'Cookie': cookie,
                }
            data_certify = {
                    'page': 1,
                    'size': 10,
                    'certifyStatus':'',
                    'userId':userId,
                    'regionType':''
                }
            res_certify = requests.post(url_certify, headers=header_certify,data=data_certify)
            res_text_certify = res_certify.text
            try:
                real_status =  json.loads(res_text_certify)['items'][0]['certifyStatus']
                real_id = json.loads(res_text_certify)['items'][0]['id']
            except:
                st.write('�û�δ�ύʵ����Ϣ����ȷ��')

            if real_status == 'FINISHED':
                st.success(userId + ' ʵ��״̬����ʵ��')
            elif real_status == 'PENDING_CHECK':
                st.write(userId + ' ʵ��״̬�������')
            else:
                st.write('���鵱ǰС���')

            url_realname = now_host + '/user/certify/verify'
            data_realname = {
                'id':real_id,
                'certifyStatus':'FINISHED'
            }
            header_realname = {
                    'Host': now_host.replace('http://',''),
                    'Referer': now_host + '/main',
                    'Cookie': cookie,
            }
            try:
                res_real = requests.post(url_realname,json=data_realname,headers=header_realname)
            except:
                st.error('�����˺�{}״̬'.format(real_id))

            res_certify = requests.post(url_certify, headers=header_certify,data=data_certify)
            res_text_certify = res_certify.text
            try:
                real_status =  json.loads(res_text_certify)['items'][0]['certifyStatus']
                real_id = json.loads(res_text_certify)['items'][0]['id']
            except:
                st.error('�û�δ�ύʵ����Ϣ����ȷ��')

            if real_status == 'FINISHED':
                st.success(userId + ' ʵ��״̬����ʵ��')
            elif real_status == 'PENDING_CHECK':
                st.info(userId + ' ʵ��״̬�������')
            else:
                st.error('���鵱ǰС���')

    def select_phoneNum(self,host,userId):
        # ��������uids��strת��dict
        list_uids = self.uids_deal(userId)

        # ����dict��ִ�в�ѯ-���
        for i in range(len(list_uids)):
            userId = list_uids[i]
            url = host + '/user/getUserInfoDetailsBasic'
            data = {
                'userId':userId,
            }
            header = {
                'Content-Type':'application/x-www-form-urlencoded'
            }
            try:
                res = requests.post(url,data=data,headers=header)
                res_text = json.loads(res.text)['detail']['phoneNumber']
                res_text_countryCode = json.loads(res.text)['detail']['countryCode']
                st.success('С��� {}�󶨵��ֻ���Ϊ{}+    {}'.format(userId,res_text_countryCode,res_text))
            except:
                st.error('�쳣����')

    def mysql_select(self,count,uid,ele_coin,ele_coin_type):
        list_uids = self.uids_deal(uid)
        count.ping(reconnect = True)
        # ���mysql���ݿ�ʵ����
        db1 = count.cursor()
        # ����dict��ִ�в�ѯ-���
        for i in range(len(list_uids)):
            userId = list_uids[i]
            # ִ��sql
            try:
                if ele_coin_type == '���':
                    db1.execute("update account.wallet_info set contributions_balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    count.commit()
                    # ������������
                    db1.execute("SELECT user_id, contributions_balance FROM account.wallet_info where user_id = '%s'" % (userId))
                    result = db1.fetchone()
                    print(result)
                    st.success('�˺�{}��ǰС������Ϊ{}'.format(userId,result[1]))
                elif ele_coin_type == '��':
                    db1.execute("update wallet.wallet_0 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    db1.execute("update wallet.wallet_1 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    db1.execute("update wallet.wallet_2 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    db1.execute("update wallet.wallet_3 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    db1.execute("update wallet.wallet_4 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    db1.execute("update wallet.wallet_5 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    db1.execute("update wallet.wallet_6 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    db1.execute("update wallet.wallet_7 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    db1.execute("update wallet.wallet_8 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    db1.execute("update wallet.wallet_9 set balance = '%s' where user_id = '%s'" % (ele_coin,userId))
                    count.commit()
                    st.write('��ֵ���')
            except Exception as e:
                st.error('��ֵʧ��~')
                st.write(e)



if __name__=='__main__':
    # ele = Ele_Tools()
    # host_test5 = 'http://showmetest5.elelive.cn:10009'
    # region = 'XM'
    # Test_uids = "Test12162713,Test12162758"
    # ele.live_premiere(host_test5,region,Test_uids)


    dev_host = 'http://192.168.50.5'
    userId = 'Test00000692'
    url = dev_host + '/user/getUserInfoDetailsBasic'
    data = {
        'userId':userId,
    }
    header = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    res = requests.post(url,data=data,headers=header)
    print(res.text)
