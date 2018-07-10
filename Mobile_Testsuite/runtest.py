#######################################################
# FileName:runtest.py
# Author:liketao
# Date:2018-7-4
# Function Description:执行用例，生成报告
#######################################################
import sys
sys.path.append('../../hades')
import os
import time
import unittest
from Mobile_Testsuite import BSTestRunner
from Mobile_Testsuite.Untils.server import Server


class Runner:
    def __init__(self):
        self.basepath = os.getcwd()
        self.testcase_dir = self.get_testcase_dir()
        self.report_dir = self.get_report_dir()

    def get_testcase_dir(self):
        # testcase目录
        testcase_dir = self.basepath + "\\testcase"
        return testcase_dir

    def start_appium_server(self):
        server = Server()
        server.main()

    def create_suite(self):
        # 实例化测试套件
        suite = unittest.TestSuite()
        # 查找目录testcase_dir下以test_开头的测试用例文件.py
        discover = unittest.defaultTestLoader.discover(self.testcase_dir, pattern='test_*.py', top_level_dir=None)
        # 将查找到的测试用例添加到测试套件中
        for test_suite in discover:
            for test_case in test_suite:
                suite.addTest(test_case)
        return suite

    def get_report_dir(self):
        now = time.strftime('%Y-%m-%d-%H-%M')
        report_dir = self.basepath + '\\Testreport\\' + now + '.html'
        return report_dir

    def main(self):
        self.start_appium_server()
        fp =open(self.report_dir, 'wb')
        runner = BSTestRunner.BSTestRunner(stream=fp, title=u'HadesM自动化测试', description=u'自动化测试结果')
        runner.run(self.create_suite())
        fp.close()

if __name__ == '__main__':
    runner = Runner()
    runner.main()










