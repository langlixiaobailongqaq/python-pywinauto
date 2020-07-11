"""

任务栏通知区域的操作：
Pywinauto如何访问系统通知区域：
	方式一：通过Explorer：
		在时钟附近有表示正在运行的应用程序的图标，该区域通常被称为"系统托盘",
		也称为通过区域。该区域的访问,可以通过启动"Explorer.exe"这个应用程序	,
		可以在'任务栏'这个窗口中找到有标题为"用户提示通知区域"的工具栏控件。
	# 底部状态栏
	# icons = app['任务栏']['用户提示通知区域']


"""
from pywinauto.application import Application
import time

# 连接Explorer
app = Application(backend="uia").connect(path="explorer")

# 使用[任务栏] 查找控件失败，尝试用 ViewWizard找到 窗口句柄后尝试成功
# task = app["任务栏"]
# app.print_control_identifiers()
# task = app["任务栏"].child_window(title="用户提示通知区域", auto_id="1504", control_type="ToolBar")
# task.print_control_identifiers()


# -前提条件：通知区域始终显示所有图标-win10系统在 -任务栏设置-选择哪些图标显示在任务栏上
# 使用窗口句柄-找到任务栏(用户提示通知区域)
task = app.window(handle=65892)
time.sleep(1)
task.print_control_identifiers()

# 点击任务栏的模拟器
task.child_window(title="夜神模拟器-62001", control_type="Button").click()



