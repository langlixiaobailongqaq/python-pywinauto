"""

应用程序的窗口的操作方法：
	1.窗口最大化：Dlg.maximize()
	2.窗口最小化：Dlg.minimize()
	3.还原窗口正常大小：Dlg.restore
	4.获取窗口显示状态：Dlg.get_show_state()
	5.关闭窗口：Dlg.close
	6.获取窗口坐标：Dlg.rectangle()


"""
from pywinauto.application import Application
import pywinauto
import time

# 启动navicat-操作时改为 "uia",获取窗口显示状态无法获取，要改为 win32
app = Application("uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")

# 通过窗口标题选择去选择窗口
dlg = app['Navicat Premium']
# 窗口最大化
dlg.maximize()
time.sleep(1)

# 窗口最小化
# dlg.minimize()

# 还原窗口正常大小
# dlg.restore()

# 获取窗口显示状态- uia无法获取，要改为 win32。 最大化：1，正常：0
# status = dlg.get_show_state()
# print(status)

# 获取窗口坐标
coordinate = dlg.rectangle()
print(coordinate)

# 关闭窗口
dlg.close()