#######################################################
# FileName:test_login.py
# Author:wangxiaoxiao
# Date:2018-7-6
# Function Description: Login页面
#######################################################
import unittest
from Mobile_Testsuite.PO import InitDriver
from Mobile_Testsuite.PO import HomePage
from Mobile_Testsuite.PO import LoginPage
from Mobile_Testsuite.Untils.server import Server



class LoginCase(unittest.TestCase):
    """Login 测试用例 """

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

    def tearDown(self):
        self.driver.quit()

    # 验证忘记密码链接跳转
    def test_001_forgot_link(self):
        """测试点：点击忘记密码跳转是否成功"""
        print("test_001_forgot_link")
        self.LoginPage.click_forgot_link()
        self.assertEqual("http://192.168.8.21:8989/fotgotpassword", self.driver.current_url)

    # 验证新用户注册链接跳转
    def test_002_register_link(self):
        """测试点：点击新用户注册跳转是否成功"""
        print("test_002_register_link")
        self.LoginPage.click_register_link()
        self.assertEqual("http://192.168.8.21:8989/newusers", self.driver.current_url)

    # 正确账号密码，验证登录
    def test_003_login_correct(self):
        """测试点：输入正确账号密码，点击登录是否登录成功"""
        print("test_003_login_correct")
        self.LoginPage.send_username("xiaoxiao")
        self.LoginPage.send_password("qqq111")
        # self.driver.press_keycode('4')
        self.LoginPage.click_login_btn()
        self.assertEqual('首页', self.HomePage.get_title_text())


if __name__ == '__main__':
    unittest.main()
