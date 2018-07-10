#######################################################
# FileName:InitDriver.py
# Author:liketao
# Date:2018-6-20
# Function Description:
#######################################################

from appium import webdriver
import os

# 读取设备 id
readDeviceId = list(os.popen('adb devices').readlines())
deviceId = readDeviceId[1]

# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = deviceAndroidVersion[0]

# Appium的Desired Capabilities
dis_browser = {}
dis_browser['platformName'] = 'Android'
dis_browser['platformVersion'] = deviceVersion
dis_browser['deviceName'] = deviceId
dis_browser['browserName'] = 'chrome'
dis_browser['unicodeKeyboard'] = True

# 隐藏手机中的软键盘
dis_browser['resetKeyboard'] = True

# Appium-server启动主机和端口
server_url = 'http://localhost:4700/wd/hub'

# Appium启动session
def start_driver():
    print('Start Driver...')
    driver = webdriver.Remote(server_url, dis_browser)
    return driver

