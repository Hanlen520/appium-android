#######################################################
# FileName:LanPage.py
# Author:wang xiaoxiao
# Date:2018-6-28
# Function Description: 封装language page页面的元素和操作
#######################################################

from selenium.webdriver.common.by import By
from Mobile_Testsuite.PO.BasePage import Element


# 继承Element类
class LANGPwPage(Element):
    # 定位元素：通过元素属性定位language page页面中的元素

    # Logo图标
    logo_loc = (By.XPATH, '//*[@id="header"]/header/div[1]/button/label/img')

    # 顶栏标题--设置语言
    title_loc = (By.XPATH, '//*[@id="header"]/header/h1')

    # 简体中文
    Chinese_loc = (By.ID, '//*[@id="setlanguage"]/ul/li[1]/a')

    # 英语
    English_loc = (By.XPATH, '//*[@id="setlanguage"]/ul/li[2]/a')

    # 繁体中文
    Chinese_HK_loc = (By.ID, '//*[@id="setlanguage"]/ul/li[3]/a')

    # 取消按钮
    cancel_btn_loc = (By.XPATH, '//*[@id="setlanguage"]/div/div[1]')

    # 确认按钮
    confirm_btn_loc = (By.XPATH, '//*[@id="setlanguage"]/div/div[2]')

    # 底栏
    bottom_loc = (By.ID, 'footer')

    # 操作方法

    # 点击取消按钮
    def click_cancel_btn(self):
        self.click(self.cancel_btn_loc)

    # 点击确认按钮
    def click_code_img(self):
        self.click(self.confirm_btn_loc)

    # 点击简体中文
    def click_chinese(self):
        self.click(self.Chinese_loc)

    # 点击英语
    def click_english(self):
        self.click(self.English_loc)

    # 点击繁体中文
    def click_chinese_hk(self):
        self.click(self.Chinese_HK_loc)

    # 登录页面元素是否显示
    def forgot_password_element_is_display(self):
        self.is_display(self.logo_loc)
        self.is_display(self.title_loc)
        self.is_display(self.Chinese_loc)
        self.is_display(self.English_loc)
        self.is_display(self.Chinese_HK_loc)
        self.is_display(self.cancel_btn_loc)
        self.is_display(self.confirm_btn_loc)
        self.is_display(self.bottom_loc)

    # 获取页面标题
    def get_title_text(self):
        title_text = self.find_element(*self.title_loc).text
        return title_text

    # 判断简体中文是否被选中
    def chinese_is_selected(self):
        is_or_not = self.find_element(*self.Chinese_loc).is_selected()
        return is_or_not

    # 判断英语是否被选中
    def english_is_selected(self):
        is_or_not = self.find_element(*self.English_loc).is_selected()
        return is_or_not

    # 判断繁体中文是否被选中
    def chinese_hk_is_selected(self):
        is_or_not = self.find_element(*self.Chinese_HK_loc).is_selected()
        return is_or_not