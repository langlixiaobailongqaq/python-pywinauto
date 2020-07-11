"""

模拟键盘的基本操作：
键盘操作模块：pywinauto.keyboard（send_keys方法找不到）
	Send_keys方法：
		使用方式：send_keys(按键)
	例如：
		按F5：send_keys({VK_F5})
		按F12：send_keys({VK_F12})
		按回车键：send_keys({VK_RETURN})
		按普通字母键：send_keys('A')
					send_keyss('B')

二.使用 pykeyboard 模块进行键盘操作：
	1.注意：一定要操作进行完释放(松开)操作，否则会一直按着操作的键
	2.官方文档资料：https://pypi.org/project/PyUserInput/
	3.键盘对应的按键方法，可以ctrl+B 进入PyKeyboard类查看相关方法

"""

# 导入模块
# from pywinauto.keyboard import send_keys  # keyboard 模块里没有send_keys方法
from pykeyboard import PyKeyboard
import time


k = PyKeyboard()
# 按一个键
# k.press_key('H')

# # 释放H,注意：一定要操作进行完释放(松开)操作，否则会一直按着操作的键
# k.release_key('H')

# # 您可以“点击”同时执行以下操作的键
# k.tap_key('e')

# # 注意，tap_key确实支持一种重复击键的方式，每次击键之间都有间隔时间
# k.tap_key('l', n=2, interval=5)
#
# # 也可以根据需要发送一个字符串
# k.type_string('o World!')


# # 支持各种特殊的按键输入-创建一个Alt + Tab组合(联合按键模拟)
# k.press_key(k.alt_key)
# k.tap_key(k.tab_key)
# k.release_key(k.alt_key)

# k.tap_key(k.function_keys[5])  # 点按F5
# k.tap_key(k.numpad_keys['Home'])  cmd# 点击数字键盘上的“主页”
# k.tap_key(k.numpad_keys[5], n=3)  # 点按数字键盘上的5，三次


# 还可以使用press_keys方法一起发送多个击键（例如，访问键盘快捷键时）
# 按 windows+r 键(组合键不用执行松开操作)
k.press_keys([k.windows_l_key, 'r'])
time.sleep(1)
# 输入cmd
k.press_keys(['c', 'm', 'd'])
time.sleep(1)
# 回车
k.press_key(k.enter_key)
k.press_key(k.enter_key)
time.sleep(2)
# 输入 python(只能英文，输入中文时失败)
k.type_string('python')