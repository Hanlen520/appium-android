#######################################################
# FileName:test_account.py
# Author:liketao
# Date:2018-7-209
# Function Description:账户相关用例
#######################################################


import unittest
from Mobile_Testsuite.PO import AccoutPage
from Mobile_Testsuite.Untils.server import Server
from Mobile_Testsuite.testcase.common import Common
from Mobile_Testsuite.PO import InitDriver


class Account(unittest.TestCase):
    """账户测试用例"""
    @classmethod
    def setUpClass(cls):
        server = Server()
        server.main()

    def setUp(self):
        self.driver = InitDriver.start_driver()
        self.AccountPage = AccoutPage.AccoutPage(self.driver)
        self.common = Common(self.driver)
        self.common.enter_account_page()

    def tearDown(self):
        self.driver.quit()

    # 跳转进入到账户页面
    def test_001_click_account_btn(self):
        """测试点：点击账户按钮，跳转进入账户页面,检查跳转后页面标题是否是正确"""


if __name__ == '__main__':
    unittest.main()