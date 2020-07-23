"""

pywinauto结合selenium实现文件上传：
	文件上传练习地址：https://www.layui.com/demo/upload.html
"""
from selenium import webdriver
import pywinauto
# 键盘操作模块
from pykeyboard import PyKeyboard
import time
import unittest


class TestConnect(unittest.TestCase):
	def setUp(self):
		print("测试开始")

	def test001_upload(self):
		url = "https://www.layui.com/demo/upload.html"
		browser = webdriver.Chrome()
		# 访问图片上传的URL
		browser.get(url=url)
		# 点击图片上传按钮,打开文件选择窗口
		browser.find_element_by_xpath("//*[@id='test1']").click()

		# 使用pywinauto来选择文件-Desktop桌面应用程序对象
		app = pywinauto.Desktop()
		# 选择文件上传的窗口
		dlg = app['打开']
		dlg.print_control_identifiers()

		# 选择文件地址输入框
		dlg['地址: Admin'].click()
		k = PyKeyboard()
		# 输入图片文件夹地址(可以直接输入图片地址后回车,考虑到后期使用时可以作为两个变量，就分两步走)
		# k.type_string(r'C:\Users\Admin\Desktop\亚索图片\2.jpg')
		# type_string不支持中文,建议改成英文文件夹名称
		k.type_string(r"C:\Users\Admin\Desktop\yasuo_images")
		time.sleep(1)

		# 回车
		k.press_key(k.enter_key)
		time.sleep(1)
		k.press_key(k.enter_key)
		time.sleep(1)

		# 选择文件名输入框
		dlg["文件名(&N):Edit"].click()
		k.type_string('2.jpg')
		# 回车
		k.press_key(k.enter_key)

		# 点击 打开
		dlg['打开(&O)'].click()

	def test002_upload(self):
		print("测试002")

	def tearDown(self):
		print("测试结束")
