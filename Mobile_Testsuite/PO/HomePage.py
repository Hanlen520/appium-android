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

    # 虚拟币图标
    currency_img_loc = (By.XPATH , '//*[@id="loginRegister"]/div/div/span[3]/img')

    # 虚拟币金额
    currency_sum_loc = (By.XPATH , '//*[@id="loginRegister"]/div/div/span[2]/span/b[1]')

    # 虚拟币切换按钮
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

    # md5标题
    md5_img_loc = (By.XPATH , '//*[@id="home"]/div[2]')

    md5_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[1]')

    # md5定义
    md5definition_img_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[2]/div[1]/img')

    md5definition_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[2]/div[2]')

    md5definition_text_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[2]/div[3]')

    # 种子定义
    seeddefinition_img_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[3]/div[1]/img')

    seeddefinition_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[3]/div[2]')

    seeddefinition_text_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[3]/div[3]')

    # 摘要定义
    digestdefinition_img_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[4]/div[1]/img')

    digestdefinition_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[4]/div[2]')

    digestdefinition_text_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[4]/div[3]')

    # 偷不了牌
    unchangeorder_img_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[1]/div[1]/img')

    unchangeorder_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[1]/div[2]')

    unchangeorder_text_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[1]/div[3]')

    # 换不了牌
    unchangecard_img_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[2]/div[1]/img')

    unchangecard_title_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[2]/div[2]')

    unchangecard_text_loc = (By.XPATH , '//*[@id="home"]/div[2]/div[5]/div[2]/div[3]')

    # 可验证的公平性

    # 验证流程部分
    provablyfair_title_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[1]')

    provablyfair_img_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[2]/div[1]/img')

    provablyfair_firststep_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[2]/div[2]')

    provablyfair_secondstep_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[2]/div[4]')

    provablyfair_thirdstep_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[2]/div[3]')

    # 验证例子
    example_seed_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[3]/div[1]/img')

    seed_introduce_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[3]/div[2]')

    example_arrow_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[3]/div[3]/img')

    example_digest_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[3]/div[4]/img')

    digest_introduce_loc = (By.XPATH , '//*[@id="home"]/div[3]/div[3]/div[5]')

    # 验证工具
    verify_tools_title_loc = (By.XPATH , '//*[@id="home"]/div[4]/div[1]')

    verify_tools_breatheimg_loc = (By.XPATH , '//*[@id="home"]/div[4]/div[2]/img')

    verify_tools_text_loc = (By.XPATH , '//*[@id="home"]/div[4]/div[3]')

    verify_adress_box_loc = (By.XPATH , '//*[@id="home"]/div[4]/div[4]')

    verify_adress_link_loc = (By.XPATH , '//*[@id="home"]/div[4]/div[4]/a[1]')

    # 网站特色
    webfeature_banner_img_loc = (By.XPATH , '//*[@id="home"]/div[5]')

    # 非常快
    fast_img_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[1]/div[1]/img')

    fast_title_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[1]/div[2]')

    fast_text_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[1]/div[3]')

    # 和隐秘
    privacy_img_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[2]/div[1]/img')

    privacy_title_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[2]/div[2]')

    privacy_text_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[2]/div[3]')

    # 很安全
    safety_img_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[3]/div[1]/img')

    safety_title_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[3]/div[2]')

    safety_text_loc = (By.XPATH , '//*[@id="home"]/div[5]/div[3]/div[3]')

    # 静态图标
    static_firstimg_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[1]/div[1]/img')

    static_secondimg_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[1]/div[2]/img')

    static_thirdimg_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[1]/div[3]/img')

    static_fourthimg_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[1]/div[4]/img')

    static_fifthimg_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[1]/div[5]/img')

    # 社交链接
    facebook_img_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[2]/a[1]/img')

    twitter_img_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[2]/a[2]/img')

    mailbox_img_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[2]/a[3]/img')

    qqgroup1_img_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[2]/a[4]/img')

    qqgroup2_img_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[2]/a[5]/img')

    # 页面底部logo图标
    bottom_logo_loc = (By.XPATH , '//*[@id="home"]/div[6]/div[3]/img')

    # 底栏

    # 首页
    homepage_img_loc = (By.XPATH , '//*[@id="footer"]/a[1]/div[1]/img')

    homepage_btn_loc = (By.XPATH , '//*[@id="footer"]/a[1]/div[2]/span')

    # 记录
    record_img_loc = (By.XPATH , '//*[@id="footer"]/a[2]/div[1]/img')

    record_btn_loc = (By.XPATH , '//*[@id="footer"]/a[2]/div[2]/span')

    # 账户
    accout_img_loc = (By.XPATH , '//*[@id="footer"]/a[3]/div[1]/img')

    accout_btn_loc = (By.XPATH , '//*[@id="footer"]/a[3]/div[2]/span')

    # 我的
    mine_img_loc = (By.XPATH , '//*[@id="footer"]/a[4]/div[1]/img')

    mine_btn_loc = (By.XPATH , '//*[@id="footer"]/a[4]/div[2]/span')

    # 操作方法

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

    # 点击账户按钮
    def click_account_btn(self):
        self.click(self.accout_btn_loc)

    # 获取文本操作

    # 获取所有文本内容
    def get_all_text(self):

        # 所有文本的需求值列表

        truthelement = ['首页','简体中文','登录/注册','最有趣的百家乐','可验证的区块链游戏系统','加入官方群>',
                        '百家乐','开始','21点','开始','防篡改的MD5加密确保游戏公平','什么是MD5？',
                        'MD5是一种广泛使用的加密算法，用于确保信息传输完整一致。它能将一段字符加密运算成另一段字符，'
                        '这两段字符具备不可篡改的对应性。（维基百科）','什么是种子？',
                        '“种子”就是未加密的字符，它包含了牌的花色与点数信息，系统会在亮牌后公布给所有玩家。',
                        '什么是摘要？','“摘要”就是将“种子”加密后的字符，在下注前便会显示给玩家。'
                        '亮牌后玩家便可利用MD5工具验证“摘要”与“种子”是否吻合。','偷不了牌！',
                        '游戏开始前我们将公布所有牌的“序号”和“摘要”，游戏按照序号顺序进行发牌，'
                        '序号和摘要具备唯一对应关系，一旦开始任何人无法改变发牌顺序！','换不了牌！',
                        '牌的花色与点数由“种子”决定，一个种子通过MD5加密算法只能生成一个“摘要”，'
                        '这意味着摘要一旦公布，任何人都无法篡改游戏结果的“种子”。','可验证的公平性',
                        '1，下注前获得全部牌的“序号”与“摘要”。','2，亮牌后得到牌的“种子”。',
                        '3，利用MD5工具验证“摘要”与“种子”是否吻合。',
                        '种子由随机字符组成，前两个字符决定了牌的点数与花色，第一位数字1代表A,2-9代表2-9点，T代表10点，'
                        '第二位的字母S、H、D、C分别代表黑桃、红桃、方块和梅花。',
                        '摘要是由种子加密生成的32位字母和数字的组合。',
                        '真公平不惧任何质疑，我们支持任何第三方MD5工具检验。',
                        '您可以将种子复制到以下或其他网站进行摘要的正确性验证',
                        '非常快','我们的功能非常迅速，无论您在任何地方，都可以实时存入和转出您喜爱的数字货币。'
                        '我们的系统能让您便捷安全的使用账户。现在就加入最值得信赖的数字货币娱乐场，享受精彩的游戏。',
                        '很隐秘','保护玩家的隐私是我们商业模式的基石。我们无法收集您的任何个人信息，'
                        '您的下注记录也将会受到严格加密保护，这一切只为让你安心游戏。',
                        '很安全','我们非常重视您的账户安全，您的账户将始终冷储存在值得信赖的地方，并随时可供您使用。'
                        '我们将继续在网站中采用最高等级和最安全的标准。旨在确保您的账户永远不会受到损失，'
                        '这里是今天在线上最安全可信赖的数字币娱乐场！']

        # 获取页面所有文本
        title_text = self.find_element(*self.title_loc).text
        language_btn_text = self.find_element(*self.language_btn_loc).text
        register_btn_text = self.find_element(*self.register_btn_loc).text
        fairbanner_textone_text = self.find_element(*self.fairbanner_textone_loc).text
        fairbanner_texttwo_text = self.find_element(*self.fairbanner_texttwo_loc).text
        officialgroup_btn_text = self.find_element(*self.officialgroup_btn_loc).text
        baccarat_name_text = self.find_element(*self.baccarat_name_loc).text
        baccarat_btn_text = self.find_element(*self.baccarat_btn_loc).text
        blackjack_name_text = self.find_element(*self.blackjack_name_loc).text
        blackjack_btn_text = self.find_element(*self.blackjack_btn_loc).text
        md5_title_text = self.find_element(*self.md5_title_loc).text
        md5definition_title_text = self.find_element(*self.md5definition_title_loc).text
        md5definition_text = self.find_element(*self.md5definition_text_loc).text
        seeddefinition_title_text = self.find_element(*self.seeddefinition_title_loc).text
        seeddefinition_text = self.find_element(*self.seeddefinition_text_loc).text
        digestdefinition_title_text = self.find_element(*self.digestdefinition_title_loc).text
        digestdefinition_text = self.find_element(*self.digestdefinition_text_loc).text
        unchangeorder_title_text = self.find_element(*self.unchangeorder_title_loc).text
        unchangeorder_text = self.find_element(*self.unchangeorder_text_loc).text
        unchangecard_title_text = self.find_element(*self.unchangecard_title_loc).text
        unchangecard_text = self.find_element(*self.unchangecard_text_loc).text
        provablyfair_title_text = self.find_element(*self.provablyfair_title_loc).text
        provablyfair_firststep_text = self.find_element(*self.provablyfair_firststep_loc).text
        provablyfair_secondstep_text = self.find_element(*self.provablyfair_secondstep_loc).text
        provablyfair_thirdstep_text = self.find_element(*self.provablyfair_thirdstep_loc).text
        seed_introduce_text = self.find_element(*self.seed_introduce_loc).text
        digest_introduce_text = self.find_element(*self.digest_introduce_loc).text
        verify_tools_title_text = self.find_element(*self.verify_tools_title_loc).text
        verify_tools_text = self.find_element(*self.verify_tools_text_loc).text
        fast_title_text = self.find_element(*self.fast_title_loc).text
        fast_text = self.find_element(*self.fast_text_loc).text
        privacy_title_text = self.find_element(*self.privacy_title_loc).text
        privacy_text = self.find_element(*self.privacy_text_loc).text
        safety_title_text = self.find_element(*self.safety_title_loc).text
        safety_text = self.find_element(*self.safety_text_loc).text

        # 页面所有文本值列表

        getelement = [title_text,language_btn_text,register_btn_text,fairbanner_textone_text,
                      fairbanner_texttwo_text,officialgroup_btn_text,baccarat_name_text,baccarat_btn_text,
                      blackjack_name_text,blackjack_btn_text,md5_title_text,md5definition_title_text,
                      md5definition_text,seeddefinition_title_text,seeddefinition_text,digestdefinition_title_text,
                      digestdefinition_text,unchangeorder_title_text,unchangeorder_text,unchangecard_title_text,
                      unchangecard_text,provablyfair_title_text,provablyfair_firststep_text,
                      provablyfair_secondstep_text,provablyfair_thirdstep_text,seed_introduce_text,
                      digest_introduce_text,verify_tools_title_text,verify_tools_text,fast_title_text,fast_text,
                      privacy_title_text,privacy_text,safety_title_text,safety_text]

        correctvalue = []
        errorvalue = []
        i = 0
        while (i < 35):
            result = getelement[i]
            if (result in truthelement):
                correctvalue.append(result)
            else:
                errorvalue.append(result)
            i = i + 1

   # 首页页面元素是否显示
    def homepage_element_is_display(self):
        self.is_display(self.toplogo_loc)
        self.is_display(self.header_img_loc)
        self.is_display(self.fairbanner_img_loc)
        self.is_display(self.officialgroup_img_loc)
        self.is_display(self.baccarat_img_loc)
        self.is_display(self.blackjack_img_loc)
        self.is_display(self.md5_img_loc)
        self.is_display(self.md5definition_img_loc)
        self.is_display(self.seeddefinition_img_loc)
        self.is_display(self.digestdefinition_img_loc)
        self.is_display(self.unchangeorder_img_loc)
        self.is_display(self.unchangecard_img_loc)
        self.is_display(self.provablyfair_img_loc)
        self.is_display(self.example_seed_loc)
        self.is_display(self.example_arrow_loc)
        self.is_display(self.example_digest_loc)
        self.is_display(self.verify_tools_breatheimg_loc)
        self.is_display(self.verify_adress_box_loc)
        self.is_display(self.webfeature_banner_img_loc)
        self.is_display(self.fast_img_loc)
        self.is_display(self.privacy_img_loc)
        self.is_display(self.safety_img_loc)
        self.is_display(self.static_firstimg_loc)
        self.is_display(self.static_secondimg_loc)
        self.is_display(self.static_thirdimg_loc)
        self.is_display(self.static_fourthimg_loc)
        self.is_display(self.static_fifthimg_loc)
        self.is_display(self.facebook_img_loc)
        self.is_display(self.twitter_img_loc)
        self.is_display(self.mailbox_img_loc)
        self.is_display(self.qqgroup1_img_loc)
        self.is_display(self.qqgroup2_img_loc)
        self.is_display(self.bottom_logo_loc)
        self.is_display(self.homepage_img_loc)
        self.is_display(self.record_img_loc)
        self.is_display(self.accout_img_loc)
        self.is_display(self.mine_img_loc)









