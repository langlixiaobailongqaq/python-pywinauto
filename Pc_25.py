"""

项目实战之行为封装
"""

import pywinauto
from pywinauto import mouse
import time
from pykeyboard import PyKeyboard


class NavicatTest:

	def __init__(self, path=None, precess=None):
		# 初始化应用程序对象
		if path:
			self.app = pywinauto.Application(backend='uia').start(path)
		else:
			self.app = pywinauto.Application(backend='uia').connect(process=precess)
		# 选择主窗口
		self.dlg = self.app['Navicat Premium']

	def new_connect(self, title, user, password):
		"""新建连接"""
		# 通过窗口标题去选择窗口
		dlg = self.app["Navicat Premium"]
		dlg.maximize()
		# 选择菜单
		menu = self.dlg["menu"]
		# menu.print_control_identifiers()

		# 选择菜单项：文件
		file = menu.child_window(title="文件", control_type="MenuItem")
		# 点击文件
		file.click_input()

		# 点击新建连接
		menu.item_by_path("文件->新建连接").click_input()
		# 点击MySQL...
		menu.item_by_path("文件->新建连接->MySQL...").click_input()

		# 选择新建连接的窗口
		new_dlg = self.app["MySQL - 新建连接"]
		# # new_dlg.print_control_identifiers()

		# 选择常规
		new_dlg['常规'].print_control_identifiers()
		# 输入连接名
		new_dlg['常规'].Edit5.type_keys(title)

		# 用户名
		new_dlg['常规'].Edit3.type_keys(user)
		# 密码
		new_dlg['常规'].Edit2.type_keys(password)
		new_dlg['连接测试'].click()
		# 点击 连接测试窗口的 确定
		new_dlg['TButton'].click()

		# 点击确定
		new_dlg['确定'].click()

		print("窗口的数量：", len(self.app.windows()))
		if len(self.app.windows()) > 2:
			# 添加连接失败,需要关闭弹窗和添加连接的窗口
				self.app['TWDialogForm'].close()

	def open_connect(self):
		"""打开连接(找不到控件,最好使用控件)"""
		mouse.right_click(coords=(57, 223))
		# 选择右击出现的上下文窗口
		self.app['上下文'].print_control_identifiers()
		# 打开连接
		self.app['上下文']['MenuItem1'].click_input()

	def del_connect(self):
		"""删除连接(找不到控件,最好使用控件)"""
		mouse.right_click(coords=(57, 223))
		# 删除连接
		self.app['上下文']['MenuItem6'].click_input()
		time.sleep(1)
		# 选择删除窗口
		self.app['TWDialogForm']['删除'].click()

	def close_connect(self, title):
		"""关闭连接"""
		mouse.right_click(coords=(57, 223))
		# 关闭连接
		self.app['上下文']['MenuItem1'].click_input()
		time.sleep(1)

	def open_database(self, database):
		"""打开数据库"""
		# 找不到TTreeView控件
		# self.dlg['TTreeView'].print_control_identifiers()
		mouse.right_click(coords=(69, 426))
		# 选择右击出现的上下文窗口
		self.app['上下文'].print_control_identifiers()
		# 打开数据库
		self.app['上下文']['MenuItem1'].click_input()

	def new_find_sql(self):
		"""新建查询窗口"""
		mouse.right_click(coords=(82, 523))
		# 选择右击出现的上下文窗口
		# self.app['上下文'].print_control_identifiers()
		# 新建查询
		self.app['上下文']['MenuItem1'].click_input()

	def find_sql(self, database, title, sql):
		"""查询sql"""
		# print(self.app.windows())
		title = '无标题 @{} ({}) - 查询 - Navicat Premium'.format(database, title)
		find_dlg = self.app[title]
		# find_dlg['TabControl'].Pane.print_control_identifiers()
		# 获取编辑框
		edit = find_dlg['TabControl'].Pane
		# 获取编辑窗口控件位置
		rect = edit.rectangle().mid_point()
		mouse.click(coords=(rect.x, rect.y))
		k = PyKeyboard()
		# 输入sql语句
		k.type_string("{}".format(sql))
		time.sleep(1)
		# 使用ctrl+r运行语句
		mouse.click(coords=(rect.x, rect.y))
		k.press_keys([k.control_key, 'r'])

	def get_connect_count(self):
		"""获取连接数量"""# TVTFilterFrame TVirtualStringTree(找不到控件：TVTFilterFrame)
		print(self.dlg['TVTFilterFrame']['TVirtualStringTree'].child_window())
		count = len(self.dlg['TVTFilterFrame'].children())
		return count

	def get_connect_names(self):
		"""获取所有连接名"""
		# 还是找不到控件：TVTFilterFrame
		connects = self.dlg['TVTFilterFrame'].children()
		# 获取连接名
		names = [i.tests()[0] for i in connects]
		return names


if __name__ == '__main__':
	nav = NavicatTest(precess=1556)
	# 新建连接
	nav.new_connect(title="test1", user='root', password='Zx123456')
	# 打开连接
	nav.open_connect()
	# 删除连接
	nav.del_connect()
	# 关闭连接
	nav.close_connect(title='test1')
	# 打开数据库
	nav.open_database(database='test')
	nav.new_find_sql()

	# 查询数据
	sql = "select * from students"
	nav.find_sql('test', 'win', sql)
	nav.get_connect_count()