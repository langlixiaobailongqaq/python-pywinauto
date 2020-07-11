"""

窗口上的控件选择
"""
from pywinauto.application import Application
import pywinauto
import time

# 启动 navicat
app = Application("uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")

# 通过窗口标题选择去选择窗口
dlg = app['Navicat Premium']

# 打印窗口中所有的控件
# dlg.print_control_identifiers()

# 方式一。根据窗口类名选择窗口
# menu = dlg.Menu
# menu.print_control_identifiers()


# 打印菜单的控件
menu = dlg['Menu']
# menu.print_control_identifiers()

# 选择控件，方式二-此方式无法找到，报错
# file = dlg['MenuItem']['文件']
# file.print_control_identifiers()

# 选择控件-方式三
file = menu.child_window(title="文件", control_type="MenuItem")
file.print_control_identifiers()