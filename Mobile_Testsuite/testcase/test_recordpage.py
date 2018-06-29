from appium import webdriver
from Mobile_Testsuite.untils.disbrowser import make_dis
import unittest
import time

class forgetPasswordTestCase(unittest.TestCase):
    # set up appium
    def setUp(self):
        print("------------------setUp Test-----------------------")
        self.dis_browser = make_dis()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dis_browser)
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[2]/a[1]').click()
    def tearDown(self):
        print("------------------tearDown Test-----------------------")
        self.driver.quit()

    def test_ui(self):
        # 确认跳转至登录页面
        try:
            self.assertEqual('http://192.168.8.21:8989/fotgotpassword', self.driver.current_url)
            print("跳转忘记密码页面成功")
        except AssertionError:
            print("跳转忘记密码页面错误")
        # 忘记密码界面检查
        result = self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/button')
        self.assertEqual('发送重置链接到邮箱', result.text)
        print("发送重置密码按钮")
        #头像图标检查
        try:
            self.assertFalse(self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[1]/label').is_displayed())
            print("头像图标可见")
        except AssertionError:
            print("头像图标不可见")
        #账号输入框检查
        try:
            self.assertFalse(self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[1]/input').is_displayed())
            print("账号输入框可见")
        except AssertionError:
            print("账号输入框不可见")
        #邮箱图标检查
        try:
            self.assertFalse(self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/label').is_displayed())
            print("邮箱图标可见")
        except AssertionError:
            print("邮箱图标不可见")
        #邮箱输入框检查
        try:
            self.assertFalse(self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').is_displayed())
            print("邮箱输入框可见")
        except AssertionError:
            print("邮箱输入框不可见")
        #验证码图标检查
        try:
            self.assertFalse(self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[3]/label').is_displayed())
            print("验证码图标可见")
        except AssertionError:
            print("验证码图标不可见")
        #验证码输入框检查
        try:
            self.assertFalse(self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[3]/input').is_displayed())
            print("验证码输入框可见")
        except AssertionError:
            print("验证码输入框不可见")
        # 登录页面logo检查
        logo = self.driver.find_element_by_xpath('//*[@id="fotgotpassword"]/div')
        try:
            self.assertTrue(logo.is_displayed())
            print("忘记密码页面logo正确，logo可见")
        except AssertionError:
            print("忘记密码页面logo错误，logo不可见")
    #正常发送密码重置申请
    def test_applySuccess(self):
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[1]/input').send_keys('j123456')
        # 输入邮箱
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('lei.jiang@fafafa.io')
        # 输入验证码
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('d16a8f507db64456ad1d536aaae1e762')
        #点击重置密码按钮
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/button').click()
        time.sleep(1)
        #发送重置密码邮件申请成功提示语验证
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('密码重置链接已发送到该邮箱，请于24小时内通过链接修改密码', result.text)
        print("发送重置密码邮件申请成功提示语正确")


    #用户名为空提示语验证
    def test_emptyId(self):
        # 输入邮箱
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('lei.jiang@fafafa.io')
        # 输入验证码
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('d16a8f507db64456ad1d536aaae1e762')
        # 点击重置密码按钮
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/button').click()
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('请输入用户名', result.text)
        print("账号为空提示语正确")
    #邮箱为空提示语验证
    def test_emptyEmail(self):
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[1]/input').send_keys('j123456')
        # 输入验证码
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('d16a8f507db64456ad1d536aaae1e762')
        # 点击重置密码按钮
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/button').click()
        time.sleep(1)
        # 发送重置密码邮件申请成功提示语验证
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('请输入注册邮箱。', result.text)
        print("邮箱为空提示语正确")
    #验证码为空提示语验证
    def test_emptyAssetCode(self):
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[1]/input').send_keys('j123456')
        # 输入邮箱
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('lei.jiang@fafafa.io')
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/button').click()
        time.sleep(1)
        # 发送重置密码邮件申请成功提示语验证
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('请输入验证码。', result.text)
        print("验证码为空提示语正确")
    #输入错误的用户名，正确的验证码和邮箱
    def test_wrongId(self):
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[1]/input').send_keys('j1234567')
        # 输入邮箱
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('lei.jiang@fafafa.io')
        # 输入验证码
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('d16a8f507db64456ad1d536aaae1e762')
        # 点击重置密码按钮
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/button').click()
        time.sleep(1)
        # 发送重置密码邮件申请成功提示语验证
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('邮箱与账号不匹配。', result.text)
        print("输入错误的用户名提示语正确")
    #输入错误的邮箱，正确的验证码和用户名
    def test_wrongEmail(self):
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[1]/input').send_keys('j123456')
        # 输入邮箱
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('kk@163.com')
        # 输入验证码
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('d16a8f507db64456ad1d536aaae1e762')
        # 点击重置密码按钮
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/button').click()
        time.sleep(1)
        # 发送重置密码邮件申请成功提示语验证
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('邮箱与账号不匹配。', result.text)
        print("输入错误的邮箱提示语正确")

    # 输入错误格式的邮箱，正确的验证码和用户名
    def test_wrong_emailType(self):
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[1]/input').send_keys('j123456')
        # 输入邮箱
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('kkk1kk')
        # 输入验证码
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('d16a8f507db64456ad1d536aaae1e762')
        # 点击重置密码按钮
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/button').click()
        time.sleep(1)
        # 发送重置密码邮件申请成功提示语验证
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('请输入正确的邮箱。', result.text)
        print("输入错误格式的邮箱提示语正确")
    #输入错误的验证码，正确的用户名和邮箱
    def test_wrongAssertCode(self):
        # 输入账号
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[1]/input').send_keys('j123456')
        # 输入邮箱
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('lei.jiang@fafafa.io')
        # 输入验证码
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/div[2]/input').send_keys('456ad1762')
        # 点击重置密码按钮
        self.driver.find_element_by_xpath('//*[@id="fotgot-form"]/button').click()
        time.sleep(1)
        # 发送重置密码邮件申请成功提示语验证
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('验证码错误。', result.text)
        print("输入错的验证码提示语正确")


if __name__ == '__main__':
    unittest.main()


