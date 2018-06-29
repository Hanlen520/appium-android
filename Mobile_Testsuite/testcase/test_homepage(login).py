    import unittest
from Mobile_Testsuite.testcase.common import Common


class HomePage(unittest.TestCase, Common):
    #set up appium
    def setUp(self):
        print("------------------setUp Test-----------------------")
        Common.__init__(self)
        Common.setup(self)
        Common.login(self)


    def tearDown(self):
        print("------------------tearDown Test-----------------------")
        Common.quit(self)


# 已登录状态首页UI验证

# 页面标题
    def test_title(self):
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/h1')
        self.assertEqual("首页",result.text)

# 平台logo
    def test_logo(self):
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/div[1]/button/label/img')
        result.is_displayed()

# 语言
    def test_language(self):
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/div[2]/button/label')
        self.assertEquals('切换语言',result.text)

# 头像
    def test_headimg(self):
        result = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[1]')
        result.is_displayed()

# 玩家昵称
    def test_nickname(self):
        result = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]')
        self.assertEqual('万年僵尸玩家', result.text)

# 虚拟币
    def test_currencyimg(self):
        result = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/div/div/span[3]/img')
        result.is_displayed()

    def test_currencysum(self):
        result = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/div/div/span[2]/span/b[1]')
        self.assertEqual('0.001', result.text)

    def test_currencybutton(self):
        result = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/div/div/span[1]')
        self.assertEquals('coin-icon', result.get_attribute('class'))



# 公平说明banner图
    def test_bannerimg(self):
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div')
        self.assertEquals('home-game', result.get_attribute('class'))

    def test_game(self):
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/p[1]')
        self.assertEquals('最有趣的百家乐', result.text)

    def test_fair(self):
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/p[2]')
        self.assertEquals('可验证的区块链游戏系统', result.text)

# 百家乐游戏入口
    def test_baccaratimg(self):
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[1]/div/div[1]/img')
        result.is_displayed()

    def test_baccarat(self):
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[1]/div/div[2]/span')
        self.assertEquals('百家乐', result.text)

    def test_baccaratbutton(self):
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[1]/div/div[2]/button')
        self.assertEquals('开始', result.text)

# 21点游戏入口
    def test_BlackJackimg(self):
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[2]/div/div[1]/img')
        result.is_displayed()

    def test_BlackJack(self):
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[2]/div/div[2]/span')
        self.assertEqual('21点', result.text)

    def test_BlackJackbutton(self):
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[2]/div/div[2]/button')
        self.assertEquals('开始', result.text)

# 页面底栏

# 首页
    def test_firstpageimg(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[1]/div[1]/img')
        result.is_displayed()

    def test_firstpage(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[1]/div[2]')
        self.assertEquals('首页', result.text)

#记录
    def test_recordimg(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[2]/div[1]/img')
        result.is_displayed()

    def test_record(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[2]/div[2]')
        self.assertEquals('记录', result.text)

#账户
    def test_accountimg(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[3]/div[1]/img')
        result.is_displayed()

    def test_account(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[3]/div[2]')
        self.assertEquals('账户', result.text)

#我的
    def test_mineimg(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[4]/div[1]/img')
        result.is_displayed()

    def test_mine(self):
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[4]/div[2]')
        self.assertEquals('我的', result.text)


# 已登录状态首页按钮功能验证

# 昵称点击功能

    def test_nickclick(self):
        elementone = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]')
        elementone.click()
        elementtwo = self.driver.find_element_by_xpath('//*[@id="mine"]/div[1]/a[1]/div[2]')
        self.assertEqual('修改昵称',elementtwo.text)

# 百家乐游戏开始按钮

    def test_baccaratbutton(self):
        elementone = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[1]/div/div[2]/button')
        elementone.click()
        elementtwo = self.driver.find_element_by_xpath('//*[@id="header"]/header/h1')
        self.assertEqual('百家乐',elementtwo.text)

# 21点游戏开始按钮

    def test_BlackJackbutton(self):
        elementone = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[2]/div/div[2]/button')
        elementone.click()
        elementtwo = self.driver.find_element_by_xpath('//*[@id="header"]/header/h1')
        self.assertEqual('21点' , elementtwo.text)

# 切换语言按钮

    def test_languagebutton(self):
        elementone = self.driver.find_element_by_xpath('//*[@id="header"]/header/div[2]/button/label')
        elementone.click()
        elementtwo = self.driver.find_element_by_xpath('//*[@id="setlanguage"]/ul/li[1]/a/span[1]')
        self.assertEqual('language-title', elementtwo.get_attribute('class'))

# 切换虚拟币按钮功能

    def test_currencybutton(self):
        elementone = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/div/div/span[1]')
        elementone.click()
        elementtwo = self.driver.find_element_by_xpath('//*[@id="dropdown-menu-610"]/li/div/span[3]')
        self.assertEqual('coin-icon coin-icon-list', elementtwo.get_attribute('class'))


if __name__ == '__main__':
    unittest.main()
