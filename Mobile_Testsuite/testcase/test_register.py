#######################################################
# FileName:test_register.py
# Author:wangxiaoxiao
# Date:2018-7-6
# Function Description: Register页面
#######################################################
import unittest
from Mobile_Testsuite.PO import InitDriver
from Mobile_Testsuite.PO import HomePage
from Mobile_Testsuite.PO import LoginPage
from Mobile_Testsuite.PO import RegPage
from Mobile_Testsuite.Untils.server import Server
import random

registerName = "test" + random.randint(0, 9) + random.randint(0, 9) + random.randint(0, 9)
registerEmail = str(registerName) + "@sina.cn"


class RegisterCase(unittest.TestCase):
    """Register 测试用例 """

    @classmethod
    def setUpClass(cls):
        server = Server()
        server.main()

    def setUp(self):
        self.driver = InitDriver.start_driver()
        self.HomePage = HomePage.HomePage(self.driver)
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        self.HomePage.click_register_btn()
        self.LoginPage = LoginPage.LoginPage(self.driver)
        self.LoginPage.click_register_link()
        self.RegisterPage = RegPage.RegPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    # 验证服务条款弹窗
    def test_001_service_window(self):
        """测试点：点击服务条款，弹出弹窗"""
        print("test_001_service_window")
        self.RegisterPage.click_service_btn()
        self.assertTrue(self.RegisterPage.service_window_is_display())

    # 验证正确注册信息提交
    def test_002_register_correct(self):
        """测试点：正确用户名，密码，邮箱，是否提交成功"""
        print("test_002_register_correct")
        self.RegisterPage.send_username(registerName)
        self.RegisterPage.send_password("qqq111")
        self.RegisterPage.send_email(registerEmail)
        self.RegisterPage.click_register_btn()
        self.assertEqual('首页', self.HomePage.get_title_text())



if __name__ == '__main__':
    unittest.main()
