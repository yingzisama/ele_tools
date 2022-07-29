# coding:gbk
import pymysql

class Ele_config():
    host_start1 = 'studio01.svc.elelive.cn'
    host_start2 = 'studio02.svc.elelive.cn'
    host_start3 = 'studio03.svc.elelive.cn'
    host_start4 = 'studio04.svc.elelive.cn'
    host_start5 = 'studio05.svc.elelive.cn'

    host_account1 = 'http://account01.svc.elelive.cn'
    host_account2 = 'http://account02.svc.elelive.cn'
    host_account3 = 'http://account03.svc.elelive.cn'
    host_account4 = 'http://account04.svc.elelive.cn'
    host_account5 = 'http://account05.svc.elelive.cn'

    host_test1 = 'http://showmetest-2011.elelive.cn:10009'
    host_test2 = 'http://showmetest2.elelive.cn:10009'
    host_test3 = 'http://showmetest3.elelive.cn:10009'
    host_test4 = 'http://showmetest4.elelive.cn:10009'
    host_test5 = 'http://showmetest5.elelive.cn:10009'


    count1 = pymysql.connect(
    host = 'rm-wz9j9pe0u90c474t1yo.mysql.rds.aliyuncs.com',     
    port = 3306,        
    user='showmetest_app',        
    password='M90JB123kdF95',     
    db= '',  
    charset = 'gbk'     
    )

    count2 = pymysql.connect(
    host = 'showmetest2.elelive.cn',     
    port = 10633,        
    user='showmetest_app',        
    password='M90JB123kdF95',     
    db= '',  
    charset = 'gbk'     
    )

    count3 = pymysql.connect(
    host = 'mysqltest3.elelive.cn',     
    port = 10634,        
    user='showmetest_app',        
    password='M90JB123kdF95',     
    db= '',  
    charset = 'gbk'     
    )

    count4 = pymysql.connect(
    host = 'showmetest4.elelive.cn',     
    port = 10635,        
    user='showmetest_app',        
    password='M90JB123kdF95',     
    db= '',  
    charset = 'gbk'     
    )

    count5 = pymysql.connect(
    host = '47.107.239.95',     
    port = 3306,        
    user='showmetest_app',        
    password='M90JB123kdF95',     
    db= '',  
    charset = 'gbk'     
    )
