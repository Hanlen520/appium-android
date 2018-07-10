# 移动端
-----------------

### 运行环境要求
-----------------
- Python 3.6
- node.js 8.11.3
- npm 6.1.0
- Appium 1.8.1
- Android SDK(or adb),Enable ADB setting on device and connect your android device using usb with your PC.

### 目录结构
* Mobile_Testsuite <br>
    * config：配置app以及测试设备的相关信息
    * PO: PO模式，分离测试对象（元素对象）和测试脚本（用例脚本）
        * BasePage：基类，重新封装的元素定位方法
        * InitDriver：Appium-python-client启动器
        * xxxPages: 其他所有页面类
    * testcase：测试用例及公共方法
        * Democase:示范性用例
        * test_xxx:测试用例
        * common:测试用例公共方法
    * testreport：测试报告/报错截图
    * untils： 工具库
    * runtest.py 在testcase中收集并运行测试用例、生成测试报告

## 使用方法
-----------------
> 
step1：使用USB连接测试设备到PC并允许usb调试 <br>
step2：运行runtest.py <br>
