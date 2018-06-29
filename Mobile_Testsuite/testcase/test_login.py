from Mobile_Testsuite.untils.log import LOG
from Mobile_Testsuite.testcase.common import *
import unittest
import time


class LoginTestCase(unittest.TestCase, Common):
    def setUp(self):
        print("------------------setUp Test-----------------------")
        Common.__init__(self)
        Common.setup(self)

    def tearDown(self):
        print("------------------tearDown Test-----------------------")
        Common.quit(self)

    # 登录页面UI检查
    def test_ui(self):
        LOG.info("登录页面UI验证")
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]').click()
        # 登录页面标题部分检查，应该不可见
        self.assertFalse((self.driver.find_element_by_xpath('//*[@id="header"]/header').is_displayed()))
        # 登录页面logo检查
        logo = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]')
        self.assertTrue(logo.is_displayed())
        # 登录页面账号图标检查
        account_picture = self.driver.find_element_by_xpath('//*[@id="form_login"]/div[1]/label')
        self.assertTrue(account_picture.is_displayed())
        # 登录页面密码图标检查
        password_picture = self.driver.find_element_by_xpath('//*[@id="form_login"]/div[2]/label')
        self.assertTrue(password_picture.is_displayed())
        # 登录页面登录按钮状态检查，默认禁用
        self.assertFalse(self.driver.find_element_by_xpath('//*[@id="form_login"]/button').is_enabled())
        # 登录页面“忘记密码”文本检查
        self.assertTrue((self.driver.find_element_by_link_text("忘记密码").is_displayed()))
        # 登录页面“新用户注册”文本检查
        self.assertTrue((self.driver.find_element_by_link_text("新用户注册").is_displayed()))
        LOG.info("登录页面UI正确")

    # 输入正确账号和密码，登录成功验证
    def test_login_success(self):
        LOG.info("正确信息，登录成功验证")
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]').click()
        # 确认跳转至登录页面
        self.assertEqual('http://192.168.8.21:8989/login', self.driver.current_url)
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="form_login"]/div[1]/input').send_keys(self.username)
        # 输入密码
        self.driver.find_element_by_xpath('//*[@id="form_login"]/div[2]/input').send_keys(self.password)
        # 点击提交
        self.driver.find_element_by_xpath('//*[@id="form_login"]/button').click()	   
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]').is_displayed())
        LOG.info("正确账号密码，登录成功")


if __name__ == '__main__':
    unittest.main()

