"""

键盘修饰符的使用：
	# 打印按键属性
	print(dir(k))

"""

# 导入模块
from pykeyboard import PyKeyboard
import time

k = PyKeyboard()
# # 按 ， 号键
# k.press_key(",")
# k.release_key(",")
#
# # 按 shit+ / 键
# k .press_keys([k.shift_key, '/'])

# 联合按键-按ctrl + s
k.press_key(k.control_key)
k.tap_key("c")
k.release_key(k.control_key)

# 打印按键属性
print(dir(k))

