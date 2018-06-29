#######################################################
# FileName:HomePage.py
# Author:liketao and xiangdefu
# Date:2018-6-20
# Function Description: 封装home page页面的元素和操作
#######################################################

from selenium.webdriver.common.by import By
from Mobile_Testsuite.PO.BasePage import Element


# 继承Element类
class HomePage(Element):
    # 定位元素：通过元素属性定位home page页面中的元素

    # 顶栏标题
    title_loc = (By.XPATH, '//*[@id="header"]/header/h1')

    # 顶栏Logo图标
    toplogo_loc = (By.XPATH, '//*[@id="header"]/header/div[1]/button/label/img')

    # 语言切换按钮
    language_btn_loc = (By.XPATH, '//*[@id="header"]/header/div[2]/button/label')

    # 用户头像图标
    header_img_loc = (By.XPATH , '//*[@id="loginRegister"]/a/span[1]')

    # 登录/注册按钮
    register_btn_loc = (By.XPATH, '//*[@id="loginRegister"]/a/span[3]')

    # 玩家昵称
    nickname_loc = (By.XPATH , '//*[@id="loginRegister"]/a/span[2]')

    # 虚拟币（试玩币）

    ## 虚拟币图标
    currency_img_loc = (By.XPATH , '//*[@id="loginRegister"]/div/div/span[3]/img')

    ## 虚拟币金额
    currency_sum_loc = (By.XPATH , '//*[@id="loginRegister"]/div/div/span[2]/span/b[1]')

    ## 虚拟币切换按钮
    currency_change_btn_loc = (By.XPATH , '//*[@id="loginRegister"]/div/div/span[1]')

    # 公平说明banner图
    fairbanner_img_loc = (By.XPATH, '//*[@id="home"]/div[1]')

    fairbanner_textone_loc = (By.XPATH, '//*[@id="home"]/div[1]/p[1]')

    fairbanner_texttwo_loc = (By.XPATH , '//*[@id="home"]/div[1]/p[2]')

    # 加入官方群入口
    officialgroup_img_loc = (By.XPATH , '//*[@id="home"]/div[1]/a/img')

    officialgroup_btn_loc = (By.XPATH , '//*[@id="home"]/div[1]/a/span')

    # 百家乐游戏入口
    baccarat_img_loc = (By.XPATH , '//*[@id="home"]/div/div/a[1]/div/div[1]/img')

    baccarat_name_loc = (By.XPATH , '//*[@id="home"]/div/div/a[1]/div/div[2]/span')

    baccarat_btn_loc = (By.XPATH , '//*[@id="home"]/div/div/a[1]/div/div[2]/button')

    # 21点游戏入口
    blackjack_img_loc = (By.XPATH , '//*[@id="home"]/div/div/a[2]/div/div[1]/img')

    blackjack_name_loc = (By.XPATH , '//*[@id="home"]/div/div/a[2]/div/div[2]/span')

    blackjack_btn_loc = (By.XPATH , '//*[@id="home"]/div/div/a[2]/div/div[2]/button')

    # MD5公平性说明

    ## md5标题
    md5_img_loc = (By.XPATH , '//*[@id="home"]/div[2]')

    md5_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[1]')

    ## md5定义
    md5definition_img_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[2]/div[1]/img')

    md5definition_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[2]/div[2]')

    md5definition_text_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[2]/div[3]')

    ## 种子定义
    seeddefinition_img_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[3]/div[1]/img')

    seeddefinition_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[3]/div[2]')

    seeddefinition_text_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[3]/div[3]')

    ## 摘要定义
    digestdefinition_img_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[4]/div[1]/img')

    digestdefinition_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[4]/div[2]')

    digestdefinition_text_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[4]/div[3]')

    ## 偷不了牌
    unchangeorder_img_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[1]/div[1]/img')

    unchangeorder_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[1]/div[2]')

    unchangeorder_text_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[1]/div[3]')

    ## 换不了牌
    unchangecard_img_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[2]/div[1]/img')

    unchangecard_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[2]/div[2]')

    unchangecard_text_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[2]/div[3]')

    # 可验证的公平性

    ## 验证流程部分
    provablyfair_title_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[1]')

    provablyfair_img_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[2]/div[1]/img')

    provablyfair_firststep_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[2]/div[2]')

    provablyfair_secondstep_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[2]/div[4]')

    provablyfair_thirdstep_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[2]/div[3]')

    ## 验证例子
    example_seed_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[3]/div[1]/img')

    seed_introduce_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[3]/div[2]')

    example_arrow_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[3]/div[3]/img')

    example_digest_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[3]/div[4]/img')

    digest_introduce_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[3]/div[5]')

    ## 验证工具
    verify_tools_title_loc = (By.XPATH , '//*[@id="home"]/div[4]/div[1]')

    verify_tools_breatheimg_loc = (By.XPATH , '//*[@id="home"]/div[4]/div[2]/img')

    verify_tools_text_loc = (By.XPATH , '//*[@id="home"]/div[4]/div[3]')

    verify_adress_box_loc = (By.XPATH , '//*[@id="home"]/div[4]/div[4]')

    verify_adress_link_loc = (By.XPATH , '//*[@id="home"]/div[4]/div[4]/a[1]')

    # 网站特色
    webfeature_banner_img_loc = (By.XPATH , '//*[@id="home"]/div[5]')

    ## 非常快
    fast_img_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[1]/div[1]/img')

    fast_title_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[1]/div[2]')

    fast_text_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[1]/div[3]')

    ## 和隐秘
    privacy_img_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[2]/div[1]/img')

    privacy_title_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[2]/div[2]')

    privacy_text_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[2]/div[3]')

    ## 很安全
    safety_img_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[3]/div[1]/img')

    safety_title_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[3]/div[2]')

    safety_text_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[3]/div[3]')

    # 静态图标
    static_firstimg_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[1]/div[1]/img')

    static_secondimg_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[1]/div[2]')

    static_thirdimg_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[1]/div[3]')

    static_fourthimg_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[1]/div[4]')

    static_fifthimg_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[1]/div[5]')

    # 社交链接
    facebook_img_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[2]/a[1]/img')

    twitter_img_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[2]/a[2]/img')

    mailbox_img_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[2]/a[3]/img')

    qqgroup1_img_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[2]/a[4]/img')

    qqgroup2_img_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[2]/a[5]/img')

    # 页面底部logo图标
    bottom_logo_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[3]/img')

    # 底栏

    ## 首页
    homepage_img_loc = (By.XPATH , '//*[@id="footer"]/a[1]/div[1]/img')

    homepage_btn_loc = (By.XPATH , '//*[@id="footer"]/a[1]/div[2]/span')

    ## 记录
    record_img_loc = (By.XPATH , '//*[@id="footer"]/a[2]/div[1]/img')

    record_btn_loc = (By.XPATH , '//*[@id="footer"]/a[2]/div[2]/span')

    ## 账户
    accout_img_loc = (By.XPATH , '//*[@id="footer"]/a[3]/div[1]/img')

    accout_btn_loc = (By.XPATH , '//*[@id="footer"]/a[3]/div[2]/span')

    ## 我的
    mine_img_loc = (By.XPATH , '//*[@id="footer"]/a[4]/div[1]/img')

    mine_btn_loc = (By.XPATH , '//*[@id="footer"]/a[4]/div[2]/span')


    # 操作方法

    # 点击操作

    # 点击注册按钮
    def click_register_btn(self):
        self.click(self.register_btn_loc)

    # 点击昵称
    def click_nickname(self):
        self.click(self.nickname_loc)

    # 点击语言切换按钮
    def click_language_btn(self):
        self.click(self.language_btn_loc)

    # 点击虚拟币切换按钮
    def click_currency_change_btn(self):
        self.click(self.currency_change_btn_loc)

    # 点击百家乐游戏开始按钮
    def click_baccarat_btn(self):
        self.click(self.baccarat_btn_loc)

    # 点击21点游戏开始按钮
    def click_blackjack_btn(self):
        self.click(self.blackjack_btn_loc)

    # 点击第三验证地址（第一个链接)
    def click_verify_address_link(self):
        self.click(self.verify_adress_link_loc)

    # 点击社交链接（Facebook）
    def click_social_link(self):
        self.click(self.facebook_img_loc)

    # 获取文本操作

    # 获取标题的文本内容
    def get_title_text(self):
        result = self.find_element(*self.title_loc).text
        return result

    # 获取语言切换按钮的文本内容
    def get_language_btn_text(self):
        result = self.find_element(*self.language_btn_loc).text
        return result

    # 获取登录/注册按钮的文本内容
    def get_register_btn_text(self):
        result = self.find_element(*self.register_btn_loc).text
        return result

    # 获取顶栏虚拟币除去末尾零的金额数字
    def get_currency_amount(self):
        result = self.find_element(*self.currency_sum_loc).text
        return result

    # 获取公平说明banner图的文本内容
    def get_fairbanner_textone_text(self):
        result = self.find_element(*self.fairbanner_textone_loc).text
        return result

    def get_fairbanner_texttwo_text(self):
        result = self.find_element(*self.fairbanner_texttwo_loc).text
        return result

    # 获取加入官方群按钮的文本内容
    def get_officialgroup_btn_text(self):
        result = self.find_element(*self.officialgroup_btn_loc).text
        return result

    # 获取百家乐游戏名称的文本内容
    def get_baccarat_name_text(self):
        result = self.find_element(*self.baccarat_name_loc).text
        return result

    # 获取百家乐游戏开始按钮的文本内容
    def get_baccarat_btn_text(self):
        result = self.find_element(*self.baccarat_btn_loc).text
        return result

    # 获取21点游戏名称的文本内容
    def get_blackjack_name_text(self):
        result = self.find_element(*self.blackjack_name_loc).text
        return result

    # 获取21点游戏开始按钮的文本内容
    def get_blackjack_btn_text(self):
        result = self.find_element(*self.blackjack_btn_loc).text
        return result

    # 获取md5标题的文本内容
    def get_md5_title_text(self):
        result = self.find_element(*self.md5_title_loc).text
        return result

    # 获取md5定义标题的文本内容
    def get_md5definition_title_text(self):
        result = self.find_element(*self.md5definition_title_loc).text
        return result

    # 获取md5定义的文本内容
    def get_md5definition_text(self):
        result = self.find_element(*self.md5definition_text_loc).text
        return result

    # 获取种子定义标题的文本内容
    def get_seeddefinition_title_title_text(self):
        result = self.find_element(*self.seeddefinition_title_loc).text
        return result

    # 获取种子定义的文本内容
    def get_seeddefinition_text(self):
        result = self.find_element(*self.seeddefinition_text_loc).text
        return result

    # 获取摘要定义标题的文本内容
    def get_digestdefinition_title_text(self):
        result = self.find_element(*self.digestdefinition_title_loc).text
        return result

    # 获取摘要定义的文本内容
    def get_digestdefinition_text(self):
        result = self.find_element(*self.digestdefinition_text_loc).text
        return result

    # 获取偷不了牌标题的文本内容
    def get_unchangeorder_title_text(self):
        result = self.find_element(*self.unchangeorder_title_loc).text
        return result

    # 获取偷不了牌的文本内容
    def get_unchangeorder_text(self):
        result = self.find_element(*self.unchangeorder_text_loc).text
        return result

    # 获取换不了牌标题的文本内容
    def get_unchangeorder_title_text(self):
        result = self.find_element(*self.unchangecard_title_loc).text
        return result

    # 获取换不了牌的文本内容
    def get_unchangecard_text(self):
        result = self.find_element(*self.unchangecard_text_loc).text
        return result

    # 获取可验证公平性标题的文本内容
    def get_provablyfair_title_text(self):
        result = self.find_element(*self.provablyfair_title_loc).text
        return result

    # 获取可验证公平性第一步的文本内容
    def get_provablyfair_firststep_text(self):
        result = self.find_element(*self.provablyfair_firststep_loc).text
        return result

    # 获取可验证公平性第二步的文本内容
    def get_provablyfair_secondstep_text(self):
        result = self.find_element(*self.provablyfair_secondstep_loc).text
        return result

    # 获取可验证公平性第三步的文本内容
    def get_provablyfair_thirdstep_text(self):
        result = self.find_element(*self.provablyfair_thirdstep_loc).text
        return result

    # 获取种子说明的文本内容
    def get_seed_introduce_text(self):
        result = self.find_element(*self.seed_introduce_loc).text
        return result

    # 获取摘要说明的文本内容
    def get_digest_introduce_text(self):
        result = self.find_element(*self.digest_introduce_loc).text
        return result

    # 获取第三方验证工具标题的文本内容
    def get_verify_tools_title_text(self):
        result = self.find_element(*self.verify_tools_title_loc).text
        return result

    # 获取第三方验证工具说明的文本内容
    def get_verify_tools_text(self):
        result = self.find_element(*self.verify_tools_text_loc).text
        return result

    # 获取网站特色非常快标题的文本内容
    def get_fast_title_text(self):
        result = self.find_element(*self.fast_title_loc).text
        return result

    # 获取网站特色非常快说明的文本内容
    def get_fast_text(self):
        result = self.find_element(*self.fast_text_loc).text
        return result

    # 获取网站特色很隐秘标题的文本内容
    def get_privacy_title_text(self):
        result = self.find_element(*self.privacy_title_loc).text
        return result

    # 获取网站特色很隐秘说明的文本内容
    def get_privacy_text(self):
        result = self.find_element(*self.privacy_text_loc).text
        return result

    # 获取网站特色很安全标题的文本内容
    def get_safety_title_text(self):
        result = self.find_element(*self.safety_title_loc).text
        return result

    # 获取网站特色很安全说明的文本内容
    def get_safety_text(self):
        result = self.find_element(*self.safety_text_loc).text
        return result








