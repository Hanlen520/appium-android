from Mobile_Testsuite.PO.MinePage import MinePage
import unittest
from Mobile_Testsuite.PO.HomePage import HomePage
from Mobile_Testsuite.Untils.server import Server
from Mobile_Testsuite.PO import InitDriver
from Mobile_Testsuite.testcase.common import Common
class mineTestCase(unittest.TestCase,Common):
    @classmethod
    def setUpClass(cls):
            server = Server()
            server.main()

    def setUp(self):
        self.driver = InitDriver.start_driver()
        self.HomePage = HomePage(self.driver)
        self.driver.get('http://192.168.8.21:8989/home')
        self.common = Common(self.driver)
        self.common.login()
        self.MinePage = MinePage(self.driver)
        self.MinePage.click_mine_interface()
    def tearDown(self):
        print("------------------环境初始化-----------------------")
        self.driver.quit()
    def test_ui(self):
        # 确认跳转至我的页面
        title_text = self.MinePage.get_title_text()
        self.assertEqual(title_text, '我的')
        print('我的')
    def test_nicknameFUN(self):
        self.MinePage.click_nickname_btn()
        text=self.MinePage.get_title_text()
        self.assertEqual(text, '我的')
 # 我的界面检查
    def test_logout(self):
        logout_text = self.MinePage.get_logout_text()
        self.assertEqual(logout_text, '退出登录')
        print("退出登录")
#修改昵称
    #修改昵称文本检查
    def test_alterNicknameContent(self):
        modifiedNicknameTittle_text = self.MinePage.get_modifiedNicknameTittle_text()
        self.assertEqual(modifiedNicknameTittle_text, '修改昵称')
        print("------------------修改昵称-----------------------")

    def test__modified_nickname_text(self):
        modified_nickname_text=self.MinePage. get_modified_nickname_text()
        self.assertEqual(modified_nickname_text,'修改昵称')

      #修改昵称按钮功能检查
    def test_alterNicknameFUN(self):
        self.MinePage.click_modified_nickname_btn()
        modifiedNicknameTittle_text = self.MinePage.get_modifiedNicknameTittle_text()
        self.assertEqual(modifiedNicknameTittle_text, '修改昵称')
        print("跳转修改昵称页面正确")
    def test_clearButtonFun(self):
        self.MinePage.click_modified_nickname_btn()
        self.MinePage.click_clear_btn()
        text = self.MinePage.get_inputBOX_text()
        self.assertIsNone(text,'None')
   #修改昵称成功
    def test_input_6digit(self):
        self.MinePage.click_modified_nickname_btn()
        self.MinePage.click_clear_btn()
        self.MinePage.click_input_box().sendkeys('123456')
        self.MinePage.click_modifiedNicknameConfirm_btn()
        self.assertEqual('http://192.168.8.21:8989/home', self.driver.current_url)
        print("------------------昵称修改成功-----------------------")
    #修改昵称失败
        #输入昵称为空
    def test_empty(self):
        self.MinePage.click_modified_nickname_btn()
        self.MinePage.click_clear_btn()
        self.MinePage.click_modifiedNicknameConfirm_btn()
        self.assertEqual('http://192.168.8.21:8989/changename', self.driver.current_url)
        print("------------------昵称为空提示语正确-----------------------")
        #输入的昵称含有特殊字符
    def test_input_specialCharacter(self):
        self.MinePage.click_modified_nickname_btn()
        self.MinePage.click_clear_btn()
        self.MinePage.click_input_box().sendkeys('12@#个')
        self.MinePage.click_modifiedNicknameConfirm_btn()
        self.assertEqual('http://192.168.8.21:8989/changename', self.driver.current_url)
        print("------------------含有特殊字符的昵称提示语正确-----------------------")
#修改密码

    #修改密码按钮文本检查
    def test_modifiedPassword_text(self):
        modifiedPassword_text = self.MinePage.get_modifiedPassword_text()
        self.assertEqual(modifiedPassword_text, '修改密码')
        print("------------------修改密码-----------------------")

#修改密码界面检查
    #顶栏文本检查
    def test_topBarTittleCheck(self):
        self.MinePage.click_modified_password_btn()
        modifiedNicknameTittle_text = self.MinePage.get_modifiedNicknameTittle_text()
        self.assertEqual(modifiedNicknameTittle_text, '修改密码')
        print("------------------修改密码顶栏标题正确-----------------------")
  # 修改密码提交成功成功
    # 输入正确的邮箱和验证码
    def test_enter6digit(self):
        self.MinePage.click_modified_password_btn()
        self.MinePage.click_email_input_box().sendkeys('lei.jiang@fafafa.io')
        self.MinePage.click_assertCode_input_box().sendkeys('d16a8f507db64456ad1d536aaae1e762')
        self.MinePage.click_modifiedPassword_btn()
        self.assertEqual('http://192.168.8.21:8989/changepassword?response_random=5109', self.driver.current_url)
        print("------------------修改密码申请提交成功-----------------------")
        try:

            print("跳转我的界面正确")
        except AssertionError:
            print("跳转我的界面错误")
    # 内容为空时查看确认按钮状态
    def test_buttonCheck(self):
        self.MinePage.click_modified_password_btn()
        self.assertFalse(self.MinePage. modifiedPassword_btn).is_disabled()
   #输入错误的邮箱
    def test_wrongEmail(self):
        self.MinePage.click_modified_password_btn()
        self.MinePage.click_email_input_box().sendkeys('sghafdsf')
        self.MinePage.click_assertCode_input_box().sendkeys('d16a8f507db64456ad1d536aaae1e762')
        self.MinePage.click_modifiedPassword_btn()
        self.assertEqual('http://192.168.8.21:8989/changepassword?response_random=925', self.driver.current_url)
        print("------------------昵称修改成功-----------------------")
    # 输入错误的验证码
    def test_wrongAssertCode(self):
        self.MinePage.click_modified_password_btn()
        self.MinePage.click_email_input_box().sendkeys('lei.jiang@fafafa.io')
        self.MinePage.click_assertCode_input_box().sendkeys('d16a8f507db64456ad1')
        self.MinePage.click_modifiedPassword_btn()
        self.assertEqual('http://192.168.8.21:8989/changepassword?response_random=925', self.driver.current_url)
        print("------------------提示语正确-----------------------")
#公平说明
    def test_fairTittle(self):
        self.MinePage.click_provably_fair_btn()
        fairTittle_text = self.MinePage.get_fairTittle_text()
        self.assertEqual(fairTittle_text,'公平说明')
        print("------------------公平说明界面标题正确-----------------------")
#常见问题
    #常见问题功能验证
    def test_FAQFun(self):
        self.MinePage.click_faq_btn()
        result = self.MinePage.get_faqTittle_text()
        self.assertEqual('常见问题', result.text)
        print("-------------------常见问题页面跳转正确----------------------")
#服务条款
    #服务条款功能验证
    def test_serviceFun(self):
        self.MinePage.click_service_term()
        result = self.MinePage.get_serviceTittle_text()
        self.assertEqual('服务条款', result.text)
        print("-------------------服务条款页面跳转正确----------------------")

#关于我们
   #关于我们功能验证
    def test_aboutUsFun(self):
        self.MinePage.click_about_us_btn()
        result = self.MinePage.get_aboutUsTittle_text()
        self.assertEqual('关于我们', result.text)
        print("-------------------关于我们页面跳转正确----------------------")
#退出按钮功能验证
    def test_logoutFun(self):
       self.MinePage.click_logout_btn()
       result = self.MinePage.get_title_text()
       self.assertEqual('首页', result.text)


if __name__ == '__main__':
    unittest.main()


