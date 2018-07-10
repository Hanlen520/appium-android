#######################################################
# FileName:FogotPwPage.py
# Author:wang xiaoxiao
# Date:2018-6-28
# Function Description: 封装forgotPassword page页面的元素和操作
#######################################################

from selenium.webdriver.common.by import By
from Mobile_Testsuite.PO.BasePage import Element


# 继承Element类
class FogotPwPage(Element):
    # 定位元素：通过元素属性定位forgotPassword page页面中的元素

    # Logo图标
    logo_loc = (By.XPATH, '//*[@id="fotgotpassword"]/div')

    # 账户图标
    username_icon_loc = (By.XPATH, '//*[@id="fotgot-form"]/div[1]/label')
    # 账户输入框
    username_input_loc = (By.ID, 'fotgot-name')

    # 邮箱图标
    email_icon_loc = (By.XPATH, '//*[@id="fotgot-form"]/div[2]/label')
    # 邮箱输入框
    email_input_loc = (By.ID, 'fotgot-email')

    # 验证码图标
    code_icon_loc = (By.XPATH, '//*[@id="fotgot-form"]/div[3]/label')
    # 验证码输入框
    code_input_loc = (By.ID, 'fotgot-verify')
    # 验证按图片
    code_img_loc = (By.XPATH, '//*[@id="verification_code_image"]')

    # 发送重置链接到邮箱按钮
    sendLink_btn_loc = (By.XPATH, '//*[@id="fotgot-form"]/button')

    # 提交成功提示
    correct_loc = (By.XPATH, '//*[@id="body_main"]/div/div[2]')

    # 底栏
    bottom_loc = (By.ID, 'footer')

    # 操作方法

    # 点击发送重置链接到邮箱按钮
    def click_send_link_btn(self):
        self.click(self.sendLink_btn_loc)

    # 点击验证码图片
    def click_code_img(self):
        self.click(self.code_img_loc)

    # 输入用户名
    def send_username(self, username):
        self.send_key(self.username_input_loc, username)

    # 输入邮箱
    def send_email(self, email):
        self.send_key(self.email_input_loc, email)

    # 输入验证码
    def send_code(self, code):
        self.send_key(self.code_input_loc, code)

    # 登录页面元素是否显示
    def forgot_password_element_is_display(self):
        self.is_display(self.logo_loc)
        self.is_display(self.username_icon_loc)
        self.is_display(self.username_input_loc)
        self.is_display(self.email_icon_loc)
        self.is_display(self.email_input_loc)
        self.is_display(self.code_icon_loc)
        self.is_display(self.code_input_loc)
        self.is_display(self.code_img_loc)
        self.is_display(self.sendLink_btn_loc)
        self.is_display(self.bottom_loc)

    # 获取用户名输入框默认文本
    def get_username_text(self):
        username_value = self.find_element(*self.username_input_loc).get_attribute('placeholder')
        return username_value

    # 获取邮箱输入框默认文本
    def get_email_text(self):
        email_value = self.find_element(*self.email_input_loc).get_attribute('placeholder')
        return email_value

    # 获取验证码输入框默认文本
    def get_code_text(self):
        code_value = self.find_element(*self.code_input_loc).get_attribute('placeholder')
        return code_value

    # 获取验证码图片地址
    def get_code_img_address(self):
        code_address = self.find_element(*self.code_img_loc).get_attribute('src')
        return code_address

    # 获取正确信息提交成功提示
    def get_correct_text(self):
        correct_text = self.find_element(*self.correct_loc).text
        return correct_text

    # 判断发送重置链接到邮箱按钮是否禁用
    def send_link_btn_is_enable(self):
        true_or_false = self.find_element(*self.sendLink_btn_loc).is_enabled()
        return true_or_false



