from selenium.webdriver.common.by import By
from Mobile_Testsuite.PO.BasePage import Element


# 继承Element类
class RecordPage(Element):
    # 记录界面入口
    record_interface = (By.XPATH, '//*[@id="footer"]/a[2]')
    # 顶栏标题
    title_loc = (By.XPATH, '//*[@id="header"]/header/h1')
    # Logo图标
    logo_loc = (By.XPATH, '//*[@id="header"]/header/div[1]/button/label/img')
    # 默认头像图标
    defalut_avatar_icon = (By.XPATH, '//*[@id="loginRegister"]/a/span[1]')
    # 有效下注按钮
    effBet_btn_loc = (By.XPATH, '//*[@id="profile-main"]/div[1]/a[1]/div[2]')
    # 下注详情按钮
    betDetails_btn_loc = (By.XPATH, '//*[@id="profile-main"]/div[1]/a[2]/div[2]')
    # 本周勾选框
    week_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[1]/label[1]/span[1]/span')
    # 本月勾选框
    month_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[1]/label[2]/span[1]/span')
    # 下注勾选框
    bet_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[1]/span[1]/span')
    # 派彩勾选框
    payout_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[2]/span[1]/span')
    # 转入勾选框
    deposit_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[3]/span[1]/span')
    # 转出勾选框
    withdraw_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[4]/span[1]/span')
    # 退还勾选框
    refund_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[5]/span[1]/span')
    # 奖励勾选框
    reward_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[6]/span[1]/span')
    # 百家乐勾选框
    baccarat_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[3]/div/label[1]/span[1]/span')
    # 21点勾选框
    blackjack_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[3]/div/label[2]/span[1]/span')
    # ETC勾选框
    ETH_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[4]/div/label[1]/span[1]/span')
    # BTC勾选框
    BTC_box = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[4]/div/label[2]/span[1]/span')
    # 搜索按钮
    search_btn = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[5]/button')
    # 表格内容（时间）
    time_loc = (By.XPATH, '//*[@id="profileRight-form"]/div[2]/table/thead/tr/th[1]')
    # 表格内容（游戏）
    game_loc = (By.XPATH, '//*[@id="profileRight-form"]/div[2]/table/thead/tr/th[2]')
    # 表格内容（类型）
    type_loc = (By.XPATH, '//*[@id="profileRight-form"]/div[2]/table/thead/tr/th[3]')
    # 表格内容（币种）
    currency_loc = (By.XPATH, '//*[@id="profileRight-form"]/div[2]/table/thead/tr/th[4]')
    # 表格内容（额度）
    lines_loc = (By.XPATH, '//*[@id="profileRight-form"]/div[2]/table/thead/tr/th[5]')

    # 操作方法
    # 点击记录入口按钮
    def __init__(self, driver):
        super().__init__(driver)

    def click_register_btn(self):
        self.click(self.record_interface)

    # 点击有效下注按钮
    def click_effBet_btn(self):
        self.click(self.effBet_btn_loc)

    # 点击下注详情按钮
    def click_betDetails_btn(self):
        self.click(self.betDetails_btn_loc)

    # 点击本周勾选框
    def click_week_box(self):
        self.click(self.week_box)

    # 点击本月勾选框
    def click_month_box(self):
        self.click(self.month_box)

    # 点击下注勾选框
    def click_bet_box(self):
        self.click(self.bet_box)

    # 点击派彩勾选框
    def click_payout_box(self):
        self.click(self.payout_box)

    # 点击转入勾选框
    def click_deposit_box(self):
        self.click(self.deposit_box)

    # 点击转出勾选框
    def click_withdraw_box(self):
        self.click(self.withdraw_box)

    # 点击退还勾选框
    def click_refund_box(self):
        self.click(self.refund_box)

    # 点击奖励勾选框
    def click_reward_box(self):
        self.click(self.reward_box)

    # 点击百家乐勾选框
    def click__baccarat_box(self):
        self.click(self.baccarat_box)

    # 点击21点勾选框
    def click_blackjack_box(self):
        self.click(self.blackjack_box)

    # 点击ETH勾选框
    def click_ETH_box(self):
        self.click(self.ETH_box)

    # 点击BTC勾选框
    def click_BTC_box(self):
        self.click(self.BTC_box)

    # 点击搜索按钮
    def click_search_btn(self):
        self.click(self.search_btn)

    # 获取界面元素
    # 获取顶栏标题的文本内容
    def get_title_text(self):
        title_text = self.find_element(*self.title_loc).text
        return title_text

    # 获取表格时间标题
    def get_time_text(self):
        title_text = self.find_element(*self.title_loc).text
        return title_text

    # 获取表格游戏标题
    def get_game_text(self):
        game_text = self.find_element(*self.game_loc).text
        return game_text

    # 获取表格类型标题
    def get_type_text(self):
        type_text = self.find_element(*self.type_loc).text
        return type_text

    # 获取表格币种标题
    def get_currency_text(self):
        currency_text = self.find_element(*self.currency_loc).text
        return currency_text

    # 获取表格额度标题
    def get_lines_text(self):
        lines_text = self.find_element(*self.lines_loc).text
        return lines_text
