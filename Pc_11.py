"""

控件及窗口的截图操作

"""

from pywinauto.application import Application

# 启动 navicat
app = Application("uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")

# 通过窗口标题去选择窗口
dlg = app["Navicat Premium"]

# 选择菜单
menu = dlg["Menu"]

# 选择菜单项：文件
file = menu.child_window(title="文件", control_type="MenuItem")

# 截图处理-截图窗口
# pic = dlg.capture_as_image()
# print(pic)
# pic.save('01.png')

# 截图处理-截图菜单
# pic1 = menu.capture_as_image()
# pic1.save('02.png')

# 截图菜单项-文件
pic3 = file.capture_as_image()
pic3.save('03.png')

dlg.close()