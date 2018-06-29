#######################################################
# FileName:Democase.py
# Author:liketao
# Date:2018-6-21
# Function Description: 示范性的demo用例
#######################################################

import unittest
from Mobile_Testsuite.PO import InitDriver
from Mobile_Testsuite.PO import HomePage


class DemoCase(unittest.TestCase):
    """Demo 测试用例 """
    def setUp(self):
        self.driver = InitDriver.start_driver()
        self.HomePage = HomePage.HomePage(self.driver)
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')

    def tearDown(self):
        self.driver.quit()

    # 未登录时，点击“登录/注册按钮”
    def test_001_click_register_btn(self):
        """测试点：点击登录/注册按钮，跳转进入登录/注册页面"""
        self.HomePage.click_register_btn()

    # 验证页面标题元素及文本正常展示
    def test_002_validation_title(self):
        """测试点：进入首页，取到首页标题并和预期结果比对"""
        title_text = self.HomePage.get_title_text()
        self.assertEqual(title_text, '首页')

if __name__ == '__main__':
    unittest.main()