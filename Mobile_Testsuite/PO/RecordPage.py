from selenium.webdriver.common.by import By
from Mobile_Testsuite.PO.BasePage import Element

# 继承Element类
class RecordPage(Element):
    # 记录界面入口
    record_interface = (By.XPATH, '//*[@id="footer"]/a[2]')
    # 个人下注顶栏标题
    title_text =(By.XPATH, '//*[@id="header"]/header/h1')
    # 有效下注按钮
    effBet_btn = (By.XPATH, '//*[@id="profile-main"]/div[1]/a[1]/div[2]')
    # 下注详情按钮
    betDetails_btn = (By.XPATH, '//*[@id="profile-main"]/div[1]/a[2]/div[2]')
    # 搜索按钮
    search_btn = (By.XPATH, '//*[@id="profileRight-form"]/div[1]/div[5]/button')
 # 操作方法
    # 点击记录入口按钮
    def click_record_btn(self):
        self.click(self.record_interface)
    # 点击有效下注按钮
    def click_effBet_btn(self):
        self.click(self.effBet_btn)
    # 点击下注详情按钮
    def click_betDetails_btn(self):
        self.click(self.betDetails_btn)
    # 点击搜索按钮
    def click_search_btn(self):
        self.click(self.search_btn)
    # 获取界面元素
    # 获取顶栏标题的文本内容
    def get_title_text(self):
        title_text = self.find_element(*self.title_text).text
        return title_text
     #获取有效下注按钮文本信息
    def get_effBet_btn_text(self):
        effBet_btn = self.find_element(*self.effBet_btn).text
        return effBet_btn
    #获取下注详情按钮文本
    def get_betDetails_text(self):
        betDetails_text=self.find_element(*self.betDetails_btn).text
        return betDetails_text
    #获取搜索按钮文本
    def get_search_text(self):
        search_text=self.find_element(*self.search_btn).text
        return search_text