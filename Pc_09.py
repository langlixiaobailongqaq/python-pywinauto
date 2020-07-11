"""

窗口控件的分类：
	状态栏：StatusBar            静态内容：Static
	按钮：Button                复选框：CheckBOX
	单选框：RadioButton         组框：GroupBOX
	组合框：ComboxBox           对话框(窗口)：Dialog
	编辑栏：Edit                头部内容：Header
	列表框：ListBox             列表显示控件：ListView
	弹出菜单：PopupMenu         选项卡控件：TabControl
	工具栏：Toolbar             工具提示：ToolTips
	树状视图：Tree View         Menu：菜单
	Menultem：菜单项            Pane：窗格

"""

from pywinauto.application import Application

# 启动 navicat
app = Application("uia").start(r"D:\navicat112_premium_cs_x64\Navicat Premium\navicat.exe")

# 通过窗口标题去选择窗口
dlg = app["Navicat Premium"]
# 打印窗口中所有的控件
dlg.print_control_identifiers()