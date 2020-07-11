"""
PC端程序自动化的切入点：
	确定应用程序的可访问技术：
		如何确定应用程序的控件可访问技术(pywinauto的后端):

支持控件的访问技术：
	1. Win32 API(backend="win32")-默认的backend
		MEC, VB6, VCL, 简单的WinForms控件和大多数旧的应用程序

	2. MS UI Automation API(backend="uia")
		WinForms, WPF, Store apps, QT5,浏览器

启动应用程序：
	切入点主要是限制自动化控制进程的范围。如一个程序有多个实例,自动化控制一个实例，而保证其他实例(进程)不受影响。
	在pywinauto 中主要有两种对象可以建立这种入口点：

	一.Application：
		Application的作用范围是一个进程，如一般的桌面应用程序都为此类。

	二.Desktop：
		Desktop的作用范围可以跨进程。主要用于一个程序可以包含多个实例(进程)的程序
"""