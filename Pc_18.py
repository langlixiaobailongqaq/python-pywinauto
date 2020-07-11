"""

模拟用户鼠标操作：
鼠标操作模块：Pywinauto.mouse
	press：按下鼠标
	repleace：释放鼠标
	move：鼠标移动
	scroll：滚动鼠标

"""

from pywinauto import mouse

# 鼠标单击(默认左键)- 点击x轴坐标：214, y轴坐标：50
# mouse.click(coords=(214, 50))

# # 鼠标右键
# mouse.right_click(coords=(832, 507))

# # 鼠标双击
# mouse.double_click(button="left", coords=(553, 287))

# # 点击鼠标中键
# mouse.wheel_click(coords=(498, 228))

# # 按下鼠标
# mouse.press(coords=(34, 31))
# # 释放鼠标
# mouse.release(coords=(1000, 500))

# 滑动鼠标滚轮- wheel_dist:滚动次数,负数往下滚动，正数往上滚动
# mouse.scroll(coords=(850, 538), wheel_dist=2)

# 移动鼠标位置
mouse.move(coords=(0, 0))
for i in range(0, 1000, 50):
	mouse.move(coords=(i, i))

