# coding:gbk
from ele_function import *
import streamlit as st
from ele_config import *

# 页面设置
st.set_page_config(
    page_title = "小象数据工厂",   
    page_icon = "random",        
    layout = "centered",         
    initial_sidebar_state = "auto",  
)

# 去掉右上角目录按钮
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 左边导航栏
sidebar = st.sidebar.radio(
    "功能导航",
    ("首页", '获取可开播uid',"直播间开播","直播间关播", "账号充值", "实名认证审批",'查询账号手机号')
)

# 可开播uid
if sidebar == "获取可开播uid":
    st.title('Elelive_TestTools')
    st.subheader('测试环境-批量获取可开播uid')
    st.write("批量获取有开播权限，但未开播的主播uid")
    ele_uids_host = st.selectbox(
        '选择测试环境',
        ('测试环境一','测试环境二','测试环境三','测试环境四','测试环境五')
    )

    if ele_uids_host == '测试环境一':
        hosts_uids = Ele_config.host_test1
    elif ele_uids_host == '测试环境二':
        hosts_uids = Ele_config.host_test2
    elif ele_uids_host == '测试环境三':
        hosts_uids = Ele_config.host_test3
    elif ele_uids_host == '测试环境四':
        hosts_uids = Ele_config.host_test4
    elif ele_uids_host == '测试环境五':
        hosts_uids = Ele_config.host_test5

    test_origin_ele_uids = st.selectbox(
            '选择地区',
            ('马来西亚', '新加坡','台湾' ,'越南','印尼','马来非华语'))

    if test_origin_ele_uids == '马来西亚':
        option_ele_uids = 'XM'
    elif test_origin_ele_uids == '新加坡':
        option_ele_uids = 'SG'
    elif test_origin_ele_uids == '台湾':
        option_ele_uids = 'TW'
    elif test_origin_ele_uids == '越南':
        option_ele_uids = 'VN'
    elif test_origin_ele_uids == '印尼':
        option_ele_uids = 'ID'
    elif test_origin_ele_uids == '马来非华语':
        option_ele_uids = 'MS'

    uid_num_creat = st.number_input('输入需要的uid个数,',step=1,min_value=1,max_value=100)

    if st.button('确定'):
        st.write('正在获取uid...')
        els_uids = Ele_Tools().get_anchor_lists(Ele_Tools().login(hosts_uids), hosts_uids, uid_num_creat, option_ele_uids)
        txt_realname = st.text_area('获取可开播uids', value=els_uids)


# 设置直播间开播页面展示
elif sidebar == "直播间开播":
    st.title('Elelive_TestTools')

    # 展示二级标题
    st.subheader('测试环境-模拟用户开播')
    ele_host_start = st.selectbox(
        '选择测试环境',
        ('测试环境一','测试环境二','测试环境三','测试环境四','测试环境五')
    )

    if ele_host_start == '测试环境一':
        hosts_start = Ele_config.host_start1
    elif ele_host_start == '测试环境二':
        hosts_start = Ele_config.host_start2
    elif ele_host_start == '测试环境三':
        hosts_start = Ele_config.host_start3
    elif ele_host_start == '测试环境四':
        hosts_start = Ele_config.host_start4
    elif ele_host_start == '测试环境五':
        hosts_start = Ele_config.host_start5

    test_origin_start = st.selectbox(
            '选择开播地区',
            ('马来西亚', '新加坡','台湾' ,'越南','印尼','马来非华语'))

    if test_origin_start == '马来西亚':
        option_start = 'XM'
    elif test_origin_start == '新加坡':
        option_start = 'SG'
    elif test_origin_start == '台湾':
        option_start = 'TW'
    elif test_origin_start == '越南':
        option_start = 'VN'
    elif test_origin_start == '印尼':
        option_start = 'ID'
    elif test_origin_start == '马来非华语':
        option_start = 'MS'

    txt_start = st.text_area('请输入uid，逗号分隔', value="请输入")

    if st.button('确定'):
        Ele_Tools().live_premiere(hosts_start,option_start,txt_start)

