"""

Pywinauto 选择指定的窗口：
	1.根据窗口标题或类名选择
	dlg = app[窗口类名/标题]

	2.根据窗口类名选择窗口
	dlg = app.窗口类名

	# 非英文程序，推荐使用方式1
"""

from pywinauto.application import Application
import time

# 启动 navicat - 需要先关闭要打开的程序，否则打印所有的控件可能会失败
Application().start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")
# 连接
app = Application(backend="uia").connect(path="navicat.exe", title="Navicat Premium'")

# 一.使用类名/窗口标题来选择窗口
# dlg = app['Navicat PremiumDialog']
# dlg = app['Navicat Premium']
# time.sleep(2)

# 方式二.根据窗口类名选择窗口：app.窗口类名
dlg = app.NavicatPremiumDialog
time.sleep(2)

# 打印窗口中所有的控件
dlg.print_control_identifiers()
