import unittest
from Mobile_Testsuite.PO.RecordPage import RecordPage
from Mobile_Testsuite.PO.HomePage import HomePage
from Mobile_Testsuite.Untils.server import Server
from Mobile_Testsuite.PO import InitDriver
from Mobile_Testsuite.testcase.common import Common


class RecordPageTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        server = Server()
        server.main()

    def setUp(self):
        self.driver = InitDriver.start_driver()
        self.HomePage = HomePage(self.driver)
        self.driver.get('http://192.168.8.21:8989/home')
        self.common = Common(self.driver)
        self.common.login()
        self.RecordPage = RecordPage(self.driver)
        self.RecordPage.click_record_btn()

    def tearDown(self):
        print("------------------环境初始化-----------------------")
        self.driver.quit()

    # 确认是否已进入记录界面
    def test_ownRecordUI(self):
        title_text = self.RecordPage.get_title_text()
        self.assertEqual(title_text, '个人记录')
        print("------------------个人记录-----------------------")
    def test_effBet(self):
        if self.RecordPage.effBet_btn.is_selected():
            print('selected!')
        else:
            print('not yet!')

 # 有效下注记录界面元素检查
    def test_effBet_btn_text(self):
        effBet_btn_text = self.RecordPage.get_effBet_btn_text()
        self.assertEqual(effBet_btn_text, '有效下注')
        print("------------------有效下注-----------------------")
    def test_betDetails_text(self):
        betDetails_text = self.RecordPage.get_betDetails_text()
        self.assertEqual(betDetails_text, '下注详情')
        print("-----------------下注详情-----------------------")

    # 下注详情界面
    def test_confirmUI(self):
        self.RecordPage.click_betDetails_btn()
        search_text = self.RecordPage.get_search_text()
        self.assertEqual(search_text, '搜索')
        print("------------------搜索-----------------------")

    # 下注详情界面默认选中的勾选框
    def test_allRadioBox(self):
        self.RecordPage.click_betDetails_btn()
        if self.driver.find_element_by_xpath('//*[@id="profileRight-form"]/div[1]/div[1]/label[1]/span[1]/span',
                                             '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[1]/span[1]/span',
                                             '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[2]/span[1]/span',
                                             '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[3]/span[1]/span',
                                             '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[4]/span[1]/span',
                                             '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[5]/span[1]/span',
                                             '//*[@id="profileRight-form"]/div[1]/div[2]/div/label[6]/span[1]/span',
                                             '//*[@id="profileRight-form"]/div[1]/div[3]/div/label[1]/span[1]/span',
                                             '//*[@id="profileRight-form"]/div[1]/div[3]/div/label[2]/span[1]/span',
                                             '//*[@id="profileRight-form"]/div[1]/div[4]/div/label[1]/span[1]/span',
                                             '//*[@id="profileRight-form"]/div[1]/div[4]/div/label[3]/span[1]/span'
                                             ).is_selected():
            print('selected!')
        else:
            print('not yet!')
    def test_month_radioBox(self):
       if self.driver.find_element_by_xpath('//*[@id="profileRight-form"]/div[1]/div[1]/label[2]/span[1]/span').is_unselected():
        print('unselected!')
       else:
        print('not yet!')
if __name__ == '__main__':
    unittest.main()
