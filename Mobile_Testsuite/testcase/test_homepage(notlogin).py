import unittest
from Mobile_Testsuite.testcase.common import Common


class HomePage(unittest.TestCase, Common):
    def setUp(self):
        print("------------------setUp Test-----------------------")
        Common.__init__(self)
        Common.setup(self)

    def tearDown(self):
        print("------------------tearDown Test-----------------------")
        Common.quit(self)

# 未登录状态首页UI验证

# 页面标题
    def test_title(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/h1')
        self.assertEqual("首页",result.text)

# 平台logo
    def test_logo(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/div[1]/button/label/img')
        result.is_displayed()

 # 语言
    def test_language(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="header"]/header/div[2]/button/label')
        self.assertEquals('切换语言', result.text)

# 头像
    def test_headimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[1]')
        self.assertEqual('home-login-icon', result.get_attribute('class'))

# 登录/注册
    def test_register(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]')
        self.assertEquals('登录/注册', result.text)

 # 公平说明banner图
    def test_bannerimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div')
        self.assertEqual('home-game', result.get_attribute('class'))

    def test_game(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/p[1]')
        self.assertEquals('最有趣的百家乐', result.text)

    def test_fair(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/p[2]')
        self.assertEquals('可验证的区块链游戏系统', result.text)

# 百家乐游戏入口
    def test_baccaratimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[1]/div/div[1]/img')
        result.is_displayed()

    def test_baccarat(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[1]/div/div[2]/span')
        self.assertEquals('百家乐', result.text)
#
    def test_baccaratbutton(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[1]/div/div[2]/button')
        self.assertEquals('开始', result.text)

# 21点游戏入口
    def test_BlackJackimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[2]/div/div[1]/img')
        result.is_displayed()

    def test_BlackJack(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[2]/div/div[2]/span')
        self.assertEqual('21点', result.text)

    def test_BlackJackbutton(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[2]/div/div[2]/button')
        self.assertEqual('开始', result.text)

# 页面底栏

# 首页
    def test_firstpageimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[1]/div[1]/img')
        result.is_displayed()

    def test_firstpage(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[1]/div[2]')
        self.assertEquals('首页', result.text)

#记录
    def test_recordimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[2]/div[1]/img')
        result.is_displayed()

    def test_record(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[2]/div[2]')
        self.assertEquals('记录', result.text)

#账户
    def test_accountimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[3]/div[1]/img')
        result.is_displayed()

    def test_account(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[3]/div[2]')
        self.assertEquals('账户', result.text)

#我的
    def test_mineimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[4]/div[1]/img')
        result.is_displayed()

    def test_mine(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="footer"]/a[4]/div[2]')
        self.assertEqual('我的', result.text)


# 公平性说明

# md5标题

    def test_md5title(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[1]')
        self.assertEqual('防篡改的MD5加密确保游戏公平', result.text)

# md5定义

    def test_md5definitionimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[2]/div[1]/img')
        result.is_displayed()

    def test_md5definitiontitle(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[2]/div[2]')
        self.assertEqual('什么是MD5？', result.text)

    def test_md5definitiontxt(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[2]/div[3]')
        self.assertEqual('MD5是一种广泛使用的加密算法，用于确保信息传输完整一致。它能将一段字符加密运算成另一段字符，这两段字符具备不可篡改的对应性。（维基百科）' , result.text)

# 种子定义

    def test_seeddefinitionimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[3]/div[1]/img')
        result.is_displayed()

    def test_seeddefinitiontitle(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[3]/div[2]')
        self.assertEqual('什么是种子？', result.text)

    def test_seeddefinitiontxt(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[3]/div[3]')
        self.assertEqual('“种子”就是未加密的字符，它包含了牌的花色与点数信息，系统会在亮牌后公布给所有玩家。',result.text)

# 摘要定义

    def test_digestdefinitionimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[4]/div[1]/img')
        result.is_displayed()

    def test_digestdefinitiontitle(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[4]/div[2]')
        self.assertEqual('什么是摘要？', result.text)

    def test_digestdefinitiontxt(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[4]/div[3]')
        self.assertEqual('“摘要”就是将“种子”加密后的字符，在下注前便会显示给玩家。亮牌后玩家便可利用MD5工具验证“摘要”与“种子”是否吻合。', result.text)


# 偷不了牌

    def test_stealcardsimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[5]/div[1]/div[1]/img')
        result.is_displayed()

    def test_stealcardstitle(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[5]/div[1]/div[2]')
        self.assertEqual('偷不了牌！', result.text)

    def test_stealcardstxt(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[5]/div[1]/div[3]')
        self.assertEqual('游戏开始前我们将公布所有牌的“序号”和“摘要”，游戏按照序号顺序进行发牌，序号和摘要具备唯一对应关系，一旦开始任何人无法改变发牌顺序！', result.text)

# 换不了牌

    def test_changecardsimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[5]/div[2]/div[1]/img')
        result.is_displayed()

    def test_changecardstitle(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[5]/div[2]/div[2]')
        self.assertEqual('换不了牌！', result.text)

    def test_changecardstxt(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[2]/div[5]/div[2]/div[3]')
        self.assertEqual('牌的花色与点数由“种子”决定，一个种子通过MD5加密算法只能生成一个“摘要”，这意味着摘要一旦公布，任何人都无法篡改游戏结果的“种子”。', result.text)

# 可验证的公平性

# 验证流程部分

    def test_fairnesstitle(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[1]')
        self.assertEqual('可验证的公平性', result.text)

    def test_fairnessimg(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[2]/div[1]/img')
        result.is_displayed()

    def test_fairnesstxtone(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[2]/div[2]')
        self.assertEqual('1，下注前获得全部牌的“序号”与“摘要”。' , result.text)

    def test_fairnesstxttwo(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[2]/div[4]')
        self.assertEqual('2，亮牌后得到牌的“种子”。' , result.text)

    def test_fairnesstxtthree(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[2]/div[3]')
        self.assertEqual('3，利用MD5工具验证“摘要”与“种子”是否吻合。', result.text)

# 验证例子

    def test_exampleseed(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[3]/div[1]/img')
        result.is_displayed()

    def test_seedintroduce(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[3]/div[2]')
        self.assertEqual('“种子”由随机字符组成，前两个字符决定了牌的点数与花色，第一位数字1代表A,2-9代表2-9点，T代表10点，第二位的字母S、H、D、C分别代表黑桃、红桃、方块和梅花。' , result.text)

    def test_examplearrow(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[3]/div[3]/img')
        result.is_displayed()

    def test_exampledigest(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[3]/div[4]/img')
        result.is_displayed()

    def test_digestintroduce(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        result = self.driver.find_element_by_xpath('//*[@id="home"]/div[3]/div[3]/div[5]')
        self.assertEqual('摘要是由种子加密生成的32位字母和数字的组合。', result.text)







# 未登录状态首页的按钮功能验证

# 登录/注册按钮

    def test_registerbutton(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        elementone = self.driver.find_element_by_xpath('//*[@id="loginRegister"]/a/span[2]')
        elementone.click()
        elementtwo = self.driver.find_element_by_xpath('//*[@id="form_login"]/div[1]/input')
        self.assertEqual('inputBox-input theme-5-1 oattvisible',elementtwo.get_attribute('class'))

# 百家乐游戏开始按钮

    def test_baccaratbutton(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        elementone = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[1]/div/div[2]/button')
        elementone.click()
        elementtwo = self.driver.find_element_by_xpath('//*[@id="form_login"]/div[1]/input')
        self.assertEqual('inputBox-input theme-5-1 oattvisible',elementtwo.get_attribute('class'))

# 21点游戏开始按钮

    def test_BlackJackbutton(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        elementone = self.driver.find_element_by_xpath('//*[@id="home"]/div/div/a[2]/div/div[2]/button')
        elementone.click()
        elementtwo = self.driver.find_element_by_xpath('//*[@id="form_login"]/div[1]/input')
        self.assertEqual('inputBox-input theme-5-1 oattvisible' , elementtwo.get_attribute('class'))

# 切换语言按钮
    def test_languagebutton(self):
        self.driver.get('http://192.168.8.21:8989/home?c=ndydoe')
        elementone = self.driver.find_element_by_xpath('//*[@id="header"]/header/div[2]/button/label')
        elementone.click()
        elementtwo = self.driver.find_element_by_xpath('//*[@id="setlanguage"]/ul/li[1]/a/span[1]')
        self.assertEqual('language-title' , elementtwo.get_attribute('class'))


if __name__ == '__main__':
    unittest.main()
