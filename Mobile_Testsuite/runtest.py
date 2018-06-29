#######################################################
# FileName:runtest.py
# Author:liketao
# Date:2018-6-20
# Function Description:执行用例，生成报告
#######################################################

# from Mobile_Testsuite.testsuite.report import report
# import os
# from Mobile_Testsuite.untils.log import LOG
# if __name__ == "__main__":
#     LOG.info('UI自动化测试开始执行')
#     basepth = os.getcwd()
#     path = basepth+'\\testcase'
#     report(casepath=path)
#     LOG.info('UI自动化测试执行完毕！')

import HTMLTestRunner
import os
import time
import unittest
from Mobile_Testsuite import BSTestRunner
from Mobile_Testsuite.untils.log import LOG

# 当前工作目录
basepath = os.getcwd()
# testcase目录
testcase_dir = basepath + "\\testcase"


def create_suite():
    # 实例化测试套件
    suite = unittest.TestSuite()

    # 查找目录testcase_dir下以test_开头的测试用例文件.py
    discover = unittest.defaultTestLoader.discover(testcase_dir, pattern='test_*.py', top_level_dir=None)

    # 将查找到的测试用例添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTest(test_case)
    return suite


now = time.strftime('%Y-%m-%d-%H-%M')
report_dir = basepath + '\\testreport\\' + now + '.html'
LOG.info('测试报告路径为：%s' % report_dir)

all_test_cases = create_suite()
fp = open(report_dir, 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='HadesM自动化测试报告', description='自动化测试结果')
runner = BSTestRunner.BSTestRunner(stream=fp, title=u'HadesM自动化测试', description=u'自动化测试结果')

LOG.info('UI自动化测试开始执行')
runner.run(all_test_cases)
fp.close()
LOG.info('UI自动化测试执行完毕！')
