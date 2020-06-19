"""

实现多文件上传及代码封装：
	多图片上传练习地址：https://www.layui.com/demo/upload.html

"""
from selenium import webdriver
import pywinauto
# 键盘操作模块
from pykeyboard import PyKeyboard
import time

url = "https://www.layui.com/demo/upload.html"
browser = webdriver.Chrome()
# 访问图片上传的URL
browser.get(url=url)

# 点击多图片上传按钮,打开文件选择窗口
browser.find_element_by_id("test2").click()


def upload_files(file_path, file, *args):
	# 使用pywinauto来选择文件-Desktop桌面应用程序对象
	app = pywinauto.Desktop()
	# 选择文件上传的窗口
	dlg = app['打开']
	dlg.print_control_identifiers()

	# 选择文件地址输入框
	dlg['地址: Admin'].click()
	k = PyKeyboard()
	# 输入图片文件夹地址
	k.type_string(r"C:\Users\Admin\Desktop\yasuo_images")
	time.sleep(1)

	# 回车
	k.press_key(k.enter_key)
	time.sleep(1)
	k.press_key(k.enter_key)
	time.sleep(1)

	# 选择文件名输入框-
	dlg["文件名(&N):Edit"].click()
	# 输入文件名时，系统默认了中文输入法,输入一个双引号会显示两个双引号
	# 切换输入法
	k.tap_key(k.shift_key)
	time.sleep(1)

	# 输入第一个文件名并加上双引号
	k.type_string('"{}"'.format(file))
	for i in args:
		# 输入第二个文件名并加上双引号
		# 遍历不定长参数中的文件名
		k.type_string('"{}"'.format(i))
		time.sleep(1)
	# 回车时就直接打开了，不用执行 打开操作
	k.press_key(k.enter_key)
	time.sleep(1)

	# 点击 打开
	# dlg['打开(&O)'].click()


upload_files(r"C:\Users\Admin\Desktop\yasuo_images", "2.jpg", "3.jpg")