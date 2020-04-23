

from pywinauto.application import Application
from pywinauto.mouse import *
from pywinauto.keyboard import *
import time
import os


"""
	Windows应用程序自动化测试
Windows上受支持的辅助功能技术列表：
Win32 API（backend="win32"） - 现在的默认后端
MFC，VB6，VCL，简单的WinForms控件和大多数旧的遗留应用程序
MS UI Automation（backend="uia"）
WinForms，WPF，商店应用，Qt5，浏览器
注意：Chrome --force-renderer-accessibility在启动前需要cmd标志。由于comtypes Python库限制，不支持自定义属性和控件。
"""
num = 0
class Pywin():
	def slotConfigTool(self):
		global num
		#  打开程序
		app = Application(backend="uia").start(
			r'C:/Users/Admin/Desktop/测试/项目需求/2019-7-11之后/测试小程序/SlotConfigTool/SlotConfigTool(24).exe')

		# 查到这个放水表测试程序主页面的控件树
		dlg_spec = app['SlotConfigTool']
		dlg_spec.print_control_identifiers()

		# 点击第一个Click
		app['SlotConfigTool'].Clicknum.click()

		# 点击第二个Click
		# app['SlotConfigTool'].Click2.click()

		# 查到第一个Click页面的控件树
		dlg_spec1 = app['修改配置Dialog']
		dlg_spec1.print_control_identifiers()

		# 定位香蕉输入框-通过控件的text或者title来查找控件-
		# edit = dlg_spec['香蕉']   # 1
		xiangjiao = dlg_spec['Edit1']  # 2
		# edit = dlg_spec.Edit0   # 3

		# 操作输入框-第一种方法是直接设置edit的text，而第二种是在里面模拟键盘输入
		xiangjiao.set_text(r'333')  # 1
		# edit.type_keys(r'E:\test test .exe',with_spaces = True)    # 2

		# 西瓜
		xigua = dlg_spec['Edit2']
		xigua.set_text(r'200')

		# 柠檬
		ningmeng = dlg_spec['Edit3']
		ningmeng.set_text(r'67')

		# 葡萄
		putao = dlg_spec['Edit4']
		putao.set_text(r'67')

		# 猕猴桃
		mihoutao = dlg_spec['Edit5']
		mihoutao.set_text(r'67')

		# 樱桃
		yingtao = dlg_spec['Edit6']
		yingtao.set_text(r'67')

		# 铃铛
		lingdang = dlg_spec['Edit7']
		lingdang.set_text(r'67')

		# BAR
		BAR = dlg_spec['Edit8']
		BAR.set_text(r'66')

		# bouns
		bouns = dlg_spec['Edit9']
		bouns.set_text(r'66')

		# 大7
		da_7 = dlg_spec['Edit10']
		da_7.set_text(r'0')

		# Wild
		wild = dlg_spec['Edit11']
		wild.set_text(r'0')

		# Wild3
		wild3 = dlg_spec['Edit12']
		wild3.set_text(r'0')

		# 第一个Cilck的 Free Spin  child_window(title="Free Spin：", auto_id="1013", control_type="Edit").set_text(r'111')
		Spin1 = dlg_spec['Edit13']
		Spin1.set_text(r'333')

		Spin2 = dlg_spec['Edit14']
		Spin2.set_text(r'200')

		Spin3 = dlg_spec['Edit15']
		Spin3.set_text(r'67')

		Spin4 = dlg_spec['Edit16']
		Spin4.set_text(r'67')

		Spin5 = dlg_spec['Edit17']
		Spin5.set_text(r'67')

		Spin6 = dlg_spec['Edit18']
		Spin6.set_text(r'67')

		Spin7 = dlg_spec['Edit19']
		Spin7.set_text(r'67')

		Spin8 = dlg_spec['Edit20']
		Spin8.set_text(r'66')

		Spin9 = dlg_spec['Edit21']
		Spin9.set_text(r'66')

		Spin10 = dlg_spec['Edit22']
		Spin10.set_text(r'0')

		Spin11 = dlg_spec['Edit23']
		Spin11.set_text(r'0')

		Spin12 = dlg_spec['Edit24']
		Spin12.set_text(r'0')

		# 保存配置
		app['SlotConfigTool'].Button1.click()

		for i in range(13):
			#  打开程序
			app = Application(backend="uia").start(r'C:/Users/Admin/Desktop/测试/项目需求/2019-7-11之后/测试小程序/SlotConfigTool/SlotConfigTool(24).exe')

			# 查到这个放水表测试程序主页面的控件树
			dlg_spec = app['SlotConfigTool']
			dlg_spec.print_control_identifiers()

			# 点击第num个Click
			app['SlotConfigTool'].Clicknum.click()

			# 点击第二个Click
			# app['SlotConfigTool'].Click2.click()

			# 查到第一个Click页面的控件树
			dlg_spec1 = app['修改配置Dialog']
			dlg_spec1.print_control_identifiers()

			# 定位香蕉输入框-通过控件的text或者title来查找控件-
			# edit = dlg_spec['香蕉']   # 1
			xiangjiao = dlg_spec['Edit1']    # 2
			# edit = dlg_spec.Edit0   # 3

			# 操作输入框-第一种方法是直接设置edit的text，而第二种是在里面模拟键盘输入
			xiangjiao.set_text(r'333')     # 1
			# edit.type_keys(r'E:\test test .exe',with_spaces = True)    # 2

			# 西瓜
			xigua = dlg_spec['Edit2']
			xigua.set_text(r'200')

			# 柠檬
			ningmeng = dlg_spec['Edit3']
			ningmeng.set_text(r'67')

			# 葡萄
			putao = dlg_spec['Edit4']
			putao.set_text(r'67')

			# 猕猴桃
			mihoutao = dlg_spec['Edit5']
			mihoutao.set_text(r'67')

			# 樱桃
			yingtao = dlg_spec['Edit6']
			yingtao.set_text(r'67')

			# 铃铛
			lingdang = dlg_spec['Edit7']
			lingdang.set_text(r'67')

			# BAR
			BAR = dlg_spec['Edit8']
			BAR.set_text(r'66')

			# bouns
			bouns = dlg_spec['Edit9']
			bouns.set_text(r'66')

			# 大7
			da_7 = dlg_spec['Edit10']
			da_7.set_text(r'0')

			# Wild
			wild = dlg_spec['Edit11']
			wild.set_text(r'0')

			# Wild3
			wild3 = dlg_spec['Edit12']
			wild3.set_text(r'0')

			# 第一个Cilck的 Free Spin  child_window(title="Free Spin：", auto_id="1013", control_type="Edit").set_text(r'111')
			Spin1 = dlg_spec['Edit13']
			Spin1.set_text(r'333')

			Spin2 = dlg_spec['Edit14']
			Spin2.set_text(r'200')

			Spin3 = dlg_spec['Edit15']
			Spin3.set_text(r'67')

			Spin4 = dlg_spec['Edit16']
			Spin4.set_text(r'67')

			Spin5 = dlg_spec['Edit17']
			Spin5.set_text(r'67')

			Spin6 = dlg_spec['Edit18']
			Spin6.set_text(r'67')

			Spin7 = dlg_spec['Edit19']
			Spin7.set_text(r'67')

			Spin8 = dlg_spec['Edit20']
			Spin8.set_text(r'66')

			Spin9 = dlg_spec['Edit21']
			Spin9.set_text(r'66')

			Spin10 = dlg_spec['Edit22']
			Spin10.set_text(r'0')

			Spin11 = dlg_spec['Edit23']
			Spin11.set_text(r'0')

			Spin12 = dlg_spec['Edit24']
			Spin12.set_text(r'0')

			# 保存配置
			app['SlotConfigTool'].Button1.click()

			# 关闭按钮（"X"）
			# app['SlotConfigTool'].Button2.click()
			num = num + 1




