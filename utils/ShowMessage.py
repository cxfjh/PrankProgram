from os import path  # 导入 os 库 处理路径
import sys  # 导入系统库 处理路径
from tkinter import Tk, Label   # 导入 tkinter 库 处理 GUI 界面
from threading import Thread  # 导入线程库 处理多线程
from time import sleep  # 导入时间库 处理延时
import pyautogui  # 导入 pyautogui 库 处理鼠标键盘操作
from random import randint  # 导入随机数库 处理随机数


# 警告弹窗
def warningMessage(x, y):
    root = Tk()  # 创建主窗口
    root.title("错误警告")  # 设置窗口标题
    root.geometry(f"300x200+{x}+{y}")  # 设置窗口大小和位置
    root.resizable(False, False)  # 设置窗口不可缩放
    root.attributes("-topmost", True)  # 设置窗口置顶
    label = Label(root, text="系统正在遭受网络攻击", padx=20, pady=20, font=("Helvetica", 20), fg="red")  # 创建标签并将其放置在窗口中
    label.pack(expand=True)  # 设置标签自动适应窗口大小
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # 设置窗口关闭事件，禁止关闭窗口
    root.after(5000, root.destroy)  # 设置秒后关闭窗口
    root.mainloop()  # 进入消息循环


# 读取数据并将其转换为二维数据
def readData():
    filePath = path.join(sys._MEIPASS, "positions.txt") if getattr(sys, 'frozen', False) else "static/popups/positions.txt" 
    data = [] # 二维数组
    with open(filePath, 'r') as file: # 读取文件
        for line in file: # 遍历每行
            coords = line.strip().split() # 去除行末的换行符并拆分为坐标
            if len(coords) == 2: data.append([int(coords[0]), int(coords[1])]) # 转换为整数并添加到二维数组
    return data # 返回二维数组


# 显示弹窗
def showMessage():
    positionsData = readData() # 二维数组
    screenWidth, screenHeight = pyautogui.size() # 获取屏幕尺寸

    for coords in positionsData: # 遍历二维数组
        sleep(0.05)  # 延时 0.1 秒
        Thread(target=warningMessage, args=(coords[0], coords[1])).start()  # 启动线程，调用 message 函数并传入坐标参数

    while True:  # 死循环，持续生成随机坐标的警告弹窗
        sleep(0.05)  # 延时 0.1 秒
        Thread(target=warningMessage, args=((randint(0, screenWidth), randint(0, screenHeight),))).start()  # 启动线程，调用 pyautogui.click 函数并传入屏幕中心坐标

