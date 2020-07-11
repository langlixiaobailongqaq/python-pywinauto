"""
Python中GUI自动化工具介绍：

PyAutoGUi: 一个流行的跨平台库(只有基于图像的搜索功能,没有基于文本的控件操作)
Lackey：    基于图像模式匹配。
AXUI： MS UI Automation API控件的一个包装器。
winGuiAuto： 一个使用Win32 Api的控件模块。
Pywinauto ： 同时支持控件操作和图像操作，支持Win32 API和MS UI Automation API


安装前提：
	1.安装好python(建议使用python3.5以上的版本)
	2.确认pip 是否能正常使用

安装：
	1.在线安装：pip install pywinauto
	2.离线安装：python官网下载压缩包-解压压缩包-cmd进入文件夹中-运行 python setup.py install 进行安装

pywinauto中文文档:https://www.kancloud.cn/gnefnuy/pywinauto_doc/1193047
"""

CHANNEL = input("请输入你想修改的渠道,例如 happyGame：")
# print(CHANNEL)
# strip() 方法用于移除字符串头尾指定的字符 ,split()就是将一个字符串分裂成多个字符串组成的列表
channel_list = CHANNEL.strip(',').split(',')
# print(channel_list)

# channel = len(channel_list)
# print(channel)

for i in range(len(channel_list)):
	print(channel_list[i])