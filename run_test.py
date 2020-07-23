import unittest
from Pc_21 import TestConnect
from BeautifulReport import BeautifulReport

"""
使用BeautifulReport库生成 测试报告
"""

# 创建一个测试套件
suite = unittest.TestSuite()
# 将测试用例类中的所有用例加载到套件
suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestConnect))

# unittest自带的testrunner来运行套件
# runner = unittest.TextTestRunner()
# runner.run(suite)

result = BeautifulReport(suite)
result.report(description='pc自动化测试', filename="PC端自动化测试报告", report_dir=".")