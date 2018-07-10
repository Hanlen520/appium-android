#######################################################
# FileName:test_forget_password.py
# Author:wangxiaoxiao
# Date:2018-7-6
# Function Description: forget_password页面
#######################################################

import unittest
from Mobile_Testsuite.PO import InitDriver
from Mobile_Testsuite.PO import HomePage
from Mobile_Testsuite.PO import LoginPage
from Mobile_Testsuite.PO import FogotPwPage
from Mobile_Testsuite.Untils.server import Server


class ForgotPWCase(unittest.TestCase):
    """ForgotPassword 测试用例 """

    @classmethod
    def setUpClass(cls):
        server = Server()
        server.main()

    def setUp(self):
        self.driver = InitDriver.start_driver()
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        self.HomePage = HomePage.HomePage(self.driver)
        self.HomePage.click_register_btn()
        self.LoginPage = LoginPage.LoginPage(self.driver)
        self.LoginPage.click_forgot_link()
        self.ForgotPwPage = FogotPwPage.FogotPwPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    # 验证输入正确信息提交
    def test_001_info_correct(self):
        """测试点：输入正确账号，邮箱，验证码，是否能提交成功"""
        print("test_001_info_correct")
        self.ForgotPwPage.send_username("xiaoxiao")
        self.ForgotPwPage.send_email("xiaoxiao.wang@fafafa.io")
        self.ForgotPwPage.send_code("d16a8f507db64456ad1d536aaae1e762")
        self.ForgotPwPage.click_send_link_btn()
        self.assertEqual("重置密码链接已发送到您绑定的邮箱，请在24小时内前往修改密码。", self.ForgotPwPage.get_correct_text())


if __name__ == '__main__':
    unittest.main()


