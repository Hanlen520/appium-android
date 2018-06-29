from appium import webdriver
from Mobile_Testsuite.untils.disbrowser import make_dis
import unittest

class forgetPasswordTestCase(unittest.TestCase):
    def setUp(self):
        self.dis_browser = make_dis()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dis_browser)
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]').click()
        self.driver.find_element_by_xpath('//*[@id="form_login"]/div[1]/input').send_keys('j123456')
        self.driver.find_element_by_xpath('//*[@id="form_login"]/div[2]/input').send_keys('123456')
        self.driver.find_element_by_xpath('//*[@id="form_login"]/button').click()
        self.driver.find_element_by_xpath('//*[@id="footer"]/a[4]').click()
    def tearDown(self):
        print("------------------tearDown Test-----------------------")
        self.driver.quit()

    def test_ui(self):
        # 确认跳转至我的页面
        try:
            self.assertEqual('http://192.168.8.21:8989/mine', self.driver.current_url)
            print("跳转我的页面成功")
        except AssertionError:
            print("跳转我的页面错误")
        # 我的界面检查
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[3]/a')
        self.assertEqual('退出登录', result.text)
        print("退出登录")
    def test_logCheck(self):
        logo = self.driver.find_element_by_xpath('//*[@id="header"]/header/div[1]/button/label/img')
        try:
            self.assertTrue(logo.is_displayed())
            print("顶栏log可见")
        except AssertionError:
            print("顶栏log不可见")
    def test_topBarCheck(self):
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/h1')
        self.assertEqual('我的', result.text)
        print("------------------我的-----------------------")
    def test_headImage(self):
        logo = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[1]')
        try:
            self.assertTrue(logo.is_displayed())
            print("默认玩家头像可见")
        except AssertionError:
            print("默认玩家头像不可见")
    def test_nick(self):
        logo = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]')
        try:
            self.assertTrue(logo.is_displayed())
            print("玩家昵称可见")
        except AssertionError:
            print("玩家昵称不可见")
    def test_coinImage(self):
        logo = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/div/div/span[3]/img')
        try:
            self.assertTrue(logo.is_displayed())
            print("币种图标存在")
        except AssertionError:
            print("币种图标不存在")
    def test_balance(self):
        balance= self.driver.find_element_by_xpath('//*[@id="loginRegister"]/div/div/span[2]')
        try:
            self.assertTrue(balance.is_displayed())
            print("筹码存在")
        except AssertionError:
            print("筹码不存在")

    def test_coinIcon(self):
        coinIcon = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/div/div/span[1]')
        try:
            self.assertTrue(coinIcon.is_displayed())
            print("币种切换按钮存在")
        except AssertionError:
            print("币种切换按钮不存在")
