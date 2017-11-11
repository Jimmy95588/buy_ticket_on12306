#!/usr/bin/python
# #  FileName    : buy_ticket_on12306.py
# #  Author      : Haiyang Kong <985661979@qq.com>
# #  Created     : Sat Nov 11 22:08:41 2015 by Haiyang Kong
# #  Copyright   : Feather (c) 2017
# #  Description : auto 12306
# #  Time-stamp: <2017-11-11 16:28:41>
# #  �ó���������12306��Ʊ
# #  �ó�����Ҫ�õ���selenium��

from selenium import webdriver
from time import sleep
import traceback

username = u"******"		#12306�û���
passwd = u"******"			#12036����
starts = u"******"			#����Ϊ��ʼ��ַ��cookiesֵ����Ҫ�����û��ڹ�������
ends = u"******"			#����Ϊ�յ��ַ��cookiesֵ����Ҫ�����û��ڹ�������
dtime = u"****-**-**"		#����Ϊ����ʱ��
fromstation = "_jc_save_fromStation"
tostation = "_jc_save_toStation"
fromdate = "_jc_save_fromDate"
order = 0
pa = u"***"

ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"		#ѡƱ����url
login_url = "https://kyfw.12306.cn/otn/login/init"				#��½����url
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"		#���˽���url
#��¼����
def login():    
    driver.find_element_by_name("loginUserDTO.user_name").send_keys(username)
    driver.find_element_by_name("userDTO.password").send_keys(passwd)
    print(u"�ȴ���֤�룬���������롣����")
    while True:
        if driver.current_url != initmy_url:
            sleep(1)
        else:
            break
#��Ʊ����
def buy_ticket():
    global driver
    driver = webdriver.Chrome(r"******\chromedriver.exe")		#�˴���Ҫ��дchrome������λ��
    while driver.current_url != ticket_url:
        driver.get(ticket_url)
        sleep(1)
    while driver.find_element_by_link_text(u"��¼"):
        driver.find_element_by_link_text(u"��¼").click()
        sleep(1)
        login()
        break
buy_ticket()
try:
    print(u"��Ʊҳ�档����")
    while order == 0:
        click_chaxun = 0
        click_yuding = 0
        click_pa = 0
        click_queren = 0
        click_tijiaodingdan = 0
        click_fanhuixiugai = 0
        while driver.current_url != ticket_url:
            driver.get(ticket_url)
            driver.add_cookie({"name" : fromstation, "value" : starts})
            driver.add_cookie({"name" : tostation,"value" : ends})
            driver.add_cookie({"name":fromdate,"value" : dtime})
            driver.refresh()
        while click_chaxun == 0:
            sleep(2)
            driver.find_element_by_link_text(u"��ѯ").click()
            click_chaxun = 1
        while click_yuding == 0:
            sleep(2)
            driver.find_element_by_link_text(u"Ԥ��").click()
            click_yuding = 1
        while click_pa == 0:
            sleep(5)
            driver.find_element_by_xpath('//label[@for="normalPassenger_0"]').click()
            click_pa= 1
        driver.switch_to_alert()			#��ת��������
        sleep(2)
        while click_queren ==0:
            sleep(2)
            driver.find_element_by_xpath('//*[@id="qd_closeDefaultWarningWindowDialog_id"]').click()
            click_queren = 1            
        while click_tijiaodingdan == 0:
            sleep(2)
            driver.find_element_by_link_text(u"�ύ����").click()
            click_tijiaodingdan = 1
        while click_fanhuixiugai == 0:
            driver.switch_to_alert()
            sleep(4)
            driver.find_element_by_xpath('//*[@id="qr_submit_id"]').click()
            click_fanhuixiugai = 1
        break
        
except Exception as e:
    print(traceback.print_exc())