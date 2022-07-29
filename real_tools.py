# coding:gbk
from ele_function import *
import streamlit as st
from ele_config import *

# ҳ������
st.set_page_config(
    page_title = "С�����ݹ���",   
    page_icon = "random",        
    layout = "centered",         
    initial_sidebar_state = "auto",  
)

# ȥ�����Ͻ�Ŀ¼��ť
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ��ߵ�����
sidebar = st.sidebar.radio(
    "���ܵ���",
    ("��ҳ", '��ȡ�ɿ���uid',"ֱ���俪��","ֱ����ز�", "�˺ų�ֵ", "ʵ����֤����",'��ѯ�˺��ֻ���')
)

# �ɿ���uid
if sidebar == "��ȡ�ɿ���uid":
    st.title('Elelive_TestTools')
    st.subheader('���Ի���-������ȡ�ɿ���uid')
    st.write("������ȡ�п���Ȩ�ޣ���δ����������uid")
    ele_uids_host = st.selectbox(
        'ѡ����Ի���',
        ('���Ի���һ','���Ի�����','���Ի�����','���Ի�����','���Ի�����')
    )

    if ele_uids_host == '���Ի���һ':
        hosts_uids = Ele_config.host_test1
    elif ele_uids_host == '���Ի�����':
        hosts_uids = Ele_config.host_test2
    elif ele_uids_host == '���Ի�����':
        hosts_uids = Ele_config.host_test3
    elif ele_uids_host == '���Ի�����':
        hosts_uids = Ele_config.host_test4
    elif ele_uids_host == '���Ի�����':
        hosts_uids = Ele_config.host_test5

    test_origin_ele_uids = st.selectbox(
            'ѡ�����',
            ('��������', '�¼���','̨��' ,'Խ��','ӡ��','�����ǻ���'))

    if test_origin_ele_uids == '��������':
        option_ele_uids = 'XM'
    elif test_origin_ele_uids == '�¼���':
        option_ele_uids = 'SG'
    elif test_origin_ele_uids == '̨��':
        option_ele_uids = 'TW'
    elif test_origin_ele_uids == 'Խ��':
        option_ele_uids = 'VN'
    elif test_origin_ele_uids == 'ӡ��':
        option_ele_uids = 'ID'
    elif test_origin_ele_uids == '�����ǻ���':
        option_ele_uids = 'MS'

    uid_num_creat = st.number_input('������Ҫ��uid����,',step=1,min_value=1,max_value=100)

    if st.button('ȷ��'):
        st.write('���ڻ�ȡuid...')
        els_uids = Ele_Tools().get_anchor_lists(Ele_Tools().login(hosts_uids), hosts_uids, uid_num_creat, option_ele_uids)
        txt_realname = st.text_area('��ȡ�ɿ���uids', value=els_uids)


# ����ֱ���俪��ҳ��չʾ
elif sidebar == "ֱ���俪��":
    st.title('Elelive_TestTools')

    # չʾ��������
    st.subheader('���Ի���-ģ���û�����')
    ele_host_start = st.selectbox(
        'ѡ����Ի���',
        ('���Ի���һ','���Ի�����','���Ի�����','���Ի�����','���Ի�����')
    )

    if ele_host_start == '���Ի���һ':
        hosts_start = Ele_config.host_start1
    elif ele_host_start == '���Ի�����':
        hosts_start = Ele_config.host_start2
    elif ele_host_start == '���Ի�����':
        hosts_start = Ele_config.host_start3
    elif ele_host_start == '���Ի�����':
        hosts_start = Ele_config.host_start4
    elif ele_host_start == '���Ի�����':
        hosts_start = Ele_config.host_start5

    test_origin_start = st.selectbox(
            'ѡ�񿪲�����',
            ('��������', '�¼���','̨��' ,'Խ��','ӡ��','�����ǻ���'))

    if test_origin_start == '��������':
        option_start = 'XM'
    elif test_origin_start == '�¼���':
        option_start = 'SG'
    elif test_origin_start == '̨��':
        option_start = 'TW'
    elif test_origin_start == 'Խ��':
        option_start = 'VN'
    elif test_origin_start == 'ӡ��':
        option_start = 'ID'
    elif test_origin_start == '�����ǻ���':
        option_start = 'MS'

    txt_start = st.text_area('������uid�����ŷָ�', value="������")

    if st.button('ȷ��'):
        Ele_Tools().live_premiere(hosts_start,option_start,txt_start)

