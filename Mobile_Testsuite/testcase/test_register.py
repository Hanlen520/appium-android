from Mobile_Testsuite.testcase.common import Common
from Mobile_Testsuite.untils.log import LOG
import unittest
import time
import random
import string

#获取账号、密码、邮箱的输入内容
# username = globalvar.get_username()
# password = globalvar.get_password()
# email = globalvar.get_email()


#组合数字与小写字母的序列
s = string.digits + string.ascii_lowercase
#随机取出6个字母和数字的组合合并成字符串
random_data = ''.join(random.sample(s, 6))


class RegisterTestCase(unittest.TestCase, Common):
    def setUp(self):
        print("------------------setUp Test-----------------------")
        Common.__init__(self)
        Common.setup(self)

    def tearDown(self):
        print("------------------tearDown Test-----------------------")
        Common.quit(self)

    # 注册页面UI检查
    def test_register_ui(self):
        LOG.info("注册页面UI验证")
        self.driver.get(self.baseurl)
        self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]').click()
        self.driver.find_element_by_link_text("新用户注册").click()
        # 注册页面标题部分检查，应该不可见
        self.assertFalse((self.driver.find_element_by_xpath('//*[@id="header"]/header').is_displayed()))
        # 注册页面logo检查
        logo = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]')
        self.assertTrue(logo.is_displayed())
        # 注册页面账号图标检查
        account_picture = self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[1]/label')
        self.assertTrue(account_picture.is_displayed())
        # 注册页面密码图标检查
        password_picture = self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[2]/label')
        self.assertTrue(password_picture.is_displayed())
        # 注册页面邮箱图标检查
        mail_picture = self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[2]/label')
        self.assertTrue(mail_picture.is_displayed())
        # 注册页面服务条款勾选框检查
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[4]/label/span[1]').is_displayed())
        # 注册页面服务条款勾选框状态检查，默认勾选
        checkbox = self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[4]/label/span[1]/input')
        self.assertTrue(checkbox.is_selected())
        # 注册页面服务条款文本信息检查s
        rule = self.driver.find_element_by_xpath('//*[@id="newusers-form"]/div[4]/label/span[2]')
        self.assertEqual('我接受《服务条款》', rule.text)
        # 注册页面进入游戏按钮状态检查，默认禁用
        self.assertFalse(self.driver.find_element_by_xpath('//*[@id="newusers-form"]/button').is_enabled())
        LOG.info("注册页面UI正确")

    # 输入正确账号，密码和邮箱，注册成功验证
    def test_register_success(self):
        LOG.info("正确信息，注册成功验证")
        Common.register(self)
        time.sleep(3)
        result = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/div/div/span[2]/span')
        self.assertEqual('0.00000000', result.text)
        LOG.info("正确账号，密码，邮箱，注册成功")


if __name__ == '__main__':
    unittest.main()