Pw = Pywin()
Pw.slotConfigTool()

# if __name__ == "__main__":
# 	Pw.slotConfigTool()


"""
		SlotConfigTool页面的控件树：
Dialog - 'SlotConfigTool'    (L956, T493, R1499, B857)
['Dialog', 'SlotConfigTool', 'SlotConfigToolDialog']
child_window(title="SlotConfigTool", control_type="Window")
   |
   | Button - '生成测试数据'    (L1150, T825, R1252, B848)
   | ['生成测试数据', 'Button0', '生成测试数据Button', 'Button', 'Button1']
   | child_window(title="生成测试数据", auto_id="1001", control_type="Button")
   |
   | Static - '测试局数：'    (L967, T830, R1029, B843)
   | ['Static0', 'Static1', '测试局数：Static', 'Static', '测试局数：']
   | child_window(title="测试局数：", control_type="Text")
   |
   | Edit - '测试局数：'    (L1032, T825, R1118, B848)
   | ['', '1', 'Edit', 'Edit0', '测试局数：Edit', 'Edit1', '0']
   | child_window(title="测试局数：", auto_id="1002", control_type="Edit")
   |
   | Edit - ''    (L1335, T825, R1454, B848)
   | ['Edit2', '2']
   | child_window(auto_id="1003", control_type="Edit")
   |
   | Static - '奖池总额：'    (L1270, T828, R1332, B841)
   | ['Static2', '奖池总额：Static', '奖池总额：']
   | child_window(title="奖池总额：", control_type="Text")
   |
   | Edit - '奖池总额：'    (L1011, T787, R1071, B810)
   | ['Edit3', '3']
   | child_window(title="奖池总额：", auto_id="1004", control_type="Edit")
   |
   | Button - '-'    (L978, T787, R1002, B810)
   | ['-Button', 'Button2', '-Button1', '-0', '-Button0', '-', '-1']
   | child_window(title="-", auto_id="1005", control_type="Button")
   |
   | Button - '+'    (L1081, T787, R1105, B810)
   | ['+1', '+Button', 'Button3', '+', '+Button1', '+0', '+Button0']
   | child_window(title="+", auto_id="1006", control_type="Button")
   |
   | Edit - ''    (L1176, T786, R1236, B809)
   | ['4', 'Edit4']
   | child_window(auto_id="1007", control_type="Edit")
   |
   | Button - '-'    (L1146, T786, R1170, B809)
   | ['-2', '-Button2', 'Button4']
   | child_window(title="-", auto_id="1008", control_type="Button")
   |
   | Button - '+'    (L1242, T786, R1266, B809)
   | ['Button5', '+Button2', '+2']
   | child_window(title="+", auto_id="1009", control_type="Button")
   |
   | Static - 'VIP等级：'    (L1290, T791, R1344, B804)
   | ['Static3', 'VIP等级：Static', 'VIP等级：']
   | child_window(title="VIP等级：", control_type="Text")
   |
   | Edit - 'VIP等级：'    (L1353, T786, R1410, B809)
   | ['VIP等级：Edit', '5', 'Edit5']
   | child_window(title="VIP等级：", auto_id="1010", control_type="Edit")
   |
   | Button - 'Click'    (L974, T534, R1024, B584)
   | ['Click0', 'ClickButton1', 'ClickButton0', 'Click', 'Button6', 'ClickButton', 'Click1']
   | child_window(title="Click", auto_id="10", control_type="Button")
   |
   | Button - 'Click'    (L1044, T534, R1094, B584)
   | ['ClickButton2', 'Click2', 'Button7']
   | child_window(title="Click", auto_id="11", control_type="Button")
   |
   | Button - 'Click'    (L1114, T534, R1164, B584)
   | ['Button8', 'ClickButton3', 'Click3']
   | child_window(title="Click", auto_id="12", control_type="Button")
   |
   | Button - 'Click'    (L1184, T534, R1234, B584)
   | ['Click4', 'Button9', 'ClickButton4']
   | child_window(title="Click", auto_id="13", control_type="Button")
   |
   | Button - 'Click'    (L1254, T534, R1304, B584)
   | ['Button10', 'ClickButton5', 'Click5']
   | child_window(title="Click", auto_id="14", control_type="Button")
   |
   | Button - 'Click'    (L974, T604, R1024, B654)
   | ['ClickButton6', 'Click6', 'Button11']
   | child_window(title="Click", auto_id="15", control_type="Button")
   |
   | Button - 'Click'    (L1044, T604, R1094, B654)
   | ['ClickButton7', 'Click7', 'Button12']
   | child_window(title="Click", auto_id="16", control_type="Button")
   |
   | Button - 'Click'    (L1114, T604, R1164, B654)
   | ['Button13', 'Click8', 'ClickButton8']
   | child_window(title="Click", auto_id="17", control_type="Button")
   |
   | Button - 'Click'    (L1184, T604, R1234, B654)
   | ['Click9', 'Button14', 'ClickButton9']
   | child_window(title="Click", auto_id="18", control_type="Button")
   |
   | Button - 'Click'    (L1254, T604, R1304, B654)
   | ['ClickButton10', 'Click10', 'Button15']
   | child_window(title="Click", auto_id="19", control_type="Button")
   |
   | Button - 'Click'    (L974, T674, R1024, B724)
   | ['Button16', 'Click11', 'ClickButton11']
   | child_window(title="Click", auto_id="20", control_type="Button")
   |
   | Button - 'Click'    (L1044, T674, R1094, B724)
   | ['Click12', 'ClickButton12', 'Button17']
   | child_window(title="Click", auto_id="21", control_type="Button")
   |
   | Button - 'Click'    (L1114, T674, R1164, B724)
   | ['Button18', 'Click13', 'ClickButton13']
   | child_window(title="Click", auto_id="22", control_type="Button")
   |
   | Button - 'Click'    (L1184, T674, R1234, B724)
   | ['Button19', 'ClickButton14', 'Click14']
   | child_window(title="Click", auto_id="23", control_type="Button")
   |
   | Button - 'Click'    (L1254, T674, R1304, B724)
   | ['Click15', 'ClickButton15', 'Button20']
   | child_window(title="Click", auto_id="24", control_type="Button")
   |
   | TitleBar - 'None'    (L980, T496, R1491, B524)
   | ['TitleBar', '6']
   |    |
   |    | Menu - '系统'    (L964, T501, R986, B523)
   |    | ['系统', '系统1', '系统Menu', 'Menu', '系统0']
   |    | child_window(title="系统", auto_id="MenuBar", control_type="MenuBar")
   |    |    |
   |    |    | MenuItem - '系统'    (L964, T501, R986, B523)
   |    |    | ['系统2', 'MenuItem', '系统MenuItem']
   |    |    | child_window(title="系统", control_type="MenuItem")
   |    |
   |    | Button - '关闭'    (L1458, T494, R1492, B524)
   |    | ['Button21', '关闭', '关闭Button']
   |    | child_window(title="关闭", control_type="Button")



	第一个Click修改配置页面的控件树：

Dialog - 'SlotConfigTool'    (L1105, T486, R1648, B850)
['Dialog', 'SlotConfigTool', 'Dialog1', 'Dialog0', 'SlotConfigToolDialog']
child_window(title="SlotConfigTool", control_type="Window")
   |
   | Dialog - '修改配置'    (L1118, T396, R1634, B940)
   | ['修改配置Dialog', 'Dialog2', '修改配置']
   | child_window(title="修改配置", control_type="Window")
   |    |
   |    | Button - '保存配置'    (L1315, T898, R1390, B921)
   |    | ['Button1', 'Button0', '保存配置', 'Button', '保存配置Button']
   |    | child_window(title="保存配置", auto_id="1", control_type="Button")
   |    |
   |    | Static - '香蕉：'    (L1158, T447, R1205, B460)
   |    | ['Static1', 'Static', 'Static0', '香蕉：Static', '香蕉：']
   |    | child_window(title="香蕉：", control_type="Text")
   |    |
   |    | Edit - '香蕉：'    (L1209, T443, R1331, B466)
   |    | ['', '1', 'Edit', '0', '香蕉：Edit', 'Edit0', 'Edit1']
   |    | child_window(title="香蕉：", auto_id="1000", control_type="Edit")
   |    |
   |    | Static - '西瓜：'    (L1159, T482, R1206, B495)
   |    | ['西瓜：Static', '西瓜：', 'Static2']
   |    | child_window(title="西瓜：", control_type="Text")
   |    |
   |    | Edit - '西瓜：'    (L1210, T477, R1332, B500)
   |    | ['西瓜：Edit', '2', 'Edit2']
   |    | child_window(title="西瓜：", auto_id="1001", control_type="Edit")
   |    |
   |    | Static - '柠檬：'    (L1159, T516, R1206, B529)
   |    | ['柠檬：', 'Static3', '柠檬：Static']
   |    | child_window(title="柠檬：", control_type="Text")
   |    |
   |    | Edit - '柠檬：'    (L1210, T513, R1332, B536)
   |    | ['柠檬：Edit', 'Edit3', '3']
   |    | child_window(title="柠檬：", auto_id="1002", control_type="Edit")
   |    |
   |    | Static - '葡萄：'    (L1159, T551, R1206, B564)
   |    | ['葡萄：Static', '葡萄：', 'Static4']
   |    | child_window(title="葡萄：", control_type="Text")
   |    |
   |    | Edit - '葡萄：'    (L1210, T546, R1332, B569)
   |    | ['4', 'Edit4', '葡萄：Edit']
   |    | child_window(title="葡萄：", auto_id="1003", control_type="Edit")
   |    |
   |    | Static - '猕猴桃：'    (L1137, T588, R1206, B601)
   |    | ['猕猴桃：', 'Static5', '猕猴桃：Static']
   |    | child_window(title="猕猴桃：", control_type="Text")
   |    |
   |    | Edit - '猕猴桃：'    (L1210, T583, R1332, B606)
   |    | ['猕猴桃：Edit', 'Edit5', '5']
   |    | child_window(title="猕猴桃：", auto_id="1004", control_type="Edit")
   |    |
   |    | Static - '樱桃：'    (L1137, T625, R1206, B638)
   |    | ['樱桃：', 'Static6', '樱桃：Static']
   |    | child_window(title="樱桃：", control_type="Text")
   |    |
   |    | Edit - '樱桃：'    (L1210, T620, R1332, B643)
   |    | ['樱桃：Edit', 'Edit6', '6']
   |    | child_window(title="樱桃：", auto_id="1005", control_type="Edit")
   |    |
   |    | Static - '铃铛：'    (L1137, T659, R1206, B672)
   |    | ['铃铛：Static', 'Static7', '铃铛：']
   |    | child_window(title="铃铛：", control_type="Text")
   |    |
   |    | Edit - '铃铛：'    (L1210, T655, R1332, B678)
   |    | ['铃铛：Edit', 'Edit7', '7']
   |    | child_window(title="铃铛：", auto_id="1006", control_type="Edit")
   |    |
   |    | Static - 'BAR：'    (L1137, T694, R1206, B707)
   |    | ['BAR：Static', 'BAR：', 'Static8']
   |    | child_window(title="BAR：", control_type="Text")
   |    |
   |    | Edit - 'BAR：'    (L1210, T690, R1332, B713)
   |    | ['8', 'BAR：Edit', 'Edit8']
   |    | child_window(title="BAR：", auto_id="1007", control_type="Edit")
   |    |
   |    | Static - 'bonus：'    (L1137, T729, R1206, B742)
   |    | ['bonus：Static', 'Static9', 'bonus：']
   |    | child_window(title="bonus：", control_type="Text")
   |    |
   |    | Edit - 'bonus：'    (L1210, T726, R1332, B749)
   |    | ['bonus：Edit', 'Edit9', '9']
   |    | child_window(title="bonus：", auto_id="1008", control_type="Edit")
   |    |
   |    | Static - '大7：'    (L1137, T763, R1206, B776)
   |    | ['大7：', 'Static10', '大7：Static']
   |    | child_window(title="大7：", control_type="Text")
   |    |
   |    | Edit - '大7：'    (L1210, T760, R1332, B783)
   |    | ['Edit10', '大7：Edit', '10']
   |    | child_window(title="大7：", auto_id="1009", control_type="Edit")
   |    |
   |    | Static - 'Wild：'    (L1137, T799, R1206, B812)
   |    | ['Wild：Static', 'Wild：', 'Static11']
   |    | child_window(title="Wild：", control_type="Text")
   |    |
   |    | Edit - 'Wild：'    (L1210, T796, R1332, B819)
   |    | ['Edit11', '11', 'Wild：Edit']
   |    | child_window(title="Wild：", auto_id="1010", control_type="Edit")
   |    |
   |    | Static - 'Wild3：'    (L1137, T838, R1206, B851)
   |    | ['Static12', 'Wild3：', 'Wild3：Static']
   |    | child_window(title="Wild3：", control_type="Text")
   |    |
   |    | Edit - 'Wild3：'    (L1210, T835, R1332, B858)
   |    | ['Wild3：Edit', '12', 'Edit12']
   |    | child_window(title="Wild3：", auto_id="1011", control_type="Edit")
   |    |
   |    | Edit - ''    (L1416, T443, R1538, B466)
   |    | ['Edit13', '13']
   |    | child_window(auto_id="1012", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1354, T447, R1414, B460)
   |    | ['Free Spin：Static0', 'Free Spin：Static1', 'Free Spin：0', 'Free Spin：Static', 'Static13', 'Free Spin：', 'Free Spin：1']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Static - 'Free Spin：'    (L1351, T481, R1411, B494)
   |    | ['Static14', 'Free Spin：2', 'Free Spin：Static2']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1416, T477, R1538, B500)
   |    | ['Free Spin：Edit1', '14', 'Free Spin：Edit0', 'Edit14', 'Free Spin：Edit']
   |    | child_window(title="Free Spin：", auto_id="1013", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1351, T516, R1411, B529)
   |    | ['Static15', 'Free Spin：3', 'Free Spin：Static3']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1416, T512, R1538, B535)
   |    | ['Edit15', 'Free Spin：Edit2', '15']
   |    | child_window(title="Free Spin：", auto_id="1014", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1353, T549, R1413, B562)
   |    | ['Free Spin：Static4', 'Static16', 'Free Spin：4']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1417, T544, R1539, B567)
   |    | ['Edit16', '16', 'Free Spin：Edit3']
   |    | child_window(title="Free Spin：", auto_id="1015", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1351, T585, R1411, B598)
   |    | ['Free Spin：Static5', 'Free Spin：5', 'Static17']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1416, T581, R1538, B604)
   |    | ['Free Spin：Edit4', '17', 'Edit17']
   |    | child_window(title="Free Spin：", auto_id="1016", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1353, T624, R1413, B637)
   |    | ['Free Spin：Static6', 'Static18', 'Free Spin：6']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1416, T619, R1538, B642)
   |    | ['Edit18', '18', 'Free Spin：Edit5']
   |    | child_window(title="Free Spin：", auto_id="1017", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1354, T659, R1414, B672)
   |    | ['Free Spin：Static7', 'Static19', 'Free Spin：7']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1416, T655, R1538, B678)
   |    | ['Edit19', '19', 'Free Spin：Edit6']
   |    | child_window(title="Free Spin：", auto_id="1018", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1353, T692, R1413, B705)
   |    | ['Free Spin：8', 'Free Spin：Static8', 'Static20']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1414, T690, R1536, B713)
   |    | ['Free Spin：Edit7', 'Edit20', '20']
   |    | child_window(title="Free Spin：", auto_id="1019", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1350, T729, R1410, B742)
   |    | ['Static21', 'Free Spin：Static9', 'Free Spin：9']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1416, T723, R1538, B746)
   |    | ['Free Spin：Edit8', '21', 'Edit21']
   |    | child_window(title="Free Spin：", auto_id="1020", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1351, T762, R1411, B775)
   |    | ['Static22', 'Free Spin：Static10', 'Free Spin：10']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1414, T759, R1536, B782)
   |    | ['Edit22', '22', 'Free Spin：Edit9']
   |    | child_window(title="Free Spin：", auto_id="1021", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1351, T799, R1411, B812)
   |    | ['Static23', 'Free Spin：11', 'Free Spin：Static11']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1413, T794, R1535, B817)
   |    | ['Edit23', 'Free Spin：Edit10', '23']
   |    | child_window(title="Free Spin：", auto_id="1023", control_type="Edit")
   |    |
   |    | Static - 'Free Spin：'    (L1351, T837, R1411, B850)
   |    | ['Free Spin：Static12', 'Free Spin：12', 'Static24']
   |    | child_window(title="Free Spin：", control_type="Text")
   |    |
   |    | Edit - 'Free Spin：'    (L1414, T832, R1536, B855)
   |    | ['Free Spin：Edit11', '24', 'Edit24']
   |    | child_window(title="Free Spin：", auto_id="1024", control_type="Edit")
   |    |
   |    | TitleBar - 'None'    (L1126, T399, R1626, B427)
   |    | ['TitleBar1', 'TitleBar0', 'TitleBar', '25']
   |    |    |
   |    |    | Button - '关闭'    (L1593, T397, R1627, B427)
   |    |    | ['Button2', '关闭Button1', '关闭1', '关闭', '关闭0', '关闭Button', '关闭Button0']
   |    |    | child_window(title="关闭", control_type="Button")
   |
   | Button - '生成测试数据'    (L1299, T818, R1401, B841)
   | ['生成测试数据Button', '生成测试数据', 'Button3']
   | child_window(title="生成测试数据", auto_id="1001", control_type="Button")
   |
   | Static - '测试局数：'    (L1116, T823, R1178, B836)
   | ['测试局数：Static', 'Static25', '测试局数：']
   | child_window(title="测试局数：", control_type="Text")
   |
   | Edit - '测试局数：'    (L1181, T818, R1267, B841)
   | ['Edit25', '测试局数：Edit', '26']
   | child_window(title="测试局数：", auto_id="1002", control_type="Edit")
   |
   | Edit - ''    (L1484, T818, R1603, B841)
   | ['27', 'Edit26']
   | child_window(auto_id="1003", control_type="Edit")
   |
   | Static - '奖池总额：'    (L1419, T821, R1481, B834)
   | ['奖池总额：Static', 'Static26', '奖池总额：']
   | child_window(title="奖池总额：", control_type="Text")
   |
   | Edit - '奖池总额：'    (L1160, T780, R1220, B803)
   | ['28', 'Edit27']
   | child_window(title="奖池总额：", auto_id="1004", control_type="Edit")
   |
   | Button - '-'    (L1127, T780, R1151, B803)
   | ['-', 'Button4', '-Button0', '-Button', '-Button1', '-0', '-1']
   | child_window(title="-", auto_id="1005", control_type="Button")
   |
   | Button - '+'    (L1230, T780, R1254, B803)
   | ['+1', '+Button0', '+', '+Button1', 'Button5', '+0', '+Button']
   | child_window(title="+", auto_id="1006", control_type="Button")
   |
   | Edit - ''    (L1325, T779, R1385, B802)
   | ['Edit28', '29']
   | child_window(auto_id="1007", control_type="Edit")
   |
   | Button - '-'    (L1295, T779, R1319, B802)
   | ['-2', 'Button6', '-Button2']
   | child_window(title="-", auto_id="1008", control_type="Button")
   |
   | Button - '+'    (L1391, T779, R1415, B802)
   | ['+Button2', 'Button7', '+2']
   | child_window(title="+", auto_id="1009", control_type="Button")
   |
   | Static - 'VIP等级：'    (L1439, T784, R1493, B797)
   | ['VIP等级：Static', 'Static27', 'VIP等级：']
   | child_window(title="VIP等级：", control_type="Text")
   |
   | Edit - 'VIP等级：'    (L1502, T779, R1559, B802)
   | ['VIP等级：Edit', 'Edit29', '30']
   | child_window(title="VIP等级：", auto_id="1010", control_type="Edit")
   |
   | Button - 'Click'    (L1123, T527, R1173, B577)
   | ['ClickButton', 'Click0', 'Click', 'ClickButton0', 'ClickButton1', 'Button8', 'Click1']
   | child_window(title="Click", auto_id="10", control_type="Button")
   |
   | Button - 'Click'    (L1193, T527, R1243, B577)
   | ['Click2', 'Button9', 'ClickButton2']
   | child_window(title="Click", auto_id="11", control_type="Button")
   |
   | Button - 'Click'    (L1263, T527, R1313, B577)
   | ['ClickButton3', 'Button10', 'Click3']
   | child_window(title="Click", auto_id="12", control_type="Button")
   |
   | Button - 'Click'    (L1333, T527, R1383, B577)
   | ['Click4', 'Button11', 'ClickButton4']
   | child_window(title="Click", auto_id="13", control_type="Button")
   |
   | Button - 'Click'    (L1403, T527, R1453, B577)
   | ['Button12', 'ClickButton5', 'Click5']
   | child_window(title="Click", auto_id="14", control_type="Button")
   |
   | Button - 'Click'    (L1123, T597, R1173, B647)
   | ['ClickButton6', 'Click6', 'Button13']
   | child_window(title="Click", auto_id="15", control_type="Button")
   |
   | Button - 'Click'    (L1193, T597, R1243, B647)
   | ['Click7', 'Button14', 'ClickButton7']
   | child_window(title="Click", auto_id="16", control_type="Button")
   |
   | Button - 'Click'    (L1263, T597, R1313, B647)
   | ['ClickButton8', 'Button15', 'Click8']
   | child_window(title="Click", auto_id="17", control_type="Button")
   |
   | Button - 'Click'    (L1333, T597, R1383, B647)
   | ['Button16', 'Click9', 'ClickButton9']
   | child_window(title="Click", auto_id="18", control_type="Button")
   |
   | Button - 'Click'    (L1403, T597, R1453, B647)
   | ['ClickButton10', 'Button17', 'Click10']
   | child_window(title="Click", auto_id="19", control_type="Button")
   |
   | Button - 'Click'    (L1123, T667, R1173, B717)
   | ['Button18', 'ClickButton11', 'Click11']
   | child_window(title="Click", auto_id="20", control_type="Button")
   |
   | Button - 'Click'    (L1193, T667, R1243, B717)
   | ['Click12', 'Button19', 'ClickButton12']
   | child_window(title="Click", auto_id="21", control_type="Button")
   |
   | Button - 'Click'    (L1263, T667, R1313, B717)
   | ['Button20', 'ClickButton13', 'Click13']
   | child_window(title="Click", auto_id="22", control_type="Button")
   |
   | Button - 'Click'    (L1333, T667, R1383, B717)
   | ['Button21', 'ClickButton14', 'Click14']
   | child_window(title="Click", auto_id="23", control_type="Button")
   |
   | Button - 'Click'    (L1403, T667, R1453, B717)
   | ['Button22', 'ClickButton15', 'Click15']
   | child_window(title="Click", auto_id="24", control_type="Button")
   |
   | TitleBar - 'None'    (L1129, T489, R1640, B517)
   | ['TitleBar2', '31']
   |    |
   |    | Menu - '系统'    (L1113, T494, R1135, B516)
   |    | ['系统1', '系统0', '系统', '系统Menu', 'Menu']
   |    | child_window(title="系统", auto_id="MenuBar", control_type="MenuBar")
   |    |    |
   |    |    | MenuItem - '系统'    (L1113, T494, R1135, B516)
   |    |    | ['系统MenuItem', '系统2', 'MenuItem']
   |    |    | child_window(title="系统", control_type="MenuItem")
   |    |
   |    | Button - '关闭'    (L1607, T487, R1641, B517)
   |    | ['关闭2', 'Button23', '关闭Button2']
   |    | child_window(title="关闭", control_type="Button")

In [27]:



























"""