#######################################################
# FileName:test_language.py
# Author:wangxiaoxiao
# Date:2018-7-6
# Function Description: Language页面
#######################################################
import unittest
from Mobile_Testsuite.PO import InitDriver
from Mobile_Testsuite.PO import HomePage
from Mobile_Testsuite.PO import LanPage
from Mobile_Testsuite.Untils.server import Server
import time


class LanguageCase(unittest.TestCase):
    """Language 测试用例 """

    @classmethod
    def setUpClass(cls):
        server = Server()
        server.main()

    def setUp(self):
        self.driver = InitDriver.start_driver()
        self.HomePage = HomePage.HomePage(self.driver)
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        self.HomePage.click_language_btn()
        self.LanPage = LanPage.LanPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    # 验证点击取消按钮
    def test_001_cancel_btn(self):
        """测试点：点击其他语言后，点击取消，检查是否跳转至首页，内容是否切换语言"""
        print("test_001_cancel_btn")
        self.LanPage.click_chinese_hk()
        self.assertTrue(self.LanPage.chinese_hk_is_selected())
        self.LanPage.click_cancel_btn()
        time.sleep(2)
        self.assertEqual("首页", self.HomePage.get_title_text())

    # 验证点击英语确认
    def test_002_set_english(self):
        """测试点：点击英语，检查是否被选中，点击确认后是否跳转首页，语言是英语"""
        print("test_002_set_english")
        self.LanPage.click_english()
        self.assertTrue(self.LanPage.english_is_selected())
        self.LanPage.click_confirm_btn()
        time.sleep(2)
        self.assertEqual("Home", self.HomePage.get_title_text())

    # 验证点击繁体中文确认
    def test_003_set_chinese_hk(self):
        """测试点：点击繁体中文，检查是否被选中，点击确认后是否跳转首页，语言是繁体中文"""
        print("test_003_set_chinese_hk")
        self.LanPage.click_chinese_hk()
        self.assertTrue(self.LanPage.chinese_hk_is_selected())
        self.LanPage.click_confirm_btn()
        time.sleep(2)
        self.assertEqual("首頁", self.HomePage.get_title_text())


if __name__ == '__main__':
    unittest.main()
