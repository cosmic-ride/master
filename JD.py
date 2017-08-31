#!/usr/bin/env python
# encoding: utf-8

from selenium import webdriver
import datetime
import time


driver = webdriver.Chrome()

def login(uname, pwd):
    driver.get("http://www.jd.com")
    driver.find_element_by_link_text("你好，请登录").click()
    time.sleep(3)
    driver.find_element_by_link_text("账户登录").click()
    driver.find_element_by_name("loginname").send_keys(uname)
    driver.find_element_by_name("nloginpwd").send_keys(pwd)
    driver.find_element_by_id("loginsubmit").click()
    time.sleep(3)
    driver.get("https://cart.jd.com/cart.action")
    time.sleep(3)
    driver.find_element_by_link_text("去结算").click()
    now = datetime.datetime.now()
    print(now.strftime('%Y-%m-%d %H:%M:%S'))
    print('login success')


# buytime = '2016-12-27 22:31:00'
def buy_on_time(buytime):
    count = 0
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            driver.find_element_by_id('order-submit').click()
            time.sleep(3)
            print(now.strftime('%Y-%m-%d %H:%M:%S'))
            print('purchase success')
            break
        time.sleep(0.5)
        print('尝试下单  第 %s 次 ' % count)
        count += 1


# entrance  用户名，密码

if __name__ == '__main__':
    #登陆
    login('***', '***')
    #指定下单时间
    buy_on_time('2017-08-31 20:06:00')