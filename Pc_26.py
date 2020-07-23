"""

项目实战之Unittest编写自动化用例：

"""
import unittest
from Pc_25 import NavicatTest
import time
import pywinauto


# 定义测试用例类
class TestConnect(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.nav = NavicatTest(path=r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")
		time.sleep(3)

	def test_add_connect_pass(self):
		"""添加连接成功的用例"""
		# # 第一步：准备用例数据
		data = {
			"title": "test2",
			"user": "root",
			"password": "Zx123456"
		}
		expected = {
			"count": 1,
			"title": "test2"
		}
		# 执行用例之前，要去获取连接数量
		start_count = self.nav.get_connect_count()
		# 第二步：执行页面操作
		self.nav.new_connect(**data)
		# 执行用例之后，要去获取所有的连接名
		end_count = self.nav.get_connect_count()
		# 执行用例之后，要去获取所有的连接名
		end_names = self.nav.get_connect_names()
		# 第三步：比对预期结果和实际结果
		print("预期的连接数量为：{},实际的连接数量为{}".format(expected["count"]), end_count)
		# 断言连接数量
		self.assertEqual(expected["count"], end_count-start_count)
		# 断言连接名
		self.assertIn(expected["title"], end_names)