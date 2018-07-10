#######################################################
# FileName:LoginPage.py
# Author:wang xiaoxiao
# Date:2018-6-20
# Function Description: 封装login page页面的元素和操作
#######################################################

from selenium.webdriver.common.by import By
from Mobile_Testsuite.PO.BasePage import Element


# 继承Element类
class LoginPage(Element):
    # 定位元素：通过元素属性定位login page页面中的元素

    # Logo图标
    logo_loc = (By.XPATH, '/html/body/div/div[6]/div/div[1]')

    # 账户图标
    username_icon_loc = (By.XPATH, '//*[@id="form_login"]/div[1]/label')
    # 账户输入框
    username_input_loc = (By.XPATH, '//*[@id="login-name"]')

    # 密码图标
    password_icon_loc = (By.XPATH, '//*[@id="form_login"]/div[2]/label')
    # 密码输入框
    password_input_loc = (By.XPATH, '//*[@id="login-password"]')

    # 登录按钮
    confirm_btn_loc = (By.XPATH, '//*[@id="form_login"]/button')

    # 忘记密码页面链接
    forgot_link_loc = (By.LINK_TEXT, '忘记密码')

    # 新用户注册页面链接
    register_link_loc = (By.LINK_TEXT, '新用户注册')

    # 底栏
    bottom_loc = (By.ID, 'footer')

    # 操作方法

    # 点击登录按钮
    def click_confirm_btn(self):
        self.click(self.confirm_btn_loc)

    # 点击忘记密码
    def click_forgot_link(self):
        self.click(self.forgot_link_loc)

    # 点击新用户注册
    def click_register_link(self):
        self.click(self.register_link_loc)

    # 输入用户名
    def send_username(self, username):
        self.send_key(self.username_input_loc, username)

    # 输入密码
    def send_password(self, password):
        self.send_key(self.password_input_loc, password)

    # 登录页面元素是否显示
    def login_element_is_display(self):
        login_element = {self.logo_loc,
                         self.username_icon_loc,
                         self.username_input_loc,
                         self.password_icon_loc,
                         self.password_input_loc,
                         self.confirm_btn_loc,
                         self.forgot_link_loc,
                         self.register_link_loc,
                         self.bottom_loc}
        for element in login_element:
            self.is_display(element)

    # 获取用户名输入框默认文本
    def get_username_text(self):
        username_value = self.find_element(*self.username_input_loc).get_attribute('placeholder')
        return username_value

    # 获取密码输入框默认文本
    def get_password_text(self):
        password_value = self.find_element(*self.password_input_loc).get_attribute('placeholder')
        return password_value

    # 判断登录按钮是否禁用
    def login_btn_is_enable(self):
        true_or_false = self.find_element(*self.confirm_btn_loc).is_enabled()
        return true_or_false

    # 登录测试账号
    def login_test_account(self):
        self.send_username('test001')
        self.send_password('123456')
        self.click_confirm_btn()