#修改昵称
    #顶栏检查
    def test_topLogCheck(self):
        logo = self.driver.find_element_by_xpath('//*[@id="header"]/header/div[1]/button/label/img')
        try:
            self.assertTrue(logo.is_displayed())
            print("顶栏log可见")
        except AssertionError:
            print("顶栏log不可见")
    def test_topTittleCheck(self):
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/h1')
        self.assertEqual('修改昵称', result.text)
        print("------------------修改密码顶栏标题正确-----------------------")
    def test_changeLanguage(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="header"]/header/div[2]/button/label').is_undisplayed()
            print('切换语言按钮不可见，正确')
        except AssertionError:
            print('切换语言按钮可见，错误')
    def test_alterNicknameButton(self):
        #按钮检查
        button = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]')
        try:
            self.assertTrue(button.is_displayed())
            print("修改昵称按钮可见")
        except AssertionError:
            print("修改昵称按钮不可见")
      #修改昵称文本检查
    def test_alterNicknameContent(self):
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('修改昵称', result.text)
        print("------------------修改昵称-----------------------")
      #修改昵称按钮功能检查
    def test_alterNicknameFUN(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        try:
            self.assertEqual('http://192.168.8.21:8989/changename', self.driver.current_url)
            print("跳转修改昵称页面成功")
        except AssertionError:
            print("跳转修改昵称页面错误")
    def test_alterNicknameUI(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        content = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input')
        try:
            self.assertTrue(content.is_displayed())
            print("修改昵称输入框原昵称可见")
        except AssertionError:
            print("修改昵称输入框原昵称不可见")
    def test_clearButton(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        button = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span')
        try:
            self.assertTrue(button.is_displayed())
            print("清空输入框按钮可见")
        except AssertionError:
            print("清空输入框原昵称不可见")
    def test_clearButtonFun(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        content = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input')
        try:
            self.assertTrue(content.is_displayed())
            print("清空输入框成功")
        except AssertionError:
            print("清空输入框按钮功能失效")

    def test_info(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[2]')
        self.assertEqual('请输入6-12位的用户名', result.text)
        print("------------------默认提示文本正确-----------------------")
   #修改昵称成功
        #输入6位数字
    def test_input_6digit(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('123456')
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('昵称修改成功', result.text)
        print("------------------昵称修改成功-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/mine', self.driver.current_url)
            print("跳转我的界面正确")
        except AssertionError:
            print("跳转首页界面错误")
        #输入12位数字
    def test_input_12digit(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('123456789012')
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()
        print("------------------昵称修改成功-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/home', self.driver.current_url)
            print("跳转首页界面正确")
        except AssertionError:
            print("跳转首页界面错误")
        #输入6位汉字
    def test_input_6characters(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('或多或')
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()
        print("------------------昵称修改成功-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/home', self.driver.current_url)
            print("跳转首页界面正确")
        except AssertionError:
            print("跳转首页界面错误")
        #输入12位汉字
    def test_input_12characters(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('红河黄精鸡怪')
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()
        print("------------------昵称修改成功-----------------------")
        try:
             self.assertEqual('http://192.168.8.21:8989/home', self.driver.current_url)
             print("跳转首页界面正确")
        except AssertionError:
             print("跳转首页界面错误")
        #输入6位韩文字符
    def test_input_6Korean(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('우물쭈')
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('昵称修改成功', result.text)
        print("------------------昵称修改成功-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/mine', self.driver.current_url)
            print("跳转我的界面正确")
        except AssertionError:
            print("跳转我的界面错误")
        #输入6位日文字符
    def test_input_6japanese(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('彼が食')
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('昵称修改成功', result.text)
        print("------------------昵称修改成功-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/mine', self.driver.current_url)
            print("跳转我的界面正确")
        except AssertionError:
            print("跳转我的界面错误")
        #输入12位韩文字符
    def test_input_12Korean(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('이 사람은 도대')
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('昵称修改成功', result.text)
        print("------------------昵称修改成功-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/mine', self.driver.current_url)
            print("跳转我的界面正确")
        except AssertionError:
            print("跳转我的界面错误")
        #输入12位日文字符
    def test_input_12japanese(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('彼が食べない寿司')
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()

        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('昵称修改成功', result.text)
        print("------------------昵称修改成功-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/mine', self.driver.current_url)
            print("跳转我的界面正确")
        except AssertionError:
            print("跳转我的界面错误")
    #修改昵称失败
        #输入昵称为空
    def test_empty(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('昵称不能为空', result.text)
        print("------------------昵称为空提示语正确-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/changename', self.driver.current_url)
            print("界面正确")
        except AssertionError:
            print("界面错误")
        #输入超过12个字符的数字
    def test_input_13digit(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('1234567890123')
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('请输入6-12位的用户名', result.text)
        print("------------------超过12个字符的昵称提示语正确-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/changename', self.driver.current_url)
            print("界面正确")
        except AssertionError:
            print("界面错误")
        #输入超过12个字符的汉字
    def test_input_14characters(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('好打发实际上啊')
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('请输入6-12位的用户名', result.text)
        print("------------------14个字符的汉字提示语正确-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/changename', self.driver.current_url)
            print("界面正确")
        except AssertionError:
            print("界面错误")
        #输入的昵称含有特殊字符
    def test_input_specialCharacter(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('12@#个')
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('昵称包含特殊字符', result.text)
        print("------------------含有特殊字符的昵称提示语正确-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/changename', self.driver.current_url)
            print("界面正确")
        except AssertionError:
            print("界面错误")

#修改密码
     #修改密码按钮检查
    def test_alterPasswordButton(self):

        button = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[2]/div[1]')
        try:
            self.assertTrue(button.is_displayed())
            print("修改密码按钮可见")
        except AssertionError:
            print("修改密码按钮不可见")
    #修改密码按钮文本检查
    def test_alterPasswordContent(self):
        result = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[2]/div[2]')
        self.assertEqual('修改密码', result.text)
        print("------------------修改密码-----------------------")
     #修改密码功能检查
    def test_alterPasswordFUN(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[2]/div[1]').click()
        try:
            self.assertEqual('http://192.168.8.21:8989/changepassword', self.driver.current_url)
            print("跳转修改密码页面成功")
        except AssertionError:
            print("跳转修改密码页面错误")
#修改密码界面检查
    #顶栏文本检查
    def test_languageButton(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="header"]/header/div[2]/button/label').is_undisplayed()
            print('切换语言按钮不可见，正确')
        except AssertionError:
            print('切换语言按钮可见，错误')
    def test_topBarLogCheck(self):
        logo = self.driver.find_element_by_xpath('//*[@id="header"]/header/div[1]/button/label/img')
        try:
            self.assertTrue(logo.is_displayed())
            print("顶栏log可见")
        except AssertionError:
            print("顶栏log不可见")
    def test_topBarTittleCheck(self):
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/h1')
        self.assertEqual('修改密码', result.text)
        print("------------------顶栏标题正确-----------------------")
    def test_emailContent(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[2]/div[2]').click()
        result = self.driver.find_element_by_xpath('//*[@id="changePass"]/div/form/div/div[1]/label')
        self.assertEqual('邮箱', result.text)
        print("------------------邮箱文本正确-----------------------")

    def test_assertCodeContent(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[2]/div[2]').click()
        result = self.driver.find_element_by_xpath('//*[@id="changePass"]/div/form/div/div[2]/label')
        self.assertEqual('验证码', result.text)
        print("------------------验证码文本正确-----------------------")

    def test_emailInboxContent(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[2]/div[2]').click()
        result = self.driver.find_element_by_xpath('//*[@id="changePass"]/div/form/div/div[1]/input')
        self.assertEqual('请输入注册邮箱', result.text)
        print("------------------邮箱输入框默认文本正确-----------------------")

    def test_assertCodeInboxContent(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[2]/div[2]').click()
        result = self.driver.find_element_by_xpath('//*[@id="changePass"]/div/form/div/div[2]/input')
        self.assertEqual('请输入验证码', result.text)
        print("------------------验证码输入框默认文本正确-----------------------")
  # 修改密码成功
    # 输入正确的邮箱和验证码
    def test_enter6digit(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[2]/div[2]').click()
        self.driver.find_element_by_xpath('//*[@id="changePass"]/div/form/div/div[1]/input').sendkeys('lei.jiang@fafafa.io')
        self.driver.find_element_by_xpath('//*[@id="changePass"]/div/form/div/div[2]/input').sendkeys('d16a8f507db64456ad1d536aaae1e762')
        self.driver.find_element_by_xpath('//*[@id="changePass"]/div/form/button').click()
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('重置密码链接发送成功', result.text)
        print("------------------修改密码申请提交成功-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/mine', self.driver.current_url)
            print("跳转我的界面正确")
        except AssertionError:
            print("跳转我的界面错误")
    # 内容为空时查看确认按钮状态

    def test_buttonCheck(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        try:
            self.assertFalse(self.driver.find_element_by_xpath('//*[@id="changePass"]/div/form/button').is_disabled())
            print("确认按钮状态正确，按钮状态为置灰")
        except AssertionError:
            print("确认按钮状态错误，按钮状态为高亮")
   #输入错误的邮箱
    def test_wrongEmail(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('或多或')
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('昵称修改成功', result.text)
        print("------------------昵称修改成功-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/mine', self.driver.current_url)
            print("跳转我的界面正确")
        except AssertionError:
            print("跳转我的界面错误")
    # 输入错误的验证码
    def test_wrongAssertCode(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/span').click()
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/div[1]/input').sendkeys('红河黄精鸡怪')
        self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div/form/button').click()
        result = self.driver.find_element_by_xpath('')
        self.assertEqual('昵称修改成功', result.text)
        print("------------------昵称修改成功-----------------------")
        try:
            self.assertEqual('http://192.168.8.21:8989/mine', self.driver.current_url)
            print("跳转我的界面正确")
        except AssertionError:
            print("跳转我的界面错误")
#公平说明
    #顶栏检查
    def test_fairLanguage(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        try:
            self.driver.find_element_by_xpath('//*[@id="header"]/header/div[2]/button/label').is_undisplayed()
            print('切换语言按钮不可见，正确')
        except AssertionError:
            print('切换语言按钮可见，错误')
    def test_fairTittle(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('//*[@id="changePass"]/div/form/div/div[1]/input')
        self.assertEqual('公平说明', result.text)
        print("------------------公平说明界面标题正确-----------------------")
    def test_fairImage(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        self.assertIsNotNone(self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/img'),'公平说明界面图标不存在,Fail')

    def test_content(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[2]')
        self.assertEqual('防篡改 多重加密 公平公正', result.text)
        print("-------------------防篡改 多重加密 公平公正----------------------")

    def test_MD5(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/p')
        self.assertEqual('MD5是一种广泛使用的加密算法，用于确保信息传输完整一致。本站的所有牌将利用MD5加密生成“摘要”，并于玩家下注前告诉玩家。由于我们无法预知玩家会下什么注，所以便能确保我们无法作弊。当玩家下注完毕后，我们将公布该原始字符（即种子），玩家可利用MD5工具验证该字符是否与下注前的加密字符吻合。因此这是真正公平可信赖的游戏！（维基百科）', result.text)
        print("-------------------MD5文本正确----------------------")

    def test_stealCard(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[3]/div/div[1]/h3')
        self.assertEqual('偷不了牌',result.text)
        print("-------------------偷不了牌----------------------")
    def test_stealCardContent(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[3]/div/div[1]/p')
        self.assertEqual('游戏开始前我们将公布所有牌的“序号”和“摘要”，游戏按照序号顺序进行发牌，序号和摘要具备唯一对应关系，一旦开始任何人无法改变发牌顺序！', result.text)
        print("-------------------偷不了牌文本正确----------------------")

    def test_changeCard(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[3]/div/div[2]/h3')
        self.assertEqual('换不了牌', result.text)
        print("-------------------换不了牌----------------------")

    def test_changeCardContent(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[3]/div/div[2]/p')
        self.assertEqual('牌的花色与点数由“种子”决定，一个种子通过MD5加密算法只能生成一个“摘要”，这意味着摘要一旦公布，任何人都无法篡改游戏结果的“种子”。', result.text)
        print("-------------------换不了牌文本正确----------------------")
    def test_assertFair(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[4]/div[1]')
        self.assertEqual('可验证的公平性', result.text)
        print("-------------------可验证的公平性----------------------")
    def test_assertInfo1(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[4]/div[2]/div[2]')
        self.assertEqual('1，下注前获得全部牌的“序号”与“摘要”。', result.text)
        print("-------------------说明1文本正确----------------------")

    def test_assertInfo2(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[4]/div[2]/div[4]')
        self.assertEqual('2，亮牌后得到牌的“种子”。', result.text)
        print("-------------------说明2文本正确----------------------")

    def test_assertInfo3(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[4]/div[2]/div[3]')
        self.assertEqual('3，利用MD5工具验证“摘要”与“种子”是否吻合。', result.text)
        print("-------------------说明3文本正确----------------------")

    def test_remark(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[4]/p[1]')
        self.assertEqual('注：种子可加密生成摘要，摘要不能逆向计算出种子', result.text)
        print("-------------------注释文本正确----------------------")

    def test_digestInfo(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[4]/div[7]/p')
        self.assertEqual('摘要是由种子加密生成的32位字母和数字的组合。', result.text)
        print("-------------------摘要文本正确----------------------")

    def test_assertAdress(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[5]/p[1]')
        self.assertEqual('真公平不惧任何质疑，我们支持任何第三方MD5工具检验。', result.text)
        print("-------------------验证地址文本正确----------------------")

    def test_assertAdressInfo(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[1]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('/html/body/div/div[4]/div/div[5]/p[2]')
        self.assertEqual('您可以将种子复制到以下或其他网站进行摘要的正确性验证', result.text)
        print("-------------------验证操作文本正确----------------------")
#常见问题
    #常见问题功能验证
    def test_FAQFun(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[2]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/h1')
        self.assertEqual('常见问题', result.text)
        print("-------------------常见问题页面跳转正确----------------------")

    def test_FAQui(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[2]/div[2]/div').click()
        self.assertIsNotNone(self.driver.find_element_by_xpath('//*[@id="header"]/header/div[1]/button/label/img'),'常见问题顶栏log不存在,Fail')
#服务条款
    #服务条款功能验证
    def test_serviceFun(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[3]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/h1')
        self.assertEqual('服务条款', result.text)
        print("-------------------服务条款页面跳转正确----------------------")

    def test_serviceUi(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[3]/div[2]/div').click()
        self.assertIsNotNone(self.driver.find_element_by_xpath('//*[@id="header"]/header/div[1]/button/label/img'),'服务条款顶栏log不存在,Fail')
#关于我们
   #关于我们功能验证
    def test_aboutUsFun(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[4]/div[2]/div').click()
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/h1')
        self.assertEqual('关于我们', result.text)
        print("-------------------关于我们页面跳转正确----------------------")

    def test_aboutUsUi(self):
        self.driver.find_element_by_xpath('//*[@id="mine"]/div[2]/a[4]/div[2]/div').click()
        self.assertIsNotNone(self.driver.find_element_by_xpath('//*[@id="header"]/header/div[1]/button/label/img'),'关于我们顶栏log不存在,Fail')
#底栏检查
    # 首页
    def test_firstPageImage(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[1]/div[1]/img')
        result.is_displayed()
        try:
           self.driver.find_element_by_xpath('//*[@id="footer"]/a[1]/div[1]/img').is_unselected()
           print('底栏我的标签颜色为白色，状态正确')
        except AssertionError:
           print('底栏我的标签按钮为黄色，状态错误')
    def test_firstPageContent(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[1]/div[2]')
        self.assertEquals('首页', result.text)
        print("------------------首页-----------------------")

    # 记录
    def test_recordImage(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[2]/div[1]/img')
        result.is_displayed()
        try:
           self.driver.find_element_by_xpath('//*[@id="footer"]/a[2]/div[1]/img').is_unselected()
           print('底栏我的标签颜色为白色，状态正确')
        except AssertionError:
           print('底栏我的标签按钮为黄色，状态错误')
    def test_recordContent(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[2]/div[2]')
        self.assertEquals('记录', result.text)
        print("------------------记录-----------------------")
    # 账户
    def test_accountImage(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[3]/div[1]/img')
        result.is_displayed()
        try:
           self.driver.find_element_by_xpath('//*[@id="footer"]/a[3]/div[1]/img').is_unselected()
           print('底栏我的标签颜色为白色，状态正确')
        except AssertionError:
           print('底栏我的标签按钮为黄色，状态错误')
    def test_accountContent(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[3]/div[2]')
        self.assertEquals('账户', result.text)
        print("------------------账户-----------------------")

    # 我的
    def test_mineImage(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[4]/div[1]/img')
        result.is_displayed()
        try:
           self.driver.find_element_by_xpath('//*[@id="footer"]/a[4]/div[1]/img').is_selected()
           print('底栏我的标签颜色我黄色，状态正确')
        except AssertionError:
           print('底栏我的标签按钮为白色，状态错误')
    def test_mineContent(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[4]/div[2]')
        self.assertEquals('我的', result.text)
        print("------------------我的-----------------------")


    def test_logoutFun(self):
       self.driver.find_element_by_xpath('//*[@id="mine"]/div[3]/a').click()
       try:
           self.assertEqual('http://192.168.8.21:8989/home', self.driver.current_url)
           print("退出成功")
       except AssertionError:
           print("退出失败")


if __name__ == '__main__':
    unittest.main()


