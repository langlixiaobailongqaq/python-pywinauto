"""

项目实战之单个功能操作实现二：
	tag：找不到树状视图控件 TVirtualStringTree,有找到的请联系我
"""
import pywinauto
from pywinauto import mouse
import time

app = pywinauto.Application("uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")
app = pywinauto.Application(backend='uia').connect(process=14928)

# 通过窗口标题去选择窗口
dlg = app["Navicat Premium"]
# dlg.print_control_identifiers()

# # 选择树状视图控件 TVirtualStringTree -找不到这个控件
# dlg['TTreeView'].print_control_identifiers()


# db_name = dlg["TVirtualStringTree"].child_window(title='test1', control_type='TreeItem')
# # 获取数据库连接test1 中心点的位置 mid_point
# rect = db_name.rectangle().mid_point()
# print(rect.x, rect.y)
# 鼠标在控件中心点，右击
# mouse.right_click(coords=(rect.x, rect.y))

# 找不到树状视图控件,只能使用绝对坐标然后点击
# mouse.right_click(coords=(rect.x, rect.y))
time.sleep(2)
mouse.right_click(coords=(151, 325))

# 获取该应用程序所有的窗口
# print(app.window())

# 选择右击出现的上下文窗口
app['上下文'].print_control_identifiers()
# 打开连接
app['上下文']['MenuItem1'].click_input()

# 删除连接
app['上下文']['MenuItem6'].click_input()
time.sleep(1)
# 选择删除窗口
app['TWDialogForm']['删除'].click()

# dlg.close()