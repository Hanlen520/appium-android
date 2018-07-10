#######################################################
# FileName:common.py
# Author:liketao
# Date:2018-6-20
# Function Description: 封装testcase中的一些公共方法
#######################################################
from appium import webdriver
import random
import string
from Mobile_Testsuite.PO.HomePage import HomePage
from Mobile_Testsuite.PO.LoginPage import LoginPage


class Common(object):
    def __init__(self, driver):
        self.driver = driver
        self.HomePage = HomePage(self.driver)
        self.LoginPage = LoginPage(self.driver)
        self.baseurl = 'http://192.168.8.21:8989/home'

    def login(self):
        self.driver.get(self.baseurl)
        self.HomePage.click_register_btn()
        self.LoginPage.login_test_account()

    def enter_account_page(self):
        self.login()
        self.HomePage.click_account_btn()

    def register(self):
        # 组合数字与小写字母的序列
        s = string.digits + string.ascii_lowercase
        # 随机取出6个字母和数字的组合合并成字符串
        random_data = ''.join(random.sample(s, 6))
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]').click()
        self.driver.find_element_by_link_text("新用户注册").click()
        # self.driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/a[2]').click() 同上一句功能一致，点击新用户注册按钮
        self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[1]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[1]/input').send_keys(random_data)
        self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[2]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[2]/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[3]/input').clear()
        self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[3]/input').send_keys(random_data + '@qq.com')
        # self.driver.press_keycode('4')
        # self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[4]/label/span[1]/span').click()
        self.driver.find_element_by_xpath('//*[@id="newusers-form"]/button').click()

