from appium import webdriver
from Mobile_Testsuite.Untils.write_user_command import WriteUserCommand


class BaseDriver:
    def android_driver(self):
        print("this is android_driver:", 0)
        write_file = WriteUserCommand()
        devices = write_file.get_value('user_info_0' , 'deviceName')
        plantformversion = write_file.get_value('user_info_0', 'platformVersion')
        port = write_file.get_value('user_info_0', 'port')
        capabilites = {
            "platformName": "Android",
            "deviceName": devices,
            "plantformVersion": plantformversion,
            "browserName": "chrome",
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }
        driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", capabilites)

        return driver
