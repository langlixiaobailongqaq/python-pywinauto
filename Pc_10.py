"""

窗口控件基本属性获取的方法：
	1.获取控件类型： wrapper object()
	2.获取该控件支持的方法：print(dir(a.wrapper object()))
	3.获取控件的子元素： children
	4.获取控件类名：class_name
	5.以字典形式返回控件的属性：get_properties

"""
from pywinauto.application import Application

# 启动 navicat
app = Application("uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")

# 通过窗口标题去选择窗口
dlg = app["Navicat Premium"]
# 打印窗口中所有的控件
# dlg.print_control_identifiers()

# 选择菜单
menu = dlg["Menu"]

# 选择菜单项：文件
file = menu.child_window(title="文件", control_type="MenuItem")

# 查看控件类型
print(dlg.wrapper_object())
print(menu.wrapper_object())

# 获取该控件支持的方法
print(dir(dlg.wrapper_object()))

# 控件的文本内容获取：texts
print(file.texts())

# 获取控件的子元素
print(dlg.children())

# 获取控件类名
print(dlg.class_name())

# 以字典形式返回控件的属性
print(menu.get_properties())

dlg.close()
