"""
Pywinauto 打开指定的应用程序

"""
# 1.打开 windows自带的记事本

from pywinauto.application import Application
app = Application(backend="uia").start("notepad.exe")
# dlg_spec = app['无标题 - 记事本']
# dlg_spec.print_control_identifiers()

# 打开任意的Windows程序
# app = Application(backend="后端类型").start("程序位置路径")
app = Application(backend="uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")