# ����ֱ����ز�ҳ��չʾ
elif sidebar == "ֱ����ز�":
    st.title('Elelive_TestTools')
    st.subheader('���Ի���-ֱ����ز�')
    ele_close_host = st.selectbox(
        'ѡ����Ի���',
        ('���Ի���һ','���Ի�����','���Ի�����','���Ի�����','���Ի�����')
    )
    if ele_close_host == '���Ի���һ':
        hosts_close = Ele_config.host_test1
    elif ele_close_host == '���Ի�����':
        hosts_close = Ele_config.host_test2
    elif ele_close_host == '���Ի�����':
        hosts_close = Ele_config.host_test3
    elif ele_close_host == '���Ի�����':
        hosts_close = Ele_config.host_test4
    elif ele_close_host == '���Ի�����':
        hosts_close = Ele_config.host_test5

    txt_close = st.text_area('������uid�����ŷָ�', value="������")

    if st.button('ȷ��'):
        Ele_Tools().live_close(hosts_close,Ele_Tools().login(hosts_close),txt_close)

# �����˺ų�ֵҳ��չʾ
elif sidebar == "�˺ų�ֵ":
    st.title('Elelive_TestTools')
    st.subheader('���Ի���-�˺ų�ֵ')
    ele_topup_host = st.selectbox(
        'ѡ����Ի���)',
        ('���Ի���һ','���Ի�����','���Ի�����','���Ի�����','���Ի�����')
    )

    ele_coin_type = st.selectbox(
        'ѡ���ֵ����',
        ('���','��'))

    amount = st.number_input('�����ֵ���',step=1)

    if ele_topup_host == '���Ի���һ':
        count = Ele_config.count1
    elif ele_topup_host == '���Ի�����':
        count = Ele_config.count2
    elif ele_topup_host == '���Ի�����':
        count = Ele_config.count3
    elif ele_topup_host == '���Ի�����':
        count = Ele_config.count4
    elif ele_topup_host == '���Ի�����':
        count = Ele_config.count5

    txt_topup = st.text_area('������uid', value="������")

    if st.button('ȷ��'):
        Ele_Tools().mysql_select(count,txt_topup,amount,ele_coin_type)

# ����ʵ����֤����ҳ��չʾ
elif sidebar == "ʵ����֤����":
    st.title('Elelive_TestTools')
    st.subheader('���Ի���-ʵ����֤����')
    ele_realname_host = st.selectbox(
        'ѡ����Ի���',
        ('���Ի���һ','���Ի�����','���Ի�����','���Ի�����','���Ի�����')
    )

    if ele_realname_host == '���Ի���һ':
        hosts_realname = Ele_config.host_test1
    elif ele_realname_host == '���Ի�����':
        hosts_realname = Ele_config.host_test2
    elif ele_realname_host == '���Ի�����':
        hosts_realname = Ele_config.host_test3
    elif ele_realname_host == '���Ի�����':
        hosts_realname = Ele_config.host_test4
    elif ele_realname_host == '���Ի�����':
        hosts_realname = Ele_config.host_test5

    txt_realname = st.text_area('������uid�����ŷָ�', value="������")

    if st.button('ȷ��'):
        Ele_Tools().real_name_pass(hosts_realname,Ele_Tools().login(hosts_realname),txt_realname)

# ���ò�ѯ�˺��ֻ���ҳ��չʾ
elif sidebar == "��ѯ�˺��ֻ���":
    st.title('Elelive_TestTools')
    st.subheader('���Ի���-��ѯ�˺��ֻ���')
    ele_phone_host = st.selectbox(
        'ѡ����Ի���',
        ('���Ի���һ','���Ի�����','���Ի�����','���Ի�����','���Ի�����')
    )

    if ele_phone_host == '���Ի���һ':
        hosts_phone = Ele_config.host_account1
    elif ele_phone_host == '���Ի�����':
        hosts_phone = Ele_config.host_account2
    elif ele_phone_host == '���Ի�����':
        hosts_phone = Ele_config.host_account3
    elif ele_phone_host == '���Ի�����':
        hosts_phone = Ele_config.host_account4
    elif ele_phone_host == '���Ի�����':
        hosts_phone = Ele_config.host_account5

    txt_phone = st.text_area('������uid�����ŷָ�', value="������")

    if st.button('ȷ��'):
        Ele_Tools().select_phoneNum(hosts_phone,txt_phone)



# ������ҳҳ��չʾ
else:
    st.title("С��ֱ�����ԡ������ݹ���")
    st.write("���ݹ����ܿ��١����㡢�����Ľ���һЩ����,��������ʱ��,��߲��Թ���Ч��~")
    st.image('./woman-ga660503d8_1920.jpg')