# 设置直播间关播页面展示
elif sidebar == "直播间关播":
    st.title('Elelive_TestTools')
    st.subheader('测试环境-直播间关播')
    ele_close_host = st.selectbox(
        '选择测试环境',
        ('测试环境一','测试环境二','测试环境三','测试环境四','测试环境五')
    )
    if ele_close_host == '测试环境一':
        hosts_close = Ele_config.host_test1
    elif ele_close_host == '测试环境二':
        hosts_close = Ele_config.host_test2
    elif ele_close_host == '测试环境三':
        hosts_close = Ele_config.host_test3
    elif ele_close_host == '测试环境四':
        hosts_close = Ele_config.host_test4
    elif ele_close_host == '测试环境五':
        hosts_close = Ele_config.host_test5

    txt_close = st.text_area('请输入uid，逗号分隔', value="请输入")

    if st.button('确定'):
        Ele_Tools().live_close(hosts_close,Ele_Tools().login(hosts_close),txt_close)

# 设置账号充值页面展示
elif sidebar == "账号充值":
    st.title('Elelive_TestTools')
    st.subheader('测试环境-账号充值')
    ele_topup_host = st.selectbox(
        '选择测试环境)',
        ('测试环境一','测试环境二','测试环境三','测试环境四','测试环境五')
    )

    ele_coin_type = st.selectbox(
        '选择充值类型',
        ('象币','象豆'))

    amount = st.number_input('输入充值金额',step=1)

    if ele_topup_host == '测试环境一':
        count = Ele_config.count1
    elif ele_topup_host == '测试环境二':
        count = Ele_config.count2
    elif ele_topup_host == '测试环境三':
        count = Ele_config.count3
    elif ele_topup_host == '测试环境四':
        count = Ele_config.count4
    elif ele_topup_host == '测试环境五':
        count = Ele_config.count5

    txt_topup = st.text_area('请输入uid', value="请输入")

    if st.button('确定'):
        Ele_Tools().mysql_select(count,txt_topup,amount,ele_coin_type)

# 设置实名认证审批页面展示
elif sidebar == "实名认证审批":
    st.title('Elelive_TestTools')
    st.subheader('测试环境-实名认证审批')
    ele_realname_host = st.selectbox(
        '选择测试环境',
        ('测试环境一','测试环境二','测试环境三','测试环境四','测试环境五')
    )

    if ele_realname_host == '测试环境一':
        hosts_realname = Ele_config.host_test1
    elif ele_realname_host == '测试环境二':
        hosts_realname = Ele_config.host_test2
    elif ele_realname_host == '测试环境三':
        hosts_realname = Ele_config.host_test3
    elif ele_realname_host == '测试环境四':
        hosts_realname = Ele_config.host_test4
    elif ele_realname_host == '测试环境五':
        hosts_realname = Ele_config.host_test5

    txt_realname = st.text_area('请输入uid，逗号分隔', value="请输入")

    if st.button('确定'):
        Ele_Tools().real_name_pass(hosts_realname,Ele_Tools().login(hosts_realname),txt_realname)

# 设置查询账号手机号页面展示
elif sidebar == "查询账号手机号":
    st.title('Elelive_TestTools')
    st.subheader('测试环境-查询账号手机号')
    ele_phone_host = st.selectbox(
        '选择测试环境',
        ('测试环境一','测试环境二','测试环境三','测试环境四','测试环境五')
    )

    if ele_phone_host == '测试环境一':
        hosts_phone = Ele_config.host_account1
    elif ele_phone_host == '测试环境二':
        hosts_phone = Ele_config.host_account2
    elif ele_phone_host == '测试环境三':
        hosts_phone = Ele_config.host_account3
    elif ele_phone_host == '测试环境四':
        hosts_phone = Ele_config.host_account4
    elif ele_phone_host == '测试环境五':
        hosts_phone = Ele_config.host_account5

    txt_phone = st.text_area('请输入uid，逗号分隔', value="请输入")

    if st.button('确定'):
        Ele_Tools().select_phoneNum(hosts_phone,txt_phone)



# 设置首页页面展示
else:
    st.title("小象直播测试——数据工厂")
    st.write("数据工厂能快速、方便、批量的进行一些操作,缩减测试时间,提高测试工作效率~")
    st.image('./woman-ga660503d8_1920.jpg')