"""

项目实战之单个功能操作实现一：
	写pywinauto脚本小技巧：
		1.启动之后，连接启动的程序，然后可以注释掉启动和已经写好的脚本，继续往下写(不要关闭已经打开的程序)
		2.输入方法：a.pywinauto有自带的type_keys()方法
					b.也可以用 PyKeyboard模块,注意需要先点击后再切换输入法
"""
import pywinauto
import time
# 键盘操作模块
from pykeyboard import PyKeyboard
# 鼠标模块
from pywinauto import mouse


# 启动 navicat
app = pywinauto.Application("uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")
# app = pywinauto.Application(backend='uia').connect(process=14928)

# 通过窗口标题去选择窗口
dlg = app["Navicat Premium"]
dlg.maximize()
time.sleep(1)

# 选择菜单
menu = dlg["menu"]
# menu.print_control_identifiers()

# 选择菜单项：文件
file = menu.child_window(title="文件", control_type="MenuItem")
# 点击文件
file.click_input()

# 点击新建连接
menu.item_by_path("文件->新建连接").click_input()
# 点击MySQL...
menu.item_by_path("文件->新建连接->MySQL...").click_input()

# 选择新建连接的窗口
new_dlg = app["MySQL - 新建连接"]
# # new_dlg.print_control_identifiers()

# 选择常规
new_dlg['常规'].print_control_identifiers()
# 输入连接名
new_dlg['常规'].Edit5.type_keys('test1')

# 用户名
new_dlg['常规'].Edit3.type_keys('root')
# 用户名
new_dlg['常规'].Edit2.type_keys('Zx123456')
new_dlg['连接测试'].click()
# 点击 连接测试窗口的 确定
new_dlg['TButton'].click()

# 点击确定
new_dlg['确定'].click()
time.sleep(2)

dlg.close()