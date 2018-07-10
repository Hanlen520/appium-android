#######################################################
# FileName:HomePage.py
# Author:jianglei
# Date:2018-7-6
# Function Description: 封装 Minepage页面的元素和操作
#######################################################


from selenium.webdriver.common.by import By
from Mobile_Testsuite.PO.BasePage import Element

# 继承Element类
class MinePage(Element):
    # 我的界面入口
    mine_interface = (By.XPATH, '//*[@id="footer"]/a[4]')
    # 顶栏标题
    title_text = (By.XPATH, '//*[@id="header"]/header/h1')
    #玩家昵称
    player_nickname=(By.XPATH, '//*[@id="loginRegister"]/a/span[2]')
    # 修改昵称按钮
    modified_nickname_btn = (By.XPATH, '//*[@id="mine"]/div[1]/a[1]/div[1]')
    # 修改昵称顶栏标题
    modifiedNicknameTittle_text = (By.XPATH, '//*[@id="header"]/header/h1')
    #昵称输入框
    input_box=(By.XPATH, '//*[@id="body_main"]/div/div[7]/div/div/form/div[1]/input')
    #昵称清空按钮
    clear_btn=(By.XPATH, '//*[@id="body_main"]/div/div[7]/div/div/form/div[1]/span/i')
    # 修改昵称确认按钮
    modifiedNicknameConfirm_btn = (By.XPATH, '//*[@id="body_main"]/div/div[7]/div/div/form/button')
    # 修改密码按钮
    modified_password_btn = (By.XPATH, '//*[@id="mine"]/div[1]/a[2]/div[1]')
    # 修改密码界面标题
    modifiedPasswordTittle_text = (By.XPATH, '//*[@id="header"]/header/h1')
    # 邮箱输入框
    email_input_box = (By.XPATH, '//*[@id="changePass"]/div/form/div/div[1]/input')
    # 验证码输入框
    assertCode_input_box = (By.XPATH, '//*[@id="changePass"]/div/form/div/div[2]/input')
    # 修改密码确认按钮
    modifiedPassword_btn = (By.XPATH, '//*[@id="changePass"]/div/form/div/div[2]/input')
   # 公平说明按钮
    provably_fair_btn = (By.XPATH, '//*[@id="mine"]/div[2]/a[1]/div[2]/div')
    # 公平界面顶栏标题
    fairTittle_text = (By.XPATH, '//*[@id="header"]/header/h1')
    # 常见问题
    faq_btn = (By.XPATH, '//*[@id="mine"]/div[2]/a[2]/div[2]/div')
    # 常见问题顶栏标题
    faqTittle_text = (By.XPATH, '//*[@id="header"]/header/h1')
    # 服务条款
    service_term_btn = (By.XPATH, '//*[@id="mine"]/div[2]/a[3]/div[2]/div')
    # 服务条款顶栏标题
    serviceTittle_text = (By.XPATH, '//*[@id="header"]/header/h1')
    # 关于我们
    about_us_btn = (By.XPATH, '//*[@id="mine"]/div[2]/a[4]/div[2]/div')
    # 关于我们顶栏标题
    aboutUsTittle_text = (By.XPATH, '//*[@id="header"]/header/h1')
    # 退出登录
    logout_btn = (By.XPATH, '//*[@id="mine"]/div[3]/a')
# 操作方法
    # 点击我的按钮
    def click_mine_interface(self):
        self.click(self.mine_interface)
    # 点击修改昵称按钮
    def click_modified_nickname_btn(self):
        self.click(self.modified_nickname_btn)
    # 点击清除按钮
    def click_clear_btn(self):
        self.click(self.clear_btn)
    # 点击昵称输入框
    def click_input_box(self):
        self.click(self.input_box)
    # 点击修改昵称确认按钮
    def click_modifiedNicknameConfirm_btn(self):
        self.click(self.modifiedNicknameConfirm_btn)
    #点击玩家昵称
    def click_nickname_btn(self):
        self.click(self.player_nickname)
    # 点击修改密码按钮
    def click_modified_password_btn(self):
        self.click(self.modified_password_btn)
    # 点击邮箱输入框
    def click_email_input_box(self):
        self.click(self.email_input_box)
    # 点击验证码输入框
    def click_assertCode_input_box(self):
        self.click(self.assertCode_input_box)
    # 点击修改密码确认按钮
    def click_modifiedPassword_btn(self):
        self.click(self.modifiedPassword_btn)
    # 点击公平说明按钮
    def click_provably_fair_btn(self):
        self.click(self.provably_fair_btn)
    # 点击常见问题按钮
    def click_faq_btn(self):
        self.click(self.faq_btn)
    # 点击服务条款按钮
    def click_service_term(self):
        self.click(self.service_term_btn)
    # 点击关于我们按钮
    def click_about_us_btn(self):
        self.click(self.about_us_btn)
    # 点击退出按钮
    def click_logout_btn(self):
        self.click(self.logout_btn)
# 获取标题的文本内容
    # 获取我的界面的顶栏标题
    def get_title_text(self):
        title_text = self.find_element(*self.title_text).text
        return title_text
     # 获取修改昵称按钮文本
    def get_modifiedNicknameTittle_text(self):
        modifiedNicknameTittle_text = self.find_element(*self.modifiedNicknameTittle_text).text
        return modifiedNicknameTittle_text
        # 获取修改昵称界面顶栏标题
    def get_inputBOX_text(self):
        input_text=self.find_element(*self.input_box).text
        return input_text
    def get_modified_nickname_text(self):
        modified_nickname_text = self.find_element(*self.modified_nickname_btn).text
        return modified_nickname_text
    #获取修改密码按钮文本
    def get_modifiedPassword_text(self):
        modifiedPassword_text = self.find_element(*self.modified_password_btn).text
        return modifiedPassword_text
    # 获取修改密码界面标题
    def get_modifiedPasswordTittle_text(self):
        modifiedPasswordTittle_text = self.find_element(*self.modifiedPasswordTittle_text).text
        return modifiedPasswordTittle_text
    # 公平界面顶栏标题
    def get_fairTittle_text(self):
        fairTittle_text = self.find_element(*self.fairTittle_text).text
        return fairTittle_text
    # 获取常见问题顶栏标题
    def get_faqTittle_text(self):
        faqTittle_text = self.find_element(*self.faqTittle_text).text
        return faqTittle_text
    # 获取服务条款顶栏标题
    def get_serviceTittle_text(self):
        serviceTittle_text = self.find_element(*self.serviceTittle_text).text
        return serviceTittle_text
    # 获取关于我们界面标题
    def get_aboutUsTittle_text(self):
        about_us_tittle_text = self.find_element(*self.aboutUsTittle_text).text
        return about_us_tittle_text
    #获取退出登录文本
    def get_logout_text(self):
        logout_text=self.find_element(*self.logout_btn).text
        return logout_text