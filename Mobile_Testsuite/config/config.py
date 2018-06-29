import os
from Mobile_Testsuite.untils.log import logger


# 读取设备 id
readDeviceId = list(os.popen('adb devices').readlines())
deviceId = readDeviceId[1]

# 读取设备系统版本号
deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
deviceVersion = deviceAndroidVersion[0]
'''
配置app以及测试设备的相关信息
'''
@logger('开始读取测试配置')
def make_dis():
    dis_browser = {}
    dis_browser['platformName'] = 'Android'
    dis_browser['platformVersion'] = deviceVersion
    dis_browser['deviceName'] = deviceId
    dis_browser['browserName'] = 'chrome'
    dis_browser['unicodeKeyboard'] = True
    # 隐藏手机中的软键盘
    dis_browser['resetKeyboard'] = True
    return dis_browser
