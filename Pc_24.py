"""

项目实战之单个功能操作实现二：
"""
import pywinauto

app = pywinauto.Application("uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")
# app = pywinauto.Application(backend='uia').connect(process=11328)
# 通过窗口标题去选择窗口
dlg = app["Navicat Premium"]


# 选择树状视图控件
# dlg["PanelDockHostTListView"].print_control_identifiers()
# dlg['TVTFilterFrame'].TVirtualStringTree.print_control_identifiers()
# dlg["ActionMainMenuBarTActionMainMenuBar"].print_control_identifiers()
# app.window(handle=3876).print_control_identifiers()

db_name = dlg["PanelDockHostPane"]
rest = db_name.rectangle().mid_point()
print(rest)
