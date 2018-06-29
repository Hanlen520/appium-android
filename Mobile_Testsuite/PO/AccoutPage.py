#######################################################
# FileName:AccoutPage.py
# Author:xiangdefu
# Date:2018-6-28
# Function Description: 封装accout page页面的元素和操作
#######################################################

from selenium.webdriver.common.by import By
from Mobile_Testsuite.PO.BasePage import Element


# 继承Element类
class AccoutPage(Element):
    # 定位元素：通过元素属性定位accout page页面中的元素

    # 顶栏标题
    title_loc = (By.XPATH, '//*[@id="header"]/header/h1')

    # 顶栏Logo图标
    toplogo_loc = (By.XPATH, '//*[@id="header"]/header/div[1]/button/label/img')

    # 用户头像图标
    header_img_loc = (By.XPATH, '//*[@id="loginRegister"]/a/span[1]')

    # 玩家昵称
    nickname_loc = (By.XPATH, '//*[@id="loginRegister"]/a/span[2]')

    # 虚拟币（试玩币）

    # 虚拟币图标
    currency_img_loc = (By.XPATH, '//*[@id="loginRegister"]/div/div/span[3]/img')

    # 虚拟币金额
    currency_sum_loc = (By.XPATH, '//*[@id="loginRegister"]/div/div/span[2]/span/b[1]')

    # 虚拟币切换按钮
    currency_change_btn_loc = (By.XPATH, '//*[@id="loginRegister"]/div/div/span[1]')

    # ETH虚拟币信息

    # ETH图标
    eth_img_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[1]/div[1]/div[1]/img')

    # ETH名称
    eth_name_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[1]/div[1]/div[2]/div[1]')

    # ETH余额
    eth_balance_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[1]/div[1]/div[2]/div[2]')

    # ETH金额
    eth_sum_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[1]/div[1]/div[2]/div[2]/span/b[1]')

    # ETH转入按钮
    eth_deposit_btn_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[1]/div[2]/a[1]')

    # ETH转出按钮
    eth_withdraw_btn_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[1]/div[2]/a[2]')

    # BTC图标
    btc_img_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[2]/div[1]/div[1]/img')

    # BTC名称
    btc_name_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[2]/div[1]/div[2]/div[1]')

    # BTC余额
    btc_balance_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[2]/div[1]/div[2]/div[2]')

    # BTC金额
    btc_sum_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[2]/div[1]/div[2]/div[2]/span/b[1]')

    # BTC转入按钮
    btc_deposit_btn_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[2]/div[2]/a[1]')

    # BTC转出按钮
    btc_withdraw_btn_loc = (By.XPATH, '//*[@id="body_main"]/div/div[8]/div/ul/li[2]/div[2]/a[2]')

    # 转入页面 (ETH虚拟币的转入页面）

    # 转入页面标题
    deposit_title_loc = (By.XPATH, '//*[@id="header"]/header/h1')

    # 转入说明
    deposit_introduction_loc = (By.XPATH, '//*[@id="transferin_vue"]/div/div[1]')

    # 转入页面ETH图标
    deposit_ethimg_loc = (By.XPATH, '//*[@id="transferin_vue"]/div/div[2]/div[1]/div[1]/img')

    # 转入页面ETH名称
    deposit_ethname_loc = (By.XPATH, '//*[@id="transferin_vue"]/div/div[2]/div[1]/div[2]/div[1]')

    # 转入页面ETH余额
    deposit_ethbalance_loc = (By.XPATH, '//*[@id="transferin_vue"]/div/div[2]/div[1]/div[2]/div[2]')

    # 转入页面ETH金额
    deposit_ethsum_loc = (By.XPATH, '//*[@id="transferin_vue"]/div/div[2]/div[1]/div[2]/div[2]/span/b[1]')

    # 转入地址
    deposit_address_loc = (By.XPATH, '//*[@id="copy_input"]')

    # 转入地址复制按钮
    deposit_copy_btn_loc = (By.XPATH, '//*[@id="transferin_vue"]/div/div[2]/div[2]/div/button')

    # 转入地址二维码
    deposit_quickmark_loc = (By.XPATH, '//*[@id="qrcode"]/img')

    # 转入地址二维码说明
    deposit_quickmark_intr_loc = (By.XPATH, '//*[@id="transferin_vue"]/div/div[2]/div[2]/div/p')

    # 转出页面 (ETH虚拟币的转出页面）

    # 转出页面标题
    withdraw_title_loc = (By.XPATH, '//*[@id="header"]/header/h1')

    # 转出说明
    withdraw_introduction_loc = (By.XPATH, '//*[@id="transferout_vue"]/div/div[1]')

    # 转出地址标题
    withdraw_address_title_loc = (By.XPATH, '//*[@id="transferout_vue"]/div/form/div/div[1]/label')

    # 转出地址输入框
    withdraw_address_box_loc = (By.XPATH, '//*[@id="transferout_address"]')

    # 转出数额标题
    withdraw_amount_title_loc = (By.XPATH, '//*[@id="transferout_vue"]/div/form/div/div[2]/label')

    # 转出数额输入框
    withdraw_amount_box_loc = (By.XPATH, '//*[@id="crashshow"]')

    # 最低转出说明
    withdraw_minsum_loc = (By.XPATH, '//*[@id="transferout_vue"]/div/form/div/div[3]')

    # 转出手续费标题
    withdraw_charge_title_loc = (By.XPATH, '//*[@id="transfer_fees_show_label"]')

    # 转出手续费输入框
    withdraw_charge_box_loc = (By.XPATH, '//*[@id="transfer_fees_show"]')

    # 转出按钮
    withdraw_btn_loc = (By.XPATH, '//*[@id="transferout_vue"]/div/div[2]/button')

    # 操作方法

    # 点击操作

    # 点击注册按钮
    def click_register_btn(self):
        self.click(self.register_btn_loc)

    # 点击昵称
    def click_nickname(self):
        self.click(self.nickname_loc)

    # 点击虚拟币切换按钮
    def click_currency_change_btn(self):
        self.click(self.currency_change_btn_loc)

    # 点击转入按钮
    def click_deposit_btn(self):
        self.click(self.eth_deposit_btn_loc)

    # 点击转出按钮
    def click_withdraw_btn(self):
        self.click(self.eth_withdraw_btn_loc)

    # 点击转入页面复制按钮
    def click_deposit_copy_btn(self):
        self.click(self.deposit_copy_btn_loc)

    # 点击转出页面转出按钮
    def click_withdrwa_deposit_btn(self):
        self.click(self.withdraw_btn_loc)

    # 转出页面，转出地址输入框输入信息
    def send_key_withdraw_address(self):
        self.send_key(self.withdraw_address_box_loc)

    # 转出页面，转出数额输入框输入信息
    def send_key_withdraw_amount(self):
        self.send_key(self.withdraw_amount_box_loc)

    # 转出页面，手续费输入框输入信息
    def send_key_withdraw_charge(self):
        self.send_key(self.withdraw_charge_box_loc)

    # 获取文本操作

    # 账户页面，获取标题的文本内容
    def get_title_text(self):
        result = self.find_element(*self.title_loc).text
        return result

    # 账户页面，获取顶栏虚拟币除去末尾零的金额数字
    def get_currency_amount(self):
        result = self.find_element(*self.currency_sum_loc).text
        return result

    # 账户页面，获取ETH名称的文本内容
    def get_eth_name_text(self):
        result = self.find_element(*self.eth_name_loc).text
        return result

    # 账户页面，获取ETH余额的文本内容
    def get_eth_balance_text(self):
        result = self.find_element(*self.eth_balance_loc).text
        return result

    # 账户页面，获取ETH除去末尾零的金额数字
    def get_eth_amount(self):
        result = self.find_element(*self.eth_sum_loc).text
        return result

    # 账户页面，获取ETH币转入按钮文本内容
    def get_eth_deposit_btn_text(self):
        result = self.find_element(*self.eth_deposit_btn_loc).text
        return result

    # 账户页面，获取ETH币转出按钮文本内容
    def get_eth_withdraw_btn_text(self):
        result = self.find_element(*self.eth_withdraw_btn_loc).text
        return result

    # 账户页面，获取BTC名称的文本内容
    def get_btc_name_text(self):
        result = self.find_element(*self.btc_name_loc).text
        return result

    # 账户页面，获取BTC余额的文本内容
    def get_btc_balance_text(self):
        result = self.find_element(*self.btc_balance_loc).text
        return result

    # 账户页面，获取BTC除去末尾零的金额数字
    def get_btc_amount(self):
        result = self.find_element(*self.btc_sum_loc).text
        return result

    # 账户页面，获取BTC币转入按钮文本内容
    def get_btc_deposit_btn_text(self):
        result = self.find_element(*self.btc_deposit_btn_loc).text
        return result

    # 账户页面，获取BTC币转出按钮文本内容
    def get_btc_withdraw_btn_text(self):
        result = self.find_element(*self.btc_withdraw_btn_loc).text
        return result

    # 转入页面，获取页面标题的文本内容
    def get_deposit_title_text(self):
        result = self.find_element(*self.deposit_title_loc).text
        return result

    # 转入页面，获取ETH名称的文本内容
    def get_deposit_ethname_text(self):
        result = self.find_element(*self.deposit_ethname_loc).text
        return result

    # 转入页面，获取ETH余额的文本内容
    def get_deposit_ethbalance_text(self):
        result = self.find_element(*self.deposit_ethbalance_loc).text
        return result

    # 转入页面，获取ETH除去末尾零的金额数字
    def get_deposit_eth_amount(self):
        result = self.find_element(*self.deposit_ethsum_loc).text
        return result

    # 转入页面，获取转入说明的文本内容
    def get_deposit_introduction_text(self):
        result = self.find_element(*self.deposit_introduction_loc).text
        return result

    # 转入页面，获取二维码说明的文本内容
    def get_deposit_quickmark_intr_text(self):
        result = self.find_element(*self.deposit_quickmark_intr_loc).text
        return result

    # 转出页面，获取页面标题的文本内容
    def get_withdraw_title_text(self):
        result = self.find_element(*self.withdraw_title_loc).text
        return result

    # 转出页面，获取转出说明的文本内容
    def get_withdraw_introduction_text(self):
        result = self.find_element(*self.withdraw_introduction_loc).text
        return result

    # 转出页面，获取转出地址标题的文本内容
    def get_withdraw_address_title_text(self):
        result = self.find_element(*self.withdraw_address_title_loc).text
        return result

    # 转出页面，获取转出地址输入框的文本内容
    def get_withdraw_address_box_text(self):
        result = self.find_element(*self.withdraw_address_box_loc).text
        return result

    # 转出页面，获取转出数额标题的文本内容
    def get_withdraw_amount_title_text(self):
        result = self.find_element(*self.withdraw_amount_title_loc).text
        return result

    # 转出页面，获取转出数额输入框的文本内容
    def get_withdraw_amount_box_text(self):
        result = self.find_element(*self.withdraw_amount_box_loc).text
        return result

    # 转出页面，获取最低转出说明的文本内容
    def get_withdraw_minsum_loc_text(self):
        result = self.find_element(*self.withdraw_minsum_loc).text
        return result

    # 转出页面，获取转出手续费标题的文本内容
    def get_withdraw_charge_title_text(self):
        result = self.find_element(*self.withdraw_charge_title_loc).text
        return result
