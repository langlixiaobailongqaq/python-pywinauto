"""
Pywinauto 连接已经打开的应用程序

"""
from pywinauto.application import Application

# 通过进程号去进行连接- 可以用ViewWizard2.exe 查看进程ID
app = Application("uia").connect(process=10480)
print(app)

# 通过窗口句柄进行连接-可以用ViewWizard2.exe 查看窗口句柄
app1 = Application("uia").connect(handle=198478)
print(app1)