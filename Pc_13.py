"""
pywinauto中的等待机制1：

等待机制一：
	wait方法：
		作用：等待窗口处于某个状态
		参数：
			wait_for：等待的状态(有以下几种)
				exists：表示该窗口是有效的句柄
				visible：表示该窗口未隐藏
				enabled：表示未禁用窗口
				ready：表示该窗口可见并启用
				active：表示该窗口处于活动状态
			timeout：超时时间
			retry_interval：重试时间间隔

等待机制一：
	wait_not wait方法：
		作用：等待窗口处于不可见状态

等待机制三：
	wait_cpu_usage_lower 方法：
		作用：等待该进程的cpu的使用率低于某个阙值。
		注意：此方法仅适用于整个应用程序进程，不适应于窗口/元素。
		参数：
			threshold：该进程cpu占用率
			timeout：超时时间
			retry_interval：重试时间间隔

"""
from pywinauto.application import Application

# # 启动 navicat
# app = Application("uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")

# # 通过窗口标题去选择窗口
# dlg = app["Navicat Premium"]

# # 选择菜单
# menu = dlg["menu"]

# # 选择菜单项：文件
# file = menu.child_window(title="文件", control_type="MenuItem")

# # 点击文件
# file.click_input()
# # 点击新建连接
# menu.item_by_path("文件->新建连接").click_input()
# # 点击MySQL...
# menu.item_by_path("文件->新建连接->MySQL...").click_input()

# # 选择新建连接的窗口
# new_dlg = app["MySQL - 新建连接"]

# # 等待窗口处于可见状态
# # new_dlg.wait(wait_for="ready", timeout=10, retry_interval=1)
# # print("等待通过,当前新建连接的窗口处于可见状态")

# # 等待窗口处于不可见状态-关闭[MySQL - 新建连接] 窗口则通过
# new_dlg.wait_not(wait_for_not="ready", timeout=10, retry_interval=1)
# print("等待通过,当前新建的窗口不处于可见状态")


# 等待机制三：wait_cpu_usage_lower 方法 ,通过夜深模拟器的 pid(进程ID) 进行连接
app = Application().connect(process=6044)
app.wait_cpu_usage_lower(threshold=5, timeout=5, usage_interval=1)
print("等待通过,CPU占用率低于%5")