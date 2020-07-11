"""
菜单控件的操作方法：

菜单(Menu)的方法：
	items:获取所有的子菜单
	item_by_index：根据索引选定的菜单项
	item_by_path：根据路径指定菜单项

菜单项相关操作：
	items：获取所有的子选项
	click_input：点击菜单

"""

from pywinauto.application import Application

# 启动 navicat
app = Application("uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")

# 通过窗口标题去选择窗口
dlg = app["Navicat Premium"]

# 选择菜单
menu = dlg["menu"]

# 获取所菜单中所有的子菜单
print(menu.items())

# 通过下标去选择菜单项
m = menu.item_by_index(0)
print(m)

# 通过路径去选择菜单项 item_by_path
m1 = menu.item_by_path('文件->新建连接')
print(m1)

# 选择菜单项：文件
file = menu.child_window(title="文件", control_type="MenuItem")
# click_input：点击菜单
file.click_input()

dlg.close()