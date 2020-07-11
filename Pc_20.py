"""

隐藏通知区域的窗口检测和操作：

"""

from pywinauto import Application
import time

app = Application('uia').connect(path="explorer")

# 使用窗口句柄-找到任务栏(用户提示通知区域)
task = app.window(handle=65892)
task.print_control_identifiers()


# win10系统-任务栏设置-选择哪些图标显示在任务栏上-关闭 通知区域始终显示所有图标
# 打印"通知 V 形"控件
task1 = app.window(handle=65876)
task1.print_control_identifiers()
time.sleep(1)

# 点击 用户提示通知区域里的-通知 V 形(显示隐藏的图标)
task2 = task['Button'].window(handle=65876)
task2.click()
time.sleep(1)

# 选择通知溢出的窗口，然后进行相关的操作
# 直接选择[通知溢出]找不到控件,使用inspect.exe先找到pid连接 后再进行选择控件
app1 = Application("uia").connect(process=1292)
print(app)
# 打印通知 V 形 下的应用程序控件
app1['通知溢出'].print_control_identifiers()
# 打开QQ：Button8
app1['通知溢出']['Button8'].click()


# 使用窗口句柄连接-打印任务栏下的所有信息
app1 = Application("uia").connect(process=1292)
# app1['任务栏']['运行中的应用程序'].print_control_identifiers()
app1['任务栏'].print_control_identifiers()

# 点击 运行中的应用程序-谷歌浏览器(尝试用 [用户提示通知区域]['Google Chrome - 1 个运行窗口']无法找到控件,改为用父窗体[任务栏])
app1['任务栏']['Google Chrome - 1 个运行窗口'].click()