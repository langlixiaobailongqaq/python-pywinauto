"""
pywinauto中的等待机制2：timings 模块
	wait_until方法：
		参数：
			Timeout：超时时间
			retry_interval：重试时间
			func：执行的函数
			value：比较的值
			Op：比较方式函数(默认为相等)
			args：给执行函数传位置参数
			kwargs：给执行函数传关键字参数

timings.Timings:
	在执行许多动作需要在之前，之后和之间如果我们需要暂停，
	那么模块timings中有几个方法库可以帮我们实现这种暂停操作。
	通过在对象timings.Timings 中设置全局静态变量(等待时间),它可以单独根据您的需要进行调整

	全局计时变量值的设置方法：
		Timings.defaults()：将全局计时设置为默认值
		Timings.slow() ：将所有时间加倍(使脚本执行速度降低约2倍)
		Timings.fast()：将所有计时除以2(快2倍)
"""
from pywinauto.timings import wait_until, Timings

i = 0
def work():
	global i
	i += 1
	print("当前i的值为：", i)
	return i

# 等work返回的结果为5的时候，继续往下执行
wait_until(10, 1, work, 5)
print("等待通过")


# 将等待的计时器设为默认值
Timings.Defaults()

# 将等待时间加倍
Timings.Slow()

# 将等待时间减半
Timings.Fast()