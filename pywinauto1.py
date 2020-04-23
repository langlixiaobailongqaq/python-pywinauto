

from pywinauto.application import Application
import time

app = Application(backend="uia").start('notepad.exe')

# app = Application().start('notepad.exe')
time.sleep(1)
app[' 无标题 - 记事本 '].menu_select("编辑(&E) -> 替换(&R)..")
time.sleep(1)
app['替换'].取消.click()

# 没有with_spaces 参数空格将不会被键入。请参阅SendKeys的这个方法的文档，因为它是SendKeys周围的薄包装。
app[' 无标题 - 记事本 '].Edit.type_keys("Hi from Python interactive prompt %s" % str(dir()), with_spaces = True)

app[' 无标题 - 记事本 '].menu_select('文件(&F) -> 退出(&X)')

# 在这时候不清楚“不保存”的按钮名就对app['记事本'] 使用print_control_identifiers()
app['记事本'].Button2.click()


# 查到这个记事本的控件树
# dlg_spec = app['无标题 - 记事本']
# dlg_spec.print_control_identifiers()

