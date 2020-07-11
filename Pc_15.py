"""

编辑类型(Edit)的控件操作：


"""
from pywinauto import Application

app = Application().start("notepad.exe")
# 选择主窗口
dlg = app["无标题 - 记事本"]
dlg.print_control_identifiers()
# 选择编辑框
dlg["Edit"].type_keys("pywinauto自动化666")

# 替换操作-通过菜单项选择替换
dlg.menu_select("编辑->替换(R)")

# 选择替换窗口并打印控件
app["替换"].print_control_identifiers()
# 选择查找编辑框
app["替换"]["Edit1"].type_keys("666")

# 选择替换为编辑框
app["替换"]["Edit2"].type_keys("9999")

# 选择全部替换按钮，进行点击
app["替换"]["Button3"].click()