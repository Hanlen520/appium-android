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


   # 获取所有文本内容
    def get_all_text(self):

        # 所有文本的需求值列表

        truthelement = ['账户','ETH','余额：','转入','转出','BTC']

        # 获取页面所有文本
        title_text = self.find_element(*self.title_loc).text
        eth_name_text = self.find_element(*self.eth_name_loc).text
        eth_balance_text = self.find_element(*self.eth_balance_loc).text
        eth_deposit_btn_text = self.find_element(*self.eth_deposit_btn_loc).text
        eth_withdraw_btn_text = self.find_element(*self.eth_withdraw_btn_loc).text
        btc_name_text = self.find_element(*self.btc_name_loc).text
        btc_balance_text = self.find_element(*self.btc_balance_loc).text
        btc_deposit_btn_text = self.find_element(*self.btc_deposit_btn_loc).text
        btc_withdraw_btn_text = self.find_element(*self.btc_withdraw_btn_loc).text

        # 页面所有文本值列表

        getelement = [title_text,eth_name_text,eth_balance_text,eth_deposit_btn_text,
                      eth_withdraw_btn_text,btc_name_text,btc_balance_text,btc_deposit_btn_text,
                      btc_withdraw_btn_text]

        correctvalue = []
        errorvalue = []
        i = 0
        while (i < 9):
            result = getelement[i]
            if (result in truthelement):
                correctvalue.append(result)
            else:
                errorvalue.append(result)
            i = i + 1


  # 账户页面元素是否显示
    def accoutpage_element_is_display(self):
        self.is_display(self.toplogo_loc)
        self.is_display(self.header_img_loc)
        self.is_display(self.nickname_loc)
        self.is_display(self.currency_img_loc)
        self.is_display(self.currency_sum_loc)
        self.is_display(self.eth_img_loc)
        self.is_display(self.eth_sum_loc)
        self.is_display(self.btc_img_loc)
        self.is_display(self.btc_sum_loc)



class DepositPage(AccoutPage):
    # 转入页面 (ETH虚拟币的转入页面）

    # 转入页面标题
    deposit_title_loc = (By.XPATH, '//*[@id="header"]/header/h1')

    # 转入说明注释图标
    deposit_introduction_img_loc = (By.XPATH , '//*[@id="transferin_vue"]/div/div[1]/i')

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

    # 操作方法

    # 点击操作

    # 点击转入页面复制按钮
    def click_deposit_copy_btn(self):
        self.click(self.deposit_copy_btn_loc)

   # 获取所有文本内容
    def get_all_text(self):

        # 所有文本的需求值列表

        truthelement = ['转入','ETH','余额：','本平台限制最小转入小数点后8位的数额，否则无法正常转入。',
                        '扫描二维码获取转入地址','复制']

        # 获取页面所有文本

        deposit_title_text = self.find_element(*self.deposit_title_loc).text
        deposit_ethname_text = self.find_element(*self.deposit_ethname_loc).text
        deposit_ethbalance_text = self.find_element(*self.deposit_ethbalance_loc).text
        deposit_introduction_text = self.find_element(*self.deposit_introduction_loc).text
        deposit_quickmark_intr_text = self.find_element(*self.deposit_quickmark_intr_loc).text
        deposit_copy_btn_text = self.find_element(*self.deposit_copy_btn_loc).text

        # 页面所有文本值列表

        getelement = [deposit_title_text,deposit_ethname_text,deposit_ethbalance_text,
                      deposit_introduction_text,deposit_quickmark_intr_text,deposit_copy_btn_text]

        correctvalue = []
        errorvalue = []
        i = 0
        while (i < 6):
            result = getelement[i]
            if (result in truthelement):
                correctvalue.append(result)
            else:
                errorvalue.append(result)
            i = i + 1


  # 转入页面元素是否显示
    def accoutpage_element_is_display(self):
        self.is_display(self.toplogo_loc)
        self.is_display(self.header_img_loc)
        self.is_display(self.nickname_loc)
        self.is_display(self.currency_img_loc)
        self.is_display(self.currency_sum_loc)
        self.is_display(self.deposit_introduction_img_loc)
        self.is_display(self.deposit_ethimg_loc)
        self.is_display(self.deposit_ethsum_loc)
        self.is_display(self.deposit_address_loc)
        self.is_display(self.deposit_quickmark_loc)


class WithdrawPage(AccoutPage):
    # 转出页面 (ETH虚拟币的转出页面）

    # 转出页面标题
    withdraw_title_loc = (By.XPATH, '//*[@id="header"]/header/h1')

    # 转出说明注释图标
    withdraw_introduction_img_loc = (By.XPATH , '//*[@id="transferout_vue"]/div/div[1]/i')

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

    # 点击转出页面转出按钮
    def click_withdrwa_deposit_btn(self):
        self.click(self.withdraw_btn_loc)

    # 输入操作

    # 转出页面，转出地址输入框输入信息
    def send_withdraw_address(self):
        self.send_key(self.withdraw_address_box_loc)

    # 转出页面，转出数额输入框输入信息
    def send_withdraw_amount(self):
        self.send_key(self.withdraw_amount_box_loc)

    # 转出页面，手续费输入框输入信息
    def send_withdraw_charge(self):
        self.send_key(self.withdraw_charge_box_loc)

    # 获取文本操作

   # 获取所有文本内容
    def get_all_text(self):

        # 所有文本的需求值列表

        truthelement = ['转出','单笔转出不论数额大小，均会消耗矿工费，转出时间通常为30分钟至3个小时，'
                        '提高矿工费能加快确认速度。申请之前请确认转出地址正确，'
                        '交易一旦发送到区块链网络便不可撤回。',
                        '转出地址','请输入转出地址','转出数额','请输入转出数额','最低转出0.0000001','手续费']

        # 获取页面所有文本

        withdraw_title_text = self.find_element(*self.withdraw_title_loc).text
        withdraw_introduction_text = self.find_element(*self.withdraw_introduction_loc).text
        withdraw_address_title_text = self.find_element(*self.withdraw_address_title_loc).text
        withdraw_address_box_text = self.find_element(*self.withdraw_address_box_loc).get_attribute('placeholder')
        withdraw_amount_title_text = self.find_element(*self.withdraw_amount_title_loc).text
        withdraw_amount_box_text = self.find_element(*self.withdraw_amount_box_loc).get_attribute('placeholder')
        withdraw_minsum_instr_text = self.find_element(*self.withdraw_minsum_loc).text
        withdraw_charge_title_text = self.find_element(*self.withdraw_charge_title_loc).text

        # 页面所有文本值列表

        getelement = [withdraw_title_text,withdraw_introduction_text,withdraw_address_title_text,
                      withdraw_address_box_text,withdraw_amount_title_text,withdraw_amount_box_text,
                      withdraw_minsum_instr_text,withdraw_charge_title_text]

        correctvalue = []
        errorvalue = []
        i = 0
        while (i < 8):
            result = getelement[i]
            if (result in truthelement):
                correctvalue.append(result)
            else:
                errorvalue.append(result)
            i = i + 1



  # 转出页面元素是否显示
    def accoutpage_element_is_display(self):
        self.is_display(self.toplogo_loc)
        self.is_display(self.header_img_loc)
        self.is_display(self.nickname_loc)
        self.is_display(self.currency_img_loc)
        self.is_display(self.currency_sum_loc)
        self.is_display(self.withdraw_introduction_img_loc)

 # 判断转出按钮是否禁用
    def withdraw_btn_enable(self):
        false = self.find_element(*self.withdraw_btn_loc).is_enabled()
        return false