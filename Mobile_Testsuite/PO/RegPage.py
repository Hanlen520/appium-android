#######################################################
# FileName:RegPage.py
# Author:wang xiaoxiao
# Date:2018-6-27
# Function Description: 封装register page页面的元素和操作
#######################################################

from selenium.webdriver.common.by import By
from Mobile_Testsuite.PO.BasePage import Element


# 继承Element类
class RegPage(Element):
    # 定位元素：通过元素属性定位register page页面中的元素

    # Logo图标
    logo_loc = (By.XPATH, '//*[@id="newusers"]/div')

    # 账户图标
    username_icon_loc = (By.XPATH, '//*[@id="newusers-form"]/div[1]/label')
    # 账户输入框
    username_input_loc = (By.ID, 'username')

    # 密码图标
    password_icon_loc = (By.XPATH, '//*[@id="newusers-form"]/div[2]/label')
    # 密码输入框
    password_input_loc = (By.ID, 'password')

    # 邮箱图标
    email_icon_loc = (By.XPATH, '//*[@id="newusers-form"]/div[3]/label')
    # 邮箱输入框
    email_input_loc = (By.ID, 'user-email')

    # Telegram图标
    telegram_icon_loc = (By.XPATH, '//*[@id="newusers-form"]/div[4]/label')
    # Telegram输入框
    telegram_input_loc = (By.ID, 'user-telegram')

    # 服务条款勾选框
    service_check_loc = (By.XPATH, '//*[@id="newusers-form"]/div[5]/label/span/input')
    # 我接受服务条款文本
    service_text_loc = (By.XPATH, '//*[@id="newusers-form"]/div[5]/div')
    # 服务条款文本
    service_btn_loc = (By.XPATH, '//*[@id="newusers-form"]/div[5]/div/a')

    # 进入游戏按钮
    register_btn_loc = (By.XPATH, '//*[@id="newusers-form"]/button')

    # 试玩币说明币种图片信息
    information_img_loc = (By.XPATH, '//*[@id="newusers-form"]/div[6]/div[1]/img')
    # 试玩币说明文本信息
    information_text_loc = (By.XPATH, '//*[@id="newusers-form"]/div[6]/div[2]/span')

    # 底栏
    bottom_loc = (By.ID, 'footer')

    # 操作方法

    # 点击进入游戏按钮
    def click_register_btn(self):
        self.click(self.register_btn_loc)

    # 点击服务条款弹出弹窗
    def click_service_btn(self):
        self.click(self.service_btn_loc)

    # 输入用户名
    def send_username(self, username):
        self.send_key(self.username_input_loc, username)

    # 输入密码
    def send_password(self, password):
        self.send_key(self.password_input_loc, password)

    # 输入邮箱
    def send_email(self, email):
        self.send_key(self.email_input_loc, email)

    # 输入Telegram
    def send_telegram(self, telegram):
        self.send_key(self.telegram_input_loc, telegram)

    # 登录页面元素是否显示
    def register_element_is_display(self):
        self.is_display(self.logo_loc)
        self.is_display(self.username_icon_loc)
        self.is_display(self.username_input_loc)
        self.is_display(self.password_icon_loc)
        self.is_display(self.password_input_loc)
        self.is_display(self.email_icon_loc)
        self.is_display(self.email_input_loc)
        self.is_display(self.telegram_icon_loc)
        self.is_display(self.telegram_input_loc)
        self.is_display(self.service_check_loc)
        self.is_display(self.service_text_loc)
        self.is_display(self.register_btn_loc)
        self.is_display(self.information_img_loc)
        self.is_display(self.information_text_loc)
        self.is_display(self.bottom_loc)

    # 获取用户名输入框默认文本
    def get_username_text(self):
        username_value = self.find_element(*self.username_input_loc).get_attribute('placeholder')
        return username_value

    # 获取密码输入框默认文本
    def get_password_text(self):
        password_value = self.find_element(*self.password_input_loc).get_attribute('placeholder')
        return password_value

    # 获取邮箱输入框默认文本
    def get_email_text(self):
        email_value = self.find_element(*self.email_input_loc).get_attribute('placeholder')
        return email_value

    # 获取Telegram输入框默认文本
    def get_telegram_text(self):
        telegram_value = self.find_element(*self.telegram_input_loc).get_attribute('placeholder')
        return telegram_value

    # 获取试玩币说明文本信息
    def get_information_text(self):
        information_text = self.find_element(*self.information_text_loc).text
        return information_text

    # 判断进入游戏注册按钮是否禁用
    def register_btn_is_enabled(self):
        true_or_false = self.find_element(*self.register_btn_loc).is_enabled()
        return true_or_false

    # 判断服务条款是否被勾选
    def service_btn_is_selected(self):
        true_or_false = self.find_element(*self.service_check_loc).is_selected()
        return true_or